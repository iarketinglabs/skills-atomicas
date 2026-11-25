import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().with_name("validate_kb_markdown.py")


class ExtractorValidation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def add(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode("utf-8") if isinstance(content, str) else content)
        return path

    def cli(self, path, *args):
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(SCRIPT), str(path), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def test_valid_short_guide_with_markdown_in_code_and_technical_marker(self):
        path = self.add("tema.md", "# Reprocessamento\n\nAntes de retomar, confirme se o cursor foi salvo. O campo conversation_id pertence apenas ao transporte.\n\n~~~md\n# Título como exemplo\n## Resposta\n~~~\n")
        result = self.cli(path)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("VALID=1", result.stdout)

    def test_count_on_nested_directory_and_missing_item(self):
        self.add("tema.md", "# Título\n\nGuia completo para este caso curto.\n")
        self.add("eixo/subtema.md", "# Subtema\n\nReferência verificada.\n")
        self.assertEqual(self.cli(self.root, "--expected-count", "2").returncode, 0)
        result = self.cli(self.root, "--expected-count", "3")
        self.assertEqual(result.returncode, 1, result.stderr + result.stdout)
        self.assertIn("EXPECTED=3", result.stdout)

    def test_corrupt_files_fail_independently(self):
        self.add("broken.md", b"# Titulo\n\n\xff")
        self.add("empty.md", "")
        self.add("duplicate.md", "# Um\n\n# Dois\n\nCorpo\n")
        self.add("wrapped.md", '# Titulo\n\n{"conversation_id":"fake","answer":"x"}\n')
        self.add("unbalanced.md", "# Titulo\n\n~~~md\nParte sem fechamento\n")
        result = self.cli(self.root)
        self.assertEqual(result.returncode, 1, result.stderr + result.stdout)
        self.assertIn("INVALID=5", result.stdout)

    def test_substantive_api_guide_headings_are_advisory(self):
        path = self.add("api.md", "# Guia da API\n\n## Consulta\n\nEnvie o filtro por data. Omita datas futuras.\n\n## Resposta\n\nConfira o campo de paginação no resultado.\n")
        result = self.cli(path)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("VALID=1", result.stdout)
        self.assertIn("REVIEW api.md:", result.stdout)

    def test_transport_json_rejected_but_fenced_json_example_preserved(self):
        payload = '{"conversation_id":"ficticio","answer":"guia"}'
        wrapped = self.add("transporte.md", f"# Título\n\n{payload}\n")
        result = self.cli(wrapped)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("objeto JSON de transporte", result.stdout)

        example = self.add("exemplo.md", f"# Exemplo de API\n\n~~~json\n{payload}\n~~~\n")
        self.assertEqual(self.cli(example).returncode, 0)

    def test_atx_profile_rejects_second_setext_title_and_empty_title(self):
        titles = {
            "setext.md": "# Primeiro título\n\nSegundo título\n==============\n\nCorpo do guia.\n",
            "atx-vazio.md": "# #\n\nCorpo do guia.\n",
            "atx-sem-texto.md": "#\n\nCorpo do guia.\n",
        }
        for name, content in titles.items():
            with self.subTest(name=name):
                result = self.cli(self.add(name, content))
                self.assertEqual(result.returncode, 1, result.stderr + result.stdout)

        valid = self.add("valido.md", "# Função #\n\n~~~text\nSegundo título\n==============\n~~~\n")
        self.assertEqual(self.cli(valid).returncode, 0)

    def test_empty_fenced_block_does_not_supply_body_content(self):
        empty = self.add("cerca-vazia.md", "# Título\n\n## Seção\n\n~~~text\n\n~~~\n")
        result = self.cli(empty)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("corpo vazio", result.stdout)
    def test_empty_and_missing_paths_fail(self):
        self.assertEqual(self.cli(self.root).returncode, 1)
        self.assertEqual(self.cli(self.root / "missing").returncode, 1)

    def test_does_not_mutate_source_or_normalize_code(self):
        original = b"# Exemplo\r\n\r\n```python\r\nprint('exemplo')  \r\n```\r\n"
        path = self.add("unchanged.md", original)
        self.assertEqual(self.cli(path).returncode, 0)
        self.assertEqual(path.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
