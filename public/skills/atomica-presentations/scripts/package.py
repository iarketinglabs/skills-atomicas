"""Prepare a minimal offline public deck; never deploy or copy presenter files."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit


def package(source, dest):
    source = Path(source).resolve()
    dest = Path(dest).resolve()
    if dest.exists() or dest.is_relative_to(source) or source.is_relative_to(dest):
        raise ValueError('Escolha um destino novo fora da pasta de origem')
    selected = {'index.html'}
    queue = ['index.html']
    while queue:
        relative = queue.pop()
        file = source / relative
        if not file.is_file():
            raise ValueError('Recurso ausente: ' + relative)
        text = file.read_text(encoding='utf-8')
        if relative == 'index.html' and re.search(r'id=[\"\'](?:notes-data|presenter)[\"\']', text):
            raise ValueError('HTML contém notas privadas')
        if relative.endswith('.html'):
            refs = re.findall(r'(?:src|href|poster)=[\"\']([^\"\']+)[\"\']', text)
            # External navigation is permitted; external rendering assets are not.
            rendering = re.findall(r'<(?:script|img|link|video|audio|source)\b[^>]*(?:src|href|poster)=[\"\']([^\"\']+)', text, re.I)
            if any(urlsplit(ref).scheme in {'http', 'https'} or ref.startswith('//') for ref in rendering):
                raise ValueError('Dependência externa de renderização')
        else:
            refs = re.findall(r'url\([\"\']?([^\)\"\']+)', text)
            if any(urlsplit(ref).scheme in {'http', 'https'} or ref.startswith('//') for ref in refs):
                raise ValueError('Dependência externa de CSS')
        for ref in refs:
            parsed = urlsplit(ref)
            if parsed.scheme or ref.startswith(('#', '//')):
                continue
            path = (file.parent / unquote(parsed.path)).resolve()
            if not path.is_relative_to(source):
                raise ValueError('Recurso fora da origem')
            name = path.relative_to(source).as_posix()
            if name == 'presenter.html' or name.startswith(('qa/', 'previous-', 'before-')) or path.suffix.lower() in {'.md', '.json', '.py'}:
                raise ValueError('Referência a arquivo privado ou de trabalho: ' + name)
            if not path.is_file():
                raise ValueError('Recurso ausente: ' + name)
            if name not in selected:
                selected.add(name)
                if path.suffix in {'.html', '.css'}:
                    queue.append(name)
    if (source/'presentation.pdf').is_file():
        selected.add('presentation.pdf')
    selected.update(p.relative_to(source).as_posix() for p in (source/'assets/licenses').glob('*') if p.is_file())
    dest.mkdir(parents=True)
    for name in sorted(selected):
        (dest/name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source/name, dest/name)
    (dest/'.nojekyll').write_bytes(b'')
    hashes = {p.relative_to(dest).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in dest.rglob('*') if p.is_file()}
    (dest/'manifest.sha256.json').write_text(json.dumps(hashes, indent=2), encoding='utf-8')
    return hashes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('dest', type=Path)
    args = parser.parse_args()
    try:
        files = package(args.source, args.dest)
        print(f'OK: {len(files)} arquivos públicos; manifesto incluído. Nenhuma publicação remota executada.')
    except (ValueError, OSError) as error:
        parser.exit(1, f'Erro: {error}\n')
