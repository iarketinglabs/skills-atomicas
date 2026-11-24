import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

function canonical(value) {
  if (Array.isArray(value)) return value.map(canonical);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).filter((key) => value[key] !== undefined).sort().map((key) => [key, canonical(value[key])]));
  }
  return value;
}

function releaseMetadata(skill) {
  const { id, name, installName, shortDescription, description, icon, version, categoryId, subcategoryId, memberships, createdAt, updatedAt } = skill;
  const { kind, repositoryUrl, license, distribution, permissionEvidence } = skill.origin;
  return {
    id, name, installName, shortDescription, description, icon, version, categoryId, subcategoryId,
    ...(memberships?.length ? { memberships } : {}), createdAt, updatedAt,
    origin: { kind, ...(repositoryUrl ? { repositoryUrl } : {}), license, distribution, ...(permissionEvidence ? { permissionEvidence } : {}) },
  };
}

function fileDigests(skill, root) {
  if (skill.origin.distribution === 'reference-only') return [];
  const base = join(root, 'public', 'skills', skill.id);
  return skill.files.map(({ path }) => ({
    path,
    sha256: createHash('sha256').update(readFileSync(join(base, ...path.split('/')))).digest('hex'),
  }));
}

export function verifyReleaseProofs(catalog, root = process.cwd()) {
  for (const skill of catalog.skills) {
    const proof = skill.releaseProof;
    if (!proof || !['initial-audit', 'github-comment'].includes(proof.method) || !/^[a-f0-9]{40}$/.test(proof.sourceCommit ?? '') || !/^[a-f0-9]{64}$/.test(proof.digest ?? '')) {
      throw new Error('Prova de revisão de release ausente ou inválida: ' + skill.id);
    }
    const category = catalog.categories.find((entry) => entry.id === skill.categoryId);
    const files = fileDigests(skill, root).sort((left, right) => left.path < right.path ? -1 : (left.path > right.path ? 1 : 0));
    const payload = canonical({
      schema: 1,
      category,
      release: releaseMetadata(skill),
      files,
      sourceCommit: proof.sourceCommit,
    });
    const digest = createHash('sha256').update(JSON.stringify(payload)).digest('hex');
    if (digest !== proof.digest) throw new Error('Conteúdo ou metadados alterados após a revisão: ' + skill.id);
  }
}
