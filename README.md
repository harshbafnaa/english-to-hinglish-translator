# Hindi to Hinglish Translator

This is a simple web application built with Streamlit that translates English sentences to Hinglish (a mixture of Hindi and English). 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Translation Dictionary](#translation-dictionary)
- [Contributing](#contributing)
- [Credits](#credits).

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

3. Click the "Ctrl + Enter" button.

4. The translated and replaced sentences in Hindi will be displayed below the text area.

## Translation Dictionary

The translation of Hinglish words to English is defined in the `hinglish_to_english.json` file. You can modify this dictionary to add or update translations as needed.

The format of the dictionary is as follows:

```json

hinglish_to_english = {
    "डेफिनेटली": "Definitely",
    "शेयर": "share",
    "फ़ीडबैक": "feedback",
    "सेक्शन" : "section",
    "कमेंट": "comment",
    "बिग": "big",
    "वीडियो": "video",
    "मेंशन": "mention",
    "आल": "all",
    "प्रोडक्ट्स": "products",
    "वेटिंग": "waiting",
    "बैग": "bag",
    "आयरन": "iron",
    "बार": "bar",
    "केक": "cake",
    "चॉकलेट": "chocolate",
    "चॉक": "chalk",
    "डॉक्टर": "doctor",
    "डाक": "dock",
    "डेटा": "data",
    "फैक्टरी": "factory",
    "फाइल": "file",
    "फिल्म": "film",
    "फोटो": "photo",
    "गास": "gas",
    "गोल्फ": "golf",
    "हैंडबैग": "handbag",
    "हैलिकॉप्टर": "helicopter",
    "हिल्स": "hills",
    "इलेक्ट्रिक": "electric",
    "इलेवेटर": "elevator",
    "इंजीन": "engine",
    "इंटरनेट": "internet",
    "इंटरव्यू": "interview",
    "जेल": "jail",
    "जॉब": "job",
    "जूस": "juice",
    "जूलरी": "jewelry",
    "जज": "judge",
    "लाइब्रेरी": "library",
    "लाइट": "light",
    "मैनेजर": "manager",
    "मैप": "map",
    "मार्केट": "market",
    "मीटर": "meter",
    "मोटर": "motor",
    "मशीन": "machine",
    "नेवी": "navy",
    "नोट": "note",
    "पार्क": "park",
    "पासवर्ड": "password",
    "पेपर": "paper",
    "पार्टी": "party",
    "पासपोर्ट": "passport",
    "पर्फ्यूम": "perfume",
    "पिल्स": "pills",
    "प्लेटफार्म": "platform",
    "प्लेन": "plane",
    "पॉकेट": "pocket",
    "पोलिस": "police",
    "पॉलिटिक्स": "politics",
    "पॉस्ट": "post",
    "कंप्यूटर": "computer",
    "टेलीफ़ोन": "telephone",
    "कैमरा": "camera",
    "माइक्रोवेव": "microwave",
    "टेलीविजन": "television",
    "रेस्टोरेंट": "restaurant",
    "संगीत": "music",
    "किताब": "book",
    "मोबाइल": "mobile",
    "रेडियो": "radio",
    "बस": "bus",
    "ट्रेन": "train",
    "हवाई अड्डा": "airport",
    "कार": "car",
    "साइकिल": "bicycle",
    "आइस क्रीम": "ice cream",
    "पिज़्ज़ा": "pizza",
    "कॉफ़ी": "coffee",
    "चाय": "tea",
    "समाचार पत्रिका": "newspaper",
    "मैगज़ीन": "magazine",
    "रेडियो": "radio",
    "नर्स": "nurse",
    "दवा": "medicine",
    "अस्पताल": "hospital",
    "पुलिस स्थानक": "police station",
    "फायर स्टेशन": "fire station",
    "बैंक": "bank",
    "पैसे": "money",
    "क्रेडिट कार्ड": "credit card",
    "पासपोर्ट": "passport",
    "टिकट": "ticket",
    "होटल": "hotel",
    "मेनू": "menu",
    "सुबह का नाश्ता": "breakfast",
    "दोपहर का भोजन": "lunch",
    "रात का खाना": "dinner",
    "पानी": "water",
    "रस": "juice",
    "बीयर": "beer",
    "शराब": "wine",
    "चीज़": "cheese",
    "मुर्ग़ा": "chicken",
    "सब्जियाँ": "vegetables",
    "फल": "fruit",
    "रोटी": "bread",
    "मक्खन": "butter",
    "चाकू": "knife",
    "कांटा": "fork",
    "चम्मच": "spoon",
    "प्लेट": "plate",
    "गिलास": "glass",
    "कप": "cup",
    "मिनट": "minute",
    "डेमो": "demo",
    "हेडसेट": "headset"
}
```

## Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, feel free to open an issue or create a pull request.


## Credits

This project was created by [Harsh Bafna](https://github.com/harshbafnaa).
