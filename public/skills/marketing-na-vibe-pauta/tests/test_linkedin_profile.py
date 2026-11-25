import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import scripts.linkedin_profile as linkedin_profile


class LinkedInProfilePrivacyTests(unittest.TestCase):
    def test_sanitizer_keeps_editorial_fields_and_removes_contact_data(self):
        result = linkedin_profile.sanitize(
            {
                "name": "Convidado Exemplo",
                "headline": "Pesquisador",
                "email": "guest" + "@" + "example.invalid",
                "phone": "+351 " + "912" + " 345 " + "678",
                "profileUrl": "https://www.linkedin.com/in/example",
                "experience": [{"title": "Diretor", "url": "https://example.invalid"}],
                "internal_id": "private-id",
            },
            top_level=True,
        )

        self.assertEqual(result["name"], "Convidado Exemplo")
        self.assertNotIn("email", result)
        self.assertNotIn("phone", result)
        self.assertNotIn("profileUrl", result)
        self.assertNotIn("internal_id", result)
        self.assertNotIn("url", result["experience"][0])

    def test_sanitizer_redacts_contact_strings_inside_editorial_text(self):
        result = linkedin_profile.sanitize(
            {"about": "Contacte " + "guest" + "@" + "example.invalid ou https://example.invalid"}
        )

        self.assertNotIn("guest" + "@" + "example.invalid", str(result))
        self.assertNotIn("https://example.invalid", str(result))
        self.assertIn("[e-mail removido]", result["about"])
        self.assertIn("[link removido]", result["about"])

    def test_load_profile_requires_a_local_json_object(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "profile.json"
            path.write_text(json.dumps({"name": "Convidado Exemplo"}), encoding="utf-8")
            self.assertEqual(linkedin_profile.load_profile(path)["name"], "Convidado Exemplo")

    def test_cli_requires_explicit_permission_confirmation(self):
        with patch("sys.argv", ["linkedin_profile.py", "--input", "profile.json"]), patch(
            "sys.stderr"
        ) as stderr:
            self.assertEqual(linkedin_profile.main(), 2)
            self.assertIn("autorização", "".join(str(call.args[0]) for call in stderr.write.call_args_list))

    def test_helper_contains_no_network_fetch_implementation(self):
        source = Path(linkedin_profile.__file__).read_text(encoding="utf-8")
        self.assertNotIn("urlopen", source)
        self.assertNotIn("requests.", source)
        self.assertNotIn("api.apify.com", source)


if __name__ == "__main__":
    unittest.main()
