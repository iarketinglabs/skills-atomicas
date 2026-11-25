import { createServer } from "node:http";
import { readFile, realpath, stat } from "node:fs/promises";
import { dirname, extname, isAbsolute, relative, resolve, sep } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const MODULE_DIR = dirname(fileURLToPath(import.meta.url));
const PORT = Number(process.argv[2]) || 4545;
const HOST = "127.0.0.1";

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
};

function isWithinRoot(root, candidate) {
  const relativePath = relative(root, candidate);
  return relativePath === "" || (
    relativePath !== ".." &&
    !relativePath.startsWith(".." + sep) &&
    !isAbsolute(relativePath)
  );
}

export function resolveRequestPath(requestTarget, rootDir = MODULE_DIR) {
  const rawTarget = String(requestTarget || "/");
  const rawPath = rawTarget.split(/[?#]/, 1)[0] || "/";
  if (!rawPath.startsWith("/")) return null;

  let decodedPath;
  try {
    decodedPath = decodeURIComponent(rawPath);
  } catch {
    return null;
  }

  if (decodedPath.includes(String.fromCharCode(0))) return null;
  const requestedPath = decodedPath === "/" ? "/index.html" : decodedPath;
  const root = resolve(rootDir);
  const candidate = resolve(root, "." + requestedPath);
  return isWithinRoot(root, candidate) ? candidate : null;
}

export function createDashboardServer(rootDir = MODULE_DIR) {
  const root = resolve(rootDir);

  return createServer(async (req, res) => {
    if (req.method !== "GET" && req.method !== "HEAD") {
      res.writeHead(405, { Allow: "GET, HEAD", "Content-Type": "text/plain; charset=utf-8" });
      res.end("Method not allowed");
      return;
    }

    const candidate = resolveRequestPath(req.url, root);
    if (!candidate) {
      res.writeHead(403, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Forbidden");
      return;
    }

    try {
      const [realRoot, realFile] = await Promise.all([realpath(root), realpath(candidate)]);
      if (!isWithinRoot(realRoot, realFile)) {
        res.writeHead(403, { "Content-Type": "text/plain; charset=utf-8" });
        res.end("Forbidden");
        return;
      }

      const fileInfo = await stat(realFile);
      if (!fileInfo.isFile()) {
        res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
        res.end("Not found");
        return;
      }

      const ext = extname(realFile).toLowerCase();
      res.writeHead(200, { "Content-Type": MIME[ext] || "application/octet-stream" });
      if (req.method === "HEAD") {
        res.end();
        return;
      }
      res.end(await readFile(realFile));
    } catch {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Not found");
    }
  });
}

export function listenDashboardServer(port = PORT, rootDir = MODULE_DIR) {
  const server = createDashboardServer(rootDir);
  return new Promise((resolveServer, reject) => {
    const onError = (error) => reject(error);
    server.once("error", onError);
    server.listen(port, HOST, () => {
      server.off("error", onError);
      resolveServer(server);
    });
  });
}

const isMain = process.argv[1] && pathToFileURL(resolve(process.argv[1])).href === import.meta.url;
if (isMain) {
  listenDashboardServer().then(() => {
    console.log("Dashboard rodando em http://127.0.0.1:" + PORT);
    console.log("Ctrl+C para parar.");
  }).catch(() => {
    console.error("Não foi possível iniciar o dashboard.");
    process.exitCode = 1;
  });
}
