from langdetect import detect
from googletrans import Translator
import pandas as pd

class ArxivExpertChatbot:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.translator = Translator()  # Initialize translator

    def detect_language(self, text):
        """Detect the language of the input."""
        return detect(text)

    def translate(self, text, target_lang='en'):
        """Translate text to the target language."""
        return self.translator.translate(text, dest=target_lang).text

    def search_paper(self, query):
        """Search for papers related to the query."""
        results = self.data[self.data['title'].str.contains(query, case=False)]
        if results.empty:
            return "No papers found for your query."
        else:
            titles = results['title'].head(3).tolist()
            return "Top papers:\n" + "\n".join(titles)

    def handle_query(self, query):
        """Process the query, including language detection and translation."""
        query_lang = self.detect_language(query)

        # Translate the query to English if needed
        if query_lang != 'en':
            query = self.translate(query, target_lang='en')

        # Search for papers
        response = self.search_paper(query)

        # Translate the response back to the original language
        if query_lang != 'en':
            response = self.translate(response, target_lang=query_lang)

        return response
