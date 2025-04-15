from django.test import TestCase
from .utils import generate_title_suggestions

class TitleGenerationTests(TestCase):
    def test_generate_title_suggestions(self):
        """Test that the title suggestion function returns a list of titles."""
        content = "This is a test blog post about Django programming."
        suggestions = generate_title_suggestions(content)
        
        # Check that we get a list
        self.assertIsInstance(suggestions, list)
        
        # Check that we have at least one suggestion
        self.assertGreater(len(suggestions), 0)