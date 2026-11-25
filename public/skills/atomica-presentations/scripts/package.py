"""Prepare a minimal offline public deck; never deploy or copy presenter files."""
import argparse
import hashlib
import json
import re
import shutil
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


HTML_EXTENSIONS = {'.html', '.htm'}
URL_ATTRIBUTES = {
    'src', 'href', 'poster', 'background', 'cite', 'longdesc', 'manifest',
    'action', 'formaction', 'xlink:href', 'usemap',
}


CSS_REFERENCES = re.compile(
    r"""
       /\* .*? \*/
     | @import (?:\s|/\* .*? \*/)* (?:"([^"]+)"|'([^']+)')
     | (?<![\w-]) url\( \s* (?:"([^"]+)"|'([^']+)'|([^()'"\s]+)) \s* \)
     | "(?:\\.|[^"\\])*"
     | '(?:\\.|[^'\\])*'
    """,
    re.IGNORECASE | re.DOTALL | re.VERBOSE,
)


def css_urls(text):
    # Match dependencies alongside comments and strings so literal examples are ignored.
    for match in CSS_REFERENCES.finditer(text):
        reference = next((value for value in match.groups() if value is not None), None)
        if reference is not None:
            yield reference


def source_set_urls(value):
    # A URL token ends at whitespace. Commas inside URLs (such as data URLs)
    # belong to that token; trailing commas and commas after descriptors separate candidates.
    remaining = value
    while remaining := re.sub(r'^[,\s]+', '', remaining):
        parts = remaining.split(maxsplit=1)
        url = parts[0]
        yield url.rstrip(',')
        remaining = parts[1] if len(parts) == 2 else ''
        if not url.endswith(','):
            remaining = remaining.partition(',')[2]


class HtmlDependencies(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        if tag == 'base' and any(name == 'href' for name, _ in attrs):
            raise ValueError('Base HTML impede verificar caminhos locais')
        for name, value in attrs:
            if name == 'id' and value in {'notes-data', 'presenter'}:
                raise ValueError('HTML contém notas privadas')
            if not value:
                continue
            if name in URL_ATTRIBUTES or (tag == 'object' and name == 'data'):
                navigation = tag in {'a', 'area'} and name == 'href'
                self.references.append((value.strip(), navigation))
            elif name in {'srcset', 'imagesrcset'}:
                self.references.extend((url, False) for url in source_set_urls(value))
            elif name == 'ping':
                self.references.extend((url, False) for url in value.split())
            elif name == 'style':
                self.references.extend((url, False) for url in css_urls(value))
            elif name == 'srcdoc':
                self.references.extend(html_dependencies(value))
        if tag == 'style':
            self.in_style = True

    def handle_endtag(self, tag):
        if tag == 'style':
            self.in_style = False

    def handle_data(self, text):
        if self.in_style:
            self.references.extend((url, False) for url in css_urls(text))


def html_dependencies(text):
    parser = HtmlDependencies()
    parser.feed(text)
    parser.close()
    return parser.references


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
        suffix = file.suffix.lower()
        if suffix in HTML_EXTENSIONS:
            refs = html_dependencies(text)
            own_file_type = 'renderização'
        else:
            refs = [(url, False) for url in css_urls(text)]
            own_file_type = 'CSS'
        for ref, navigation in refs:
            parsed = urlsplit(ref)
            if not ref or ref.startswith('#') or parsed.scheme == 'data':
                continue
            if parsed.scheme or parsed.netloc or ref.startswith(('/', '\\')):
                if navigation and (parsed.scheme in {'http', 'https', 'mailto', 'tel'} or parsed.netloc):
                    continue
                raise ValueError('Dependência externa de ' + own_file_type)
            if not parsed.path:
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
                if path.suffix.lower() in HTML_EXTENSIONS | {'.css'}:
                    queue.append(name)
    if (source/'presentation.pdf').is_file():
        selected.add('presentation.pdf')
    selected.update(p.relative_to(source).as_posix() for p in (source/'assets/licenses').glob('*.txt') if p.is_file())
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
