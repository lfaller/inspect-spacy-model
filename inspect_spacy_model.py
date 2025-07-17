# Inspect spaCy model contents
# Run this after downloading the model

import spacy
import json
from pathlib import Path

def inspect_spacy_model():
    """Inspect the downloaded spaCy model."""
    
    # Load the model
    try:
        nlp = spacy.load("en_core_web_sm")
        print("✅ Model loaded successfully!")
    except OSError:
        print("❌ Model not found. Run: python -m spacy download en_core_web_sm")
        return
    
    # Model location
    print(f"\n📍 Model Location:")
    print(f"   {nlp._path}")
    
    # Model metadata
    print(f"\n📊 Model Metadata:")
    meta = nlp.meta
    print(f"   Name: {meta['name']}")
    print(f"   Version: {meta['version']}")
    print(f"   Description: {meta['description']}")
    print(f"   Language: {meta['lang']}")
    print(f"   Pipeline: {meta['pipeline']}")
    print(f"   Size: ~{meta.get('size', 'Unknown')}")
    
    # Pipeline components
    print(f"\n🔧 Pipeline Components:")
    for name, component in nlp.pipeline:
        print(f"   - {name}: {type(component).__name__}")
    
    # Vocabulary stats
    print(f"\n📚 Vocabulary:")
    print(f"   Total tokens: {len(nlp.vocab)}")
    print(f"   Vector dimensions: {nlp.vocab.vectors.shape[1] if nlp.vocab.vectors.shape[0] > 0 else 'No vectors'}")
    print(f"   Vectors available: {nlp.vocab.vectors.shape[0]:,}")
    
    # Entity types
    print(f"\n🏷️  Named Entity Types:")
    for label in nlp.get_pipe("ner").labels:
        print(f"   - {label}: {spacy.explain(label)}")
    
    # POS tags
    print(f"\n📝 POS Tags (sample):")
    pos_tags = list(nlp.get_pipe("tagger").labels)[:10]  # Show first 10
    for tag in pos_tags:
        print(f"   - {tag}: {spacy.explain(tag) or 'Part-of-speech tag'}")
    if len(nlp.get_pipe("tagger").labels) > 10:
        print(f"   ... and {len(nlp.get_pipe("tagger").labels) - 10} more")
    
    # Test the model
    print(f"\n🧪 Model Test:")
    test_text = "Apple Inc. is looking at buying a startup in San Francisco for $1 billion."
    doc = nlp(test_text)
    
    print(f"   Input: {test_text}")
    print(f"   Tokens: {[token.text for token in doc]}")
    print(f"   Entities: {[(ent.text, ent.label_) for ent in doc.ents]}")
    print(f"   POS Tags: {[(token.text, token.pos_) for token in doc]}")
    
    # File structure inspection
    print(f"\n📁 Model File Structure:")
    model_path = Path(nlp._path)
    
    def print_tree(path, prefix="", max_depth=3, current_depth=0):
        if current_depth >= max_depth:
            return
        
        items = sorted(path.iterdir())
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            current_prefix = "└── " if is_last else "├── "
            print(f"{prefix}{current_prefix}{item.name}")
            
            if item.is_dir() and current_depth < max_depth - 1:
                next_prefix = prefix + ("    " if is_last else "│   ")
                print_tree(item, next_prefix, max_depth, current_depth + 1)
    
    print_tree(model_path)
    
    # Show some actual file contents
    print(f"\n📄 Sample File Contents:")
    
    # Meta.json
    meta_file = model_path / "meta.json"
    if meta_file.exists():
        print(f"\n   meta.json (first 5 lines):")
        with open(meta_file, 'r') as f:
            meta_data = json.load(f)
            for i, (key, value) in enumerate(meta_data.items()):
                if i >= 5:
                    print("        ...")
                    break
                print(f"        {key}: {value}")
    
    # Config.cfg
    config_file = model_path / "config.cfg"
    if config_file.exists():
        print(f"\n   config.cfg (first 10 lines):")
        with open(config_file, 'r') as f:
            for i, line in enumerate(f):
                if i >= 10:
                    print("        ...")
                    break
                print(f"        {line.rstrip()}")
    
    # Size information
    print(f"\n💾 Storage Information:")
    total_size = sum(f.stat().st_size for f in model_path.rglob('*') if f.is_file())
    print(f"   Total model size: {total_size / (1024*1024):.1f} MB")
    
    # Largest files
    large_files = []
    for f in model_path.rglob('*'):
        if f.is_file():
            size = f.stat().st_size
            large_files.append((f.name, size))
    
    large_files.sort(key=lambda x: x[1], reverse=True)
    print(f"\n   Largest files:")
    for name, size in large_files[:5]:
        print(f"   - {name}: {size / (1024*1024):.1f} MB")

if __name__ == "__main__":
    inspect_spacy_model()