# inspect-spacy-model

A Python utility to inspect and analyze downloaded spaCy models, revealing their internal structure, components, and capabilities.

## 🚀 What This Does

This tool provides detailed insights into spaCy models after you download them, showing you:

- **📍 Model location** on your filesystem
- **📊 Model metadata** (version, description, size)
- **🔧 Pipeline components** (tokenizer, POS tagger, NER, etc.)
- **📚 Vocabulary statistics** (total tokens, word vectors)
- **🏷️ Available entity types** with explanations
- **📝 POS tags** and their meanings
- **🧪 Live model testing** with sample text
- **📁 Complete file structure** of the model directory
- **📄 Sample configuration files** content
- **💾 Storage information** and file sizes

## 📦 Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/inspect-spacy-model.git
   cd inspect-spacy-model
   ```

2. **Install dependencies:**
   ```bash
   pip install spacy
   ```

3. **Download a spaCy model** (if you haven't already):
   ```bash
   python -m spacy download en_core_web_sm
   ```

## 🎯 Usage

### Basic Usage

```bash
python inspect_spacy_model.py
```

This will inspect the default `en_core_web_sm` model.

### Example Output

```
✅ Model loaded successfully!

📍 Model Location:
   /Users/username/.local/lib/python3.13/site-packages/en_core_web_sm

📊 Model Metadata:
   Name: en_core_web_sm
   Version: 3.8.0
   Description: English pipeline optimized for CPU...
   Language: en
   Pipeline: ['tok2vec', 'tagger', 'parser', 'attribute_ruler', 'lemmatizer', 'ner']

🔧 Pipeline Components:
   - tok2vec: Tok2Vec
   - tagger: Tagger
   - parser: DependencyParser
   - attribute_ruler: AttributeRuler
   - lemmatizer: Lemmatizer
   - ner: EntityRecognizer

📚 Vocabulary:
   Total tokens: 514,157
   Vector dimensions: 96
   Vectors available: 20,000

🧪 Model Test:
   Input: Apple Inc. is looking at buying a startup in San Francisco for $1 billion.
   Entities: [('Apple Inc.', 'ORG'), ('San Francisco', 'GPE'), ('$1 billion', 'MONEY')]
```

## 📋 Available Models

This inspector works with any spaCy model. Common models include:

| Model | Size | Description |
|-------|------|-------------|
| `en_core_web_sm` | ~17MB | Small English model |
| `en_core_web_md` | ~50MB | Medium English model with word vectors |
| `en_core_web_lg` | ~750MB | Large English model with word vectors |
| `en_core_web_trf` | ~440MB | Transformer-based English model |

Download any model with:
```bash
python -m spacy download <model_name>
```

## 🔧 Customization

To inspect a different model, modify the model name in `inspect_spacy_model.py`:

```python
nlp = spacy.load("en_core_web_md")  # Change model name here
```

Or extend the script to accept command-line arguments:

```python
import sys
model_name = sys.argv[1] if len(sys.argv) > 1 else "en_core_web_sm"
nlp = spacy.load(model_name)
```

Then run:
```bash
python inspect_spacy_model.py en_core_web_lg
```

## 🤔 Why Use This?

- **🔍 Understanding**: See exactly what you downloaded and where it lives
- **🐛 Debugging**: Verify model installation and components
- **📊 Analysis**: Compare different models' capabilities
- **🎓 Learning**: Understand spaCy's internal structure
- **⚡ Quick Reference**: Get entity types and POS tags at a glance

## 🛠️ Requirements

- Python 3.7+
- spaCy 3.0+
- At least one downloaded spaCy model

## 📁 Project Structure

```
inspect-spacy-model/
├── inspect_spacy_model.py  # Main inspection script
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore patterns
└── LICENSE               # MIT License
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Add support for more model types
- Improve the output formatting
- Add command-line argument parsing
- Create additional analysis features

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [spaCy](https://spacy.io/) - Industrial-strength NLP library
- [Explosion AI](https://explosion.ai/) - Creators of spaCy

## 📞 Support

If you encounter any issues:

1. Ensure spaCy is installed: `pip install spacy`
2. Verify the model is downloaded: `python -m spacy download en_core_web_sm`
3. Check the model name matches exactly
4. Open an issue on this repository

---

Made with ❤️ for the spaCy community