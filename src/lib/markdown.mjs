import {posix as path} from 'node:path';
import {marked} from 'marked';
import sanitize from 'sanitize-html';

export const docId = path => 'doc-'+Buffer.from(path,'utf8').toString('base64url');

export function renderDocument(markdown,doc,docs,repositoryFilesUrl,files=[]) {
  const body=markdown.replace(/^\uFEFF?---\r?\n[\s\S]*?\r?\n---(?:\r?\n|$)/,'').replace(/^---\r?\n[\s\S]*?\r?\n---(?:\r?\n|$)/,'');
  const html=marked.parse(body,{async:false,gfm:true});
  return sanitize(html,{
    allowedTags:['p','br','hr','h1','h2','h3','h4','h5','h6','a','strong','b','em','i','del','blockquote','pre','code','ul','ol','li','table','thead','tbody','tr','th','td','details','summary','kbd'],
    allowedAttributes:{a:['href','rel'],ol:['start']},
    allowedSchemes:['https','http'],
    allowProtocolRelative:false,
    transformTags:{
      h1:'h3',h2:'h3',h3:'h4',
      a:(_tag,attrs)=>{
        const link=attrs.href?.trim() ?? '';
        const clean={};
        if (/^https?:\/\//i.test(link)) {clean.href=link;clean.rel='noopener noreferrer';}
        else if (/^(?![#/])[^:\\]+$/.test(link)) {
          try {
            const local=decodeURIComponent(link.split(/[?#]/)[0]);
            const normal=path.normalize(path.join(path.dirname(doc.path),local));
            if (docs.some(d=>d.path===normal)) clean.href='#'+docId(normal);
            else if (repositoryFilesUrl && files.some(file=>file.path===normal) && !normal.startsWith('../') && normal!=='.') clean.href=repositoryFilesUrl+'/'+normal.split('/').map(encodeURIComponent).join('/');
            else return {tagName:'span',attribs:{}};
          } catch { /* Malformed URL stays as plain text. */ }
        }
        return {tagName:'a',attribs:clean};
      }
    },
  });
}
