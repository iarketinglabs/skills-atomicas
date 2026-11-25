import assert from "node:assert/strict";
import { after, before, test } from "node:test";
import { mkdtemp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { request } from "node:http";
import { listenDashboardServer, resolveRequestPath } from "../assets/kanban-dashboard/server.mjs";

let rootDir;
let server;
let baseUrl;

before(async () => {
  rootDir = await mkdtemp(join(tmpdir(), "kanban-dashboard-test-"));
  await mkdir(join(rootDir, "dashboard"));
  await mkdir(join(rootDir, "dashboard-private"));
  await writeFile(join(rootDir, "dashboard", "index.html"), "public dashboard");
  await writeFile(join(rootDir, "dashboard-private", "secret.txt"), "private sibling");
  server = await listenDashboardServer(0, join(rootDir, "dashboard"));
  const address = server.address();
  baseUrl = `http://127.0.0.1:${address.port}`;
});

after(async () => {
  if (server) await new Promise((resolve) => server.close(resolve));
  if (rootDir) await rm(rootDir, { recursive: true, force: true });
});

function get(path) {
  return new Promise((resolve, reject) => {
    const base = new URL(baseUrl);
    const req = request(
      { hostname: base.hostname, port: base.port, path, method: "GET" },
      (res) => {
      const chunks = [];
      res.on("data", (chunk) => chunks.push(chunk));
      res.on("end", () => resolve({ status: res.statusCode, body: Buffer.concat(chunks).toString() }));
      },
    );
    req.on("error", reject);
    req.end();
  });
}

test("rejects a traversal into a sibling directory with a shared prefix", async () => {
  assert.equal(resolveRequestPath("/%2e%2e/dashboard-private/secret.txt", join(rootDir, "dashboard")), null);
  const response = await get("/%2e%2e/dashboard-private/secret.txt");
  assert.equal(response.status, 403);
  assert.notEqual(response.body, "private sibling");
});

test("rejects decoded NUL bytes before resolving a filesystem path", () => {
  assert.equal(resolveRequestPath("/%00index.html", join(rootDir, "dashboard")), null);
});

test("serves files from the dashboard root only", async () => {
  const response = await get("/");
  assert.equal(response.status, 200);
  assert.equal(response.body, "public dashboard");
});

test("binds the dashboard server to loopback", () => {
  assert.equal(server.address().address, "127.0.0.1");
});
