# Language Translation Tool

This project is a language translation tool that utilizes the Google Translation API to translate text between different languages. It features a user-friendly interface that allows users to input text, select source and target languages, and view the translated output. Additionally, the tool includes a text-to-speech feature and a copy button for enhanced usability.

## Project Structure

```
language-translation-tool
├── src
│   ├── app.py                # Main entry point of the application
│   ├── translation
│   │   └── google_translate.py # Handles interactions with the Google Translation API
│   ├── tts
│   │   └── text_to_speech.py  # Manages text-to-speech functionality
│   ├── static
│   │   └── style.css          # CSS styles for the web application
│   └── templates
│       └── index.html         # HTML template for the web application
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd language-translation-tool
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Set up Google Translation API:**
   - Create a project in the Google Cloud Console.
   - Enable the Google Translation API.
   - Create credentials (API key) and set it in your environment variables or directly in the code.

4. **Run the application:**
   ```
   python src/app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage Guidelines

- Enter the text you want to translate in the input field.
- Select the source language from the dropdown menu.
- Choose the target language for translation.
- Click the "Translate" button to see the translated text.
- Use the "Copy" button to copy the translated text to your clipboard.
- Click the "Speak" button to hear the translated text spoken aloud.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.