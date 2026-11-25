# Revisão, execução local e publicação

## Uma fonte e versões coerentes

Mantenha uma entrada editável como fonte da versão atual. Após mover, unir ou inserir telas, atualize conteúdo, notas e roteiro na mesma ordem, recalcule contadores/progresso e gere o PDF novamente. Confirme o slide pelo título além do número. Elimine afirmações retiradas do escopo em todos os documentos atuais; preserve versões anteriores como histórico sem misturá-las à entrega.

Grave e leia texto com UTF-8 explícito. No Windows, prefira executar um script UTF-8 salvo a enviar código acentuado por pipelines com codificação incerta. Não corrija corrupção apenas na aparência do navegador.

## Servidor local

Identifique o processo e a pasta realmente servida antes de trocar arquivos ou porta. Vincule a 127.0.0.1 por padrão. Se o pedido nomeia uma URL local já usada, atualize-a ou explique claramente a nova URL; não entregue uma versão nova em outra porta como se a antiga tivesse sido atualizada.

Verifique HTTP 200 e compare o conteúdo servido com a versão pretendida; um status de sucesso não prova que o slide é o mais recente. Confirme HTML, CSS referenciado (incluindo query de cache), imagem alterada e PDF por SHA-256. Recarregue o navegador quando solicitado; cache pode manter uma apresentação antiga na tela.

## Pacote público

Somente publique quando solicitado. Prepare primeiro uma entrega revisável:

```powershell
python scripts/package.py caminho/deck caminho/pacote-publico
```

O script copia `index.html`, referências locais transitivas de HTML e CSS (incluindo `@import` e `url()` no CSS, `<source src>` de vídeo, posters e imagens responsivas), licenças das fontes e PDF se presente. Assim, só entram no pacote os vídeos usados nos slides. Exclui notas, fontes de trabalho, capturas, relatórios, versões anteriores e prompts não referenciados. Inclui manifesto SHA-256 e `.nojekyll`; rejeita notas estruturais em qualquer HTML coletado e dependências externas de renderização. Links de navegação externos são permitidos, sem baixar seu conteúdo.

Revise o pacote e faça a publicação pelo mecanismo disponível. Preserve mudanças não relacionadas na pasta de trabalho; use diretório ou checkout isolado para o artefato público. Não altere a visibilidade de um repositório com documentos internos para publicar um deck. Ausência de indexação não é controle de acesso; se proteção foi pedida, preserve-a e valide-a.

Ao atualizar um site existente, preserve caminho, `robots`/`noindex`, metadados e arquivos fora do escopo. Mude a query de cache do CSS quando alterar seu conteúdo mantendo o mesmo nome. Em Git, faça fetch, confirme branch e estado inicial, sincronize só os arquivos necessários, revise os caminhos preparados e proteja mudanças alheias. Com `core.autocrlf` ativo, valide o manifesto contra os blobs preparados (`git show :caminho`), não apenas contra bytes do diretório de trabalho; normalize finais de linha antes de gerar os hashes se o pacote for transformado.

Depois da publicação, espere Pages indicar `built` e a execução de deploy terminar com sucesso. Só então consulte a URL exata e compare HTML, CSS referenciado, imagem alterada, PDF e manifesto com os blobs do commit por SHA-256. HTTP 200, commit enviado ou etapa de build isolada não provam que o site atualizado está no ar. Se Pages falhar ou servir arquivos antigos, continue verificando ou informe claramente a pendência; não declare publicação concluída. O script não cria repositório, escolhe hospedagem nem fornece autenticação.
