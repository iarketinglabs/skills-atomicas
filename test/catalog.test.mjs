import test from 'node:test';
import assert from 'node:assert/strict';
import { validateCatalog, searchSkills, treeFromFiles } from '../src/lib/catalog.mjs';

const categories = [{id:'ti', name:'TI', description:'Tecnologia', icon:'cpu', subcategories:[{id:'dados',name:'Dados'}]}];
const sample = {
  id:'amostra', name:'Documentação técnica', installName:'documentacao-tecnica', shortDescription:'Organiza referências.', description:'Documenta decisões.',
  icon:'book-open',version:'1.0.0',categoryId:'ti',subcategoryId:'dados',createdAt:'2026-11-01',updatedAt:'2026-11-23',
  origin:{kind:'atomica',license:'CC-BY-4.0',distribution:'package'},
  releaseProof:{method:'initial-audit',sourceCommit:'a'.repeat(40),digest:'b'.repeat(64)},
  files:[{path:'SKILL.md',updatedAt:'2026-11-01'}, {path:'references/guia.md',updatedAt:'2026-11-23'}],
  documents:[{path:'SKILL.md',title:'Documentação',content:'## Começar'}]
};

test('aceita o catálogo vazio e uma versão aprovada',()=>{
  assert.doesNotThrow(()=>validateCatalog({categories,skills:[]}));
  assert.doesNotThrow(()=>validateCatalog({categories,skills:[sample]}));
});
test('exige ícones distintos e subcategorias nas filiações',()=>{
  const icons=['atom','audio-lines','award','badge','banknote','bell','bike','book','box','brain','brush','bug','cake','camera','car','cat','chart-bar','check','circle','clock','cloud'];
  const skills=icons.map((icon,i)=>({...sample,id:'skill-'+i,icon}));
  assert.doesNotThrow(()=>validateCatalog({categories,skills:skills.slice(0,20)}));
  assert.doesNotThrow(()=>validateCatalog({categories,skills}));
  assert.throws(()=>validateCatalog({categories,skills:skills.map((s,i)=>i===20?({...s,subcategoryId:undefined}):s)}),/subcategoria/i);
  assert.throws(()=>validateCatalog({categories,skills:[sample,{...sample,id:'outra'}]}),/ícone/i);
});
test('bloqueia pacotes e cópia de conteúdo numa referência externa',()=>{
  const ref={...sample,installName:undefined,origin:{kind:'third-party',distribution:'reference-only',repositoryUrl:'https://github.com/example/project',license:''}};
  assert.throws(()=>validateCatalog({categories,skills:[ref]}),/referência/i);
  assert.doesNotThrow(()=>validateCatalog({categories,skills:[{...ref,files:[],documents:[],description:'',shortDescription:''}]}));
});
test('rejeita caminhos externos, datas inválidas e URLs inseguras',()=>{
  assert.throws(()=>validateCatalog({categories,skills:[{...sample,files:[{path:'../fora',updatedAt:'2026-11-23'}]}]}));
  assert.throws(()=>validateCatalog({categories,skills:[{...sample,createdAt:'ontem'}]}));
  assert.throws(()=>validateCatalog({categories,skills:[{...sample,origin:{...sample.origin,kind:'third-party',repositoryUrl:'javascript:alert(1)'}}]}));
});
test('pesquisa sem acentos e mantém datas na árvore',()=>{
  assert.equal(searchSkills([sample], 'documentacao')[0].id,'amostra');
  assert.equal(searchSkills([sample], 'inexistente').length,0);
  assert.equal(treeFromFiles(sample.files).find(x=>x.name==='references').children[0].updatedAt,'2026-11-23');
});
