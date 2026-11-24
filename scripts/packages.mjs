import {existsSync,lstatSync,mkdirSync,readFileSync,readdirSync,writeFileSync} from 'node:fs';
import {join,relative,sep} from 'node:path';
import {zipSync} from 'fflate';

function inventory(base,dir=base) {
  const files=[];
  for (const entry of readdirSync(dir,{withFileTypes:true})) {
    const current=join(dir,entry.name);
    if (entry.isDirectory()) files.push(...inventory(base,current));
    else if (entry.isFile()) files.push(relative(base,current).split(sep).join('/'));
    else throw new Error('O pacote contém um link ou uma entrada não regular.');
  }
  return files;
}
export function validatePackages({skills},root=process.cwd()) {
  const base=join(root,'public','skills');
  const packages=skills.filter(s=>s.origin.distribution==='package');
  const ids=new Set(packages.map(s=>s.id));
  for (const entry of existsSync(base) ? readdirSync(base,{withFileTypes:true}) : []) {
    if (!entry.isDirectory() || !ids.has(entry.name)) throw new Error('Pasta fora do catálogo de distribuição.');
  }
  for (const s of packages) {
    const dir=join(base,s.id);
    if (!existsSync(dir) || !lstatSync(dir).isDirectory()) throw new Error('Pacote em falta: '+s.id);
    const actual=inventory(dir).sort();
    const official=s.files.map(f=>f.path).sort();
    if (JSON.stringify(actual)!==JSON.stringify(official)) throw new Error('Ficheiros diferentes do manifesto de '+s.id);
    if (!actual.some(f=>/^(license|licence|copying)(\..*)?$/i.test(f))) throw new Error('Licença ausente no pacote '+s.id);
    for (const doc of s.documents) {
      if (readFileSync(join(dir,doc.path),'utf8').replace(/^\uFEFF/,'').replace(/\r\n/g,'\n') !== doc.content.replace(/^\uFEFF/,'').replace(/\r\n/g,'\n')) throw new Error('Documento diferente da versão do pacote: '+s.id);
    }
  }
}
export function writeDownloads(catalog,root=process.cwd()) {
  validatePackages(catalog,root);
  const out=join(root,'dist','downloads');
  mkdirSync(out,{recursive:true});
  for (const skill of catalog.skills.filter(s=>s.origin.distribution==='package')) {
    const data=Object.create(null);
    for (const file of skill.files) {
      const name=skill.id+'/'+file.path;
      data[name]=[readFileSync(join(root,'public','skills',skill.id,file.path)),{mtime:new Date('2000-01-01T00:00:00Z')}];
    }
    writeFileSync(join(out,skill.id+'-'+skill.version+'.zip'),zipSync(data,{level:6}));
  }
}
