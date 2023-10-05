# Hinglish to Hindi Translator

This is a simple web application built with Streamlit that translates Hinglish (a mixture of Hindi and English) sentences to Hindi. It also replaces Hinglish words with their English equivalents.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Translation Dictionary](#translation-dictionary)
- [Contributing](#contributing)

## Installation

Before running the application, you'll need to install the required libraries. You can do this using pip:

```bash
pip install streamlit translate
```

After installing the libraries, you can run the app with the following command:

```bash
streamlit run app.py
```

## Usage

1. When you run the Streamlit app, you'll see a text area where you can enter multiple sentences in English (one per line).

2. Enter the sentences you want to translate and replace Hinglish words in.

3. Click the "Translate" button.

4. The translated and replaced sentences in Hindi will be displayed below the text area.

## Translation Dictionary

The translation of Hinglish words to English is defined in the `hinglish_to_english.json` file. You can modify this dictionary to add or update translations as needed.

The format of the dictionary is as follows:

```json
{
   "डेफिनेटली": "Definitely",
   "शेयर": "share",
   ...
   "हेडसेट": "headset"
}
```

## Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, feel free to open an issue or create a pull request.
