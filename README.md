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

### Option 1: Using Virtual Environment (Recommended)

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/inspect-spacy-model.git
   cd inspect-spacy-model
   ```

2. **Create and activate a virtual environment:**
   
   **Using venv (Python 3.3+):**
   ```bash
   # Create virtual environment
   python -m venv spacy-env
   
   # Activate it
   # On macOS/Linux:
   source spacy-env/bin/activate
   # On Windows:
   spacy-env\Scripts\activate
   ```
   
   **Using conda:**
   ```bash
   # Create virtual environment
   conda create -n spacy-env python=3.11
   
   # Activate it
   conda activate spacy-env
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download a spaCy model:**
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **When you're done, deactivate the environment:**
   ```bash
   # For venv:
   deactivate
   
   # For conda:
   conda deactivate
   ```

### Option 2: System-wide Installation

⚠️ **Note:** This installs spaCy globally on your system. We recommend using a virtual environment instead.

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/inspect-spacy-model.git
   cd inspect-spacy-model
   ```

2. **Install dependencies:**
   ```bash
   pip install spacy
   ```

3. **Download a spaCy model:**
   ```bash
   python -m spacy download en_core_web_sm
   ```

## 🎯 Usage

### Basic Usage

**Make sure your virtual environment is activated first:**
```bash
# Activate your environment
source spacy-env/bin/activate  # macOS/Linux
# or
spacy-env\Scripts\activate     # Windows
```

**Then run the inspector:**
```bash
python inspect_spacy_model.py
```

This will inspect the default `en_core_web_sm` model.

### Advanced Usage

```bash
# List all installed models
python inspect_spacy_model.py --list

# Inspect a specific model
python inspect_spacy_model.py en_core_web_md

# Get detailed information
python inspect_spacy_model.py en_core_web_lg --verbose

# Get help
python inspect_spacy_model.py --help
```

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

## 🧪 Quick Start Example

Here's a complete example from start to finish:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/inspect-spacy-model.git
cd inspect-spacy-model

# 2. Create virtual environment
python -m venv spacy-env

# 3. Activate it
source spacy-env/bin/activate  # macOS/Linux
# or spacy-env\Scripts\activate  # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download a model
python -m spacy download en_core_web_sm

# 6. Run the inspector
python inspect_spacy_model.py

# 7. Try different options
python inspect_spacy_model.py --list
python inspect_spacy_model.py en_core_web_sm --verbose

# 8. When done, deactivate
deactivate
```

- **🔍 Understanding**: See exactly what you downloaded and where it lives
- **🐛 Debugging**: Verify model installation and components
- **📊 Analysis**: Compare different models' capabilities
- **🎓 Learning**: Understand spaCy's internal structure
- **⚡ Quick Reference**: Get entity types and POS tags at a glance

## 🛠️ Requirements

- Python 3.7+
- Virtual environment (recommended)
- spaCy 3.0+
- At least one downloaded spaCy model

## 💡 Virtual Environment Best Practices

### Why Use a Virtual Environment?

- **Isolation**: Keeps project dependencies separate from your system Python
- **Reproducibility**: Ensures consistent environments across different machines
- **Safety**: Prevents conflicts with other Python projects
- **Cleanliness**: Easy to remove by just deleting the environment folder

### Managing Your Environment

**To reactivate your environment later:**
```bash
# For venv:
source spacy-env/bin/activate  # macOS/Linux
spacy-env\Scripts\activate     # Windows

# For conda:
conda activate spacy-env
```

**To check if your environment is active:**
```bash
which python  # Should show path to your virtual environment
python -c "import sys; print(sys.prefix)"  # Should show virtual env path
```

**To see installed packages in your environment:**
```bash
pip list
```

**To remove the environment when no longer needed:**
```bash
# For venv:
rm -rf spacy-env  # macOS/Linux
rmdir /s spacy-env  # Windows

# For conda:
conda env remove -n spacy-env
```

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