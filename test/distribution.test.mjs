import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,mkdirSync,writeFileSync,readFileSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {unzipSync} from 'fflate';
import {validatePackages,writeDownloads} from '../scripts/packages.mjs';
import {renderDocument} from '../src/lib/markdown.mjs';

test('ZIP contém exatamente os ficheiros listados e bloqueia extras',t=>{
 const root=mkdtempSync(join(tmpdir(),'portal-zip-'));
 t.after(()=>rmSync(root,{recursive:true,force:true}));
 const pkg=join(root,'public/skills/example');
 mkdirSync(pkg,{recursive:true});
 const markdown='---\nname: example\ndescription: Skill demonstrativa\n---\n# Exemplo';
 writeFileSync(join(pkg,'SKILL.md'),markdown);
 writeFileSync(join(pkg,'LICENSE.md'),'CC BY 4.0');
 const s={id:'example',version:'1.0.0',origin:{distribution:'package',kind:'atomica'},files:['SKILL.md','LICENSE.md'].map(path=>({path,updatedAt:'2026-11-24'})),documents:[{path:'SKILL.md',title:'Guia',content:markdown}]};
 const data={skills:[s]};
 assert.doesNotThrow(()=>validatePackages(data,root));
 writeDownloads(data,root);
 const files=unzipSync(readFileSync(join(root,'dist/downloads/example-1.0.0.zip')));
 assert.deepEqual(Object.keys(files).sort(),['example/LICENSE.md','example/SKILL.md']);
 writeFileSync(join(pkg,'outro.md'),'extra');
 assert.throws(()=>validatePackages(data,root),/manifesto/i);
});
test('a documentação remove código ativo e resolve referências entre documentos',()=>{
 const docs=[{path:'SKILL.md'},{path:'references/guia.md'}];
 const html=renderDocument('<script>alert(1)</script>\n\n[Guia](references/guia.md) ![imagem](https://tracker.example/img)',docs[0],docs);
 assert.ok(!html.includes('<script') && !html.includes('tracker.example'));
 assert.match(html,/href="#doc-/);
});
