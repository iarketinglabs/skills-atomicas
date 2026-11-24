import { readFileSync, readdirSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const textFile = /(?:\.(?:md|markdown|mdx|txt|toml|html?|css|scss|svg|json|jsonc|xml|tsx?|jsx?|[cm]?js|py|ps1|ya?ml|csv|tsv|sql|sh|bat|cmd|env|ini|cfg|conf|gitignore|gitattributes|editorconfig|example|sample|template)|\/?Dockerfile|\/?Makefile)$/i;
const secretTokens = /(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{45,}|(?:AKIA|ASIA)[A-Z0-9]{16}|xox[baprs]-[A-Za-z0-9-]{15,}|sk-(?:(?:proj|live|test|ant-api[0-9])-)?[A-Za-z0-9_-]{20,}|AIza[A-Za-z0-9_-]{32,}|hf_[A-Za-z0-9]{30,}|-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----|eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{8,})/;
const secretAssignment = /(?:^|[^\w-])["']?(?:api[_-]?key|(?:[a-z0-9]+_)*(?:secret|access_token|client_secret|service_role_key|token|password|passwd|database_url))["']?\s*[:=]\s*["']?([^\s"',}\]#]+)/gim;
const privateHost = /(?:https?|wss?|ssh|postgres(?:ql)?|mysql):\/\/(?:[^/\s]+@|(?:localhost|(?:[a-z0-9-]+\.)+(?:internal|local|lan|home\.arpa)|127(?:\.\d{1,3}){3}|10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2[0-9]|3[01])(?:\.\d{1,3}){2}|169\.254(?:\.\d{1,3}){2}|\[::1\])(?=[:/#?\s)'" ]|$))/i;
const privateGithubLinks = /https:\/\/(?:www\.)?github\.com\/iarketinglabs\/(?!skills-atomicas(?:[\/#?\s)]|$))/i;
const localPath = /(?:\b[A-Za-z]:[\\/]+(?:Users|Documents and Settings|Projetos-Atomica)(?:[\\/]|$)|\\\\(?:[^\\/\s]{2,})\\[^\\/\r\n]+|\/(?:home|Users|mnt\/[^/]+\/Users)\/[^/\s<>\])]+|file:\/\/)/i;
const email = /(?:mailto:)?\b[A-Z0-9.!#$%&'*+/=?^_{|}~-]+@([A-Z0-9.-]+\.[A-Z]{2,63})\b/gi;
const phone = /(?:\b(?:tel(?:efone)?|telem[oó]vel|whatsapp|phone|mobile)\b\s*[:=]\s*|\btel:|\bwa\.me\/|\+)(\+?\d[\d. ()-]{6,}\d)/gi;
const identity = /\b(?:cpf|cnpj|nif|tax[_ -]?id|passport|passaporte)\s*[:=]\s*["']?\d[\d.-]{7,}\d/iu;
const protectedFile = /(?:^|\/)(?:(?:\.env(?!\.(?:example|sample|template)(?:\/|$)))(?:[./]|$)|(?:id_(?:rsa|ed25519)|credentials?(?:\.(?:json|ya?ml|txt))|secrets?\.(?:json|ya?ml|txt))(?:\/|$))|(?:\.pem|\.pfx|\.p12|\.key|\.kdbx)$/i;

function scanText(text) {
  const findings = new Set();
  if (secretTokens.test(text) || Array.from(text.matchAll(secretAssignment)).some((match) => {
    const value = match[1];
    return value.length >= 12 && /\d/.test(value) && /[a-z]/i.test(value) && !/^(?:example|placeholder|dummy|fake|test|sample|your[_-])|(?:example|placeholder)|^\$|^<|^\*+$/i.test(value);
  })) findings.add('credential');
  if (localPath.test(text)) findings.add('local-path');
  if (privateHost.test(text)) findings.add('internal-url');
  if (privateGithubLinks.test(text)) findings.add('private-repository');
  if (Array.from(text.matchAll(email)).some((match) => !/(?:^|\.)(?:example\.(?:com|org|net)|example|localhost|users\.noreply\.github\.com)$/i.test(match[1]))) findings.add('personal-email');
  if (Array.from(text.matchAll(phone)).some((match) => {
    const digits = match[1].replace(/\D/g, '');
    return digits.length >= 9 && digits.length <= 15;
  })) findings.add('personal-phone');
  if (identity.test(text)) findings.add('personal-id');
  return [...findings].sort();
}

function walk(base, current = base) {
  const results = [];
  for (const entry of readdirSync(current, { withFileTypes: true })) {
    const full = join(current, entry.name);
    if (entry.isDirectory()) results.push(...walk(base, full));
    else if (entry.isFile()) results.push({ path: relative(base, full).split(sep).join('/'), bytes: readFileSync(full) });
    else throw new Error('Pacote contém entrada não regular.');
  }
  return results;
}

export function scanPackages(catalog, root = process.cwd()) {
  let failures = 0;
  let binaryFiles = 0;
  for (const skill of catalog.skills.filter((entry) => entry.origin.distribution === 'package')) {
    const base = join(root, 'public', 'skills', skill.id);
    for (const file of walk(base)) {
      const codes = new Set(scanText(file.path));
      if (protectedFile.test(file.path)) codes.add('sensitive-file-type');
      const content = file.bytes.toString('utf8');
      const isText = textFile.test(file.path) || /^(?:LICENSE|NOTICE)$/i.test(file.path.split('/').at(-1));
      if (isText && (content.includes('\0') || content.includes('\uFFFD'))) codes.add('invalid-text-encoding');
      for (const code of scanText(content)) codes.add(code);
      if (!isText) binaryFiles++;
      if (codes.size) {
        failures += codes.size;
        for (const code of codes) process.stderr.write(skill.id + '/' + file.path + ': ' + code + '\n');
      }
    }
  }
  if (failures) throw new Error('A varredura encontrou indicadores. Consulte apenas paths e códigos acima; valores detetados não são registados.');
  process.stdout.write('Privacidade validada: ' + catalog.skills.filter((entry) => entry.origin.distribution === 'package').length + ' pacotes; sem indicadores automáticos.\n');
  if (binaryFiles) process.stdout.write(binaryFiles + ' ficheiros binários dependem da revisão manual registada no fluxo privado.\n');
  return { binaryFiles };
}
