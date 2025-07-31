class GoogleTranslate:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://translation.googleapis.com/language/translate/v2"

    def translate_text(self, text, source_lang, target_lang):
        import requests

        params = {
            'q': text,
            'source': source_lang,
            'target': target_lang,
            'format': 'text',
            'key': self.api_key
        }

        response = requests.post(self.url, params=params)
        if response.status_code == 200:
            return response.json()['data']['translations'][0]['translatedText']
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")