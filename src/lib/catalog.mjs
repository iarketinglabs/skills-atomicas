import { existsSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import semver from 'semver';

const require = createRequire(import.meta.url);
export const iconFolder = join(dirname(require.resolve('lucide-static/package.json')), 'icons');
export const iconName = name => String(name).replace(/([a-z\d])([A-Z])/g, '$1-$2').toLowerCase();
export const fold = value => String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('pt');
export const skillMemberships = s => [{categoryId:s.categoryId,subcategoryId:s.subcategoryId},...(s.memberships ?? [])];
export const searchSkills = (skills, query) => skills.filter(s => fold([s.name,s.shortDescription,s.description,...skillMemberships(s).flatMap(m=>[m.categoryId,m.subcategoryId])].join(' ')).includes(fold(query).trim()));
export function treeFromFiles(files) {
  const root = [];
  for (const file of files) {
    let branch = root;
    const names = file.path.split('/');
    for (const [i, name] of names.entries()) {
      if (i === names.length-1) { branch.push({...file,name}); break; }
      let folder = branch.find(n => n.name === name && n.children);
      if (!folder) { folder={name,children:[]}; branch.push(folder); }
      branch=folder.children;
    }
  }
  function sort(nodes) {
    nodes.sort((a,b)=>Number(!!b.children)-Number(!!a.children) || a.name.localeCompare(b.name,'pt'));
    nodes.forEach(n=>{if(n.children) sort(n.children);});
  }
  sort(root);
  return root;
}

function check(condition, reason) { if (!condition) throw new Error(reason); }
const slug = s => typeof s === 'string' && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(s);
const nonempty = s => typeof s === 'string' && s.trim().length > 0;
const safePath = p => nonempty(p) && !/[\\:\x00-\x1f]/.test(p) && p.split('/').every(s => s && s !== '.' && s !== '..');
const iso = value => typeof value === 'string' && /^\d{4}-\d\d-\d\d(?:T\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d))?$/.test(value) && !Number.isNaN(Date.parse(value)) && new Date(value.slice(0,10)+'T00:00:00Z').toISOString().slice(0,10) === value.slice(0,10);
const repo = s => { try { const u = new URL(s); return u.protocol === 'https:' && !u.username && !u.password && !u.search && !u.hash && /^\/[^/]+\/[^/]+\/?$/.test(u.pathname); } catch { return false; } };

export function validateCatalog(data) {
  check(Array.isArray(data?.categories) && Array.isArray(data?.skills), 'O catálogo exige categorias e skills.');
  const areas = new Map(), skillIds = new Set(), installNames = new Set(), icons = new Set();
  function registerIcon(icon) {
    const name=iconName(icon);
    check(slug(name) && existsSync(join(iconFolder,name+'.svg')), 'Ícone Lucide desconhecido: '+name);
    check(!icons.has(name), 'Ícone repetido: '+name);
    icons.add(name);
  }
  for (const area of data.categories) {
    check(slug(area.id) && !areas.has(area.id) && nonempty(area.name) && nonempty(area.description), 'Categoria inválida.');
    registerIcon(area.icon);
    const subs = new Set();
    for (const sub of area.subcategories ?? []) {
      check(slug(sub.id) && !subs.has(sub.id) && nonempty(sub.name), 'Subcategoria inválida.');
      subs.add(sub.id);
    }
    areas.set(area.id,subs);
  }
  const sizes = new Map();
  for (const s of data.skills) for (const membership of skillMemberships(s)) sizes.set(membership.categoryId,(sizes.get(membership.categoryId) ?? 0)+1);
  for (const s of data.skills) {
    check(slug(s.id) && !skillIds.has(s.id) && nonempty(s.name), 'Identificador ou nome de skill inválido.');
    skillIds.add(s.id);
    registerIcon(s.icon);
    const memberships=skillMemberships(s);
    check(new Set(memberships.map(m=>m.categoryId)).size===memberships.length, 'Filiação de categoria repetida.');
    for (const membership of memberships) {
      const subs=areas.get(membership.categoryId);
      check(subs && nonempty(membership.subcategoryId) && subs.has(membership.subcategoryId), 'Categoria ou subcategoria inválida.');
      check(sizes.get(membership.categoryId) <= 20 || nonempty(membership.subcategoryId), 'Subcategoria obrigatória a partir da 21.ª skill.');
    }
    check(semver.valid(s.version), 'Versão SemVer inválida.');
    check(iso(s.createdAt) && iso(s.updatedAt) && Date.parse(s.createdAt)<=Date.parse(s.updatedAt), 'Datas da skill inválidas.');
    const origin=s.origin;
    check(origin && ['atomica','third-party'].includes(origin.kind) && ['package','reference-only'].includes(origin.distribution), 'Origem inválida.');
    check(origin.kind !== 'third-party' || repo(origin.repositoryUrl), 'Repositório original inválido.');
    check(!origin.repositoryUrl || repo(origin.repositoryUrl), 'URL de repositório inválida.');
    check(origin.kind !== 'third-party' || origin.distribution !== 'package' || nonempty(origin.permissionEvidence), 'Evidência de redistribuição ausente.');
    check(Array.isArray(s.files) && Array.isArray(s.documents), 'Manifesto de ficheiros/documentos inválido.');
    if (origin.distribution === 'reference-only') {
      check(!s.installName, 'Referência externa não tem nome de instalação.');
      check(origin.kind==='third-party' && !s.files.length && !s.documents.length && !s.description && !s.shortDescription, 'Referência neutra exige apenas identificação e ligação à origem.');
      continue;
    }
    check(nonempty(s.installName) && slug(s.installName) && !installNames.has(s.installName), 'Nome de instalação inválido ou repetido.');
    installNames.add(s.installName);
    check(nonempty(origin.license) && nonempty(s.description) && nonempty(s.shortDescription), 'Descrição ou licença ausente.');
    const paths = new Set();
    for (const f of s.files) {
      check(safePath(f.path) && !paths.has(f.path) && iso(f.updatedAt), 'Caminho ou data de ficheiro inválido.');
      paths.add(f.path);
    }
    check(paths.has('SKILL.md'), 'O pacote exige SKILL.md.');
    const docs = new Set();
    for (const doc of s.documents) {
      check(paths.has(doc.path) && !docs.has(doc.path) && nonempty(doc.title) && typeof doc.content==='string', 'Documento inválido.');
      docs.add(doc.path);
    }
  }
  return data;
}
