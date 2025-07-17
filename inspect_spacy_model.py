#!/usr/bin/env python3
"""
spaCy Model Inspector

A utility to inspect and analyze downloaded spaCy models, revealing their
internal structure, components, and capabilities.

Usage:
    python inspect_spacy_model.py [model_name]

Examples:
    python inspect_spacy_model.py
    python inspect_spacy_model.py en_core_web_md
    python inspect_spacy_model.py --list
"""

import argparse
import sys
from pathlib import Path

import spacy


def list_available_models():
    """List all available spaCy models in the current environment."""
    print("🔍 Searching for installed spaCy models...\n")

    try:
        # Get all installed packages
        import pkg_resources

        installed_packages = [d.project_name for d in pkg_resources.working_set]

        # Filter for spaCy models (they typically follow pattern like en_core_web_sm)
        spacy_models = []
        for package in installed_packages:
            if any(
                lang in package
                for lang in ["en_", "de_", "fr_", "es_", "pt_", "it_", "nl_", "zh_"]
            ):
                if any(size in package for size in ["_sm", "_md", "_lg", "_trf"]):
                    spacy_models.append(package)

        if spacy_models:
            print("📦 Found spaCy models:")
            for model in sorted(spacy_models):
                try:
                    nlp = spacy.load(model)
                    size = f"~{nlp.meta.get('size', 'Unknown')}"
                    version = nlp.meta.get("version", "Unknown")
                    print(f"   ✅ {model} (v{version}, {size})")
                except OSError as e:
                    print(f"   ❌ {model} (installation issue) -- error: {e}")
        else:
            print("❌ No spaCy models found.")
            print("\n💡 Install a model with: python -m spacy download en_core_web_sm")

    except ImportError:
        print("❌ Could not check installed packages. Make sure spaCy is installed.")


def inspect_spacy_model(model_name: str = "en_core_web_sm", verbose: bool = False):
    """Inspect the specified spaCy model."""

    print(f"🔍 Inspecting spaCy model: {model_name}\n")

    # Load the model
    try:
        nlp = spacy.load(model_name)
        print("✅ Model loaded successfully!")
    except OSError:
        print(f"❌ Model '{model_name}' not found.")
        print(f"💡 Install it with: python -m spacy download {model_name}")
        print("\n🔍 Use --list to see available models")
        return False

    # Model location
    print("\n📍 Model Location:")
    print(f"   {nlp._path}")

    # Model metadata
    print("\n📊 Model Metadata:")
    meta = nlp.meta
    print(f"   Name: {meta['name']}")
    print(f"   Version: {meta['version']}")
    print(f"   Description: {meta['description']}")
    print(f"   Language: {meta['lang']}")
    print(f"   Pipeline: {meta['pipeline']}")
    print(f"   Size: ~{meta.get('size', 'Unknown')}")

    if verbose:
        print(f"   License: {meta.get('license', 'Unknown')}")
        print(f"   Author: {meta.get('author', 'Unknown')}")
        print(f"   URL: {meta.get('url', 'Unknown')}")

    # Pipeline components
    print("\n🔧 Pipeline Components:")
    for name, component in nlp.pipeline:
        print(f"   - {name}: {type(component).__name__}")

    # Vocabulary stats
    print("\n📚 Vocabulary:")
    print(f"   Total tokens: {len(nlp.vocab):,}")
    if nlp.vocab.vectors.shape[0] > 0:
        print(f"   Vector dimensions: {nlp.vocab.vectors.shape[1]}")
        print(f"   Vectors available: {nlp.vocab.vectors.shape[0]:,}")
    else:
        print("   Vectors: No word vectors available")

    # Entity types
    if nlp.has_pipe("ner"):
        print("\n🏷️  Named Entity Types:")
        for label in nlp.get_pipe("ner").labels:
            explanation = spacy.explain(label) or "Entity type"
            print(f"   - {label}: {explanation}")

    # POS tags
    if nlp.has_pipe("tagger"):
        print("\n📝 POS Tags (sample):")
        pos_tags = list(nlp.get_pipe("tagger").labels)[:10]  # Show first 10
        for tag in pos_tags:
            explanation = spacy.explain(tag) or "Part-of-speech tag"
            print(f"   - {tag}: {explanation}")
        if len(nlp.get_pipe("tagger").labels) > 10:
            print(f"   ... and {len(nlp.get_pipe('tagger').labels) - 10} more")

    # Test the model
    print("\n🧪 Model Test:")
    test_text = (
        "Apple Inc. is looking at buying a startup in San Francisco for $1 billion."
    )
    doc = nlp(test_text)

    print(f"   Input: {test_text}")
    print(f"   Tokens: {[token.text for token in doc]}")
    if doc.ents:
        print(f"   Entities: {[(ent.text, ent.label_) for ent in doc.ents]}")
    else:
        print("   Entities: No entities detected")

    if verbose:
        print(f"   POS Tags: {[(token.text, token.pos_) for token in doc]}")
        print(
            f"   Lemmas: {[(token.text, token.lemma_) for token in doc if token.text != token.lemma_]}"
        )

    # File structure inspection (only if verbose)
    if verbose:
        print("\n📁 Model File Structure:")
        model_path = Path(nlp._path)

        def print_tree(path, prefix="", max_depth=3, current_depth=0):
            if current_depth >= max_depth:
                return

            try:
                items = sorted(path.iterdir())
                for i, item in enumerate(items):
                    is_last = i == len(items) - 1
                    current_prefix = "└── " if is_last else "├── "
                    print(f"{prefix}{current_prefix}{item.name}")

                    if item.is_dir() and current_depth < max_depth - 1:
                        next_prefix = prefix + ("    " if is_last else "│   ")
                        print_tree(item, next_prefix, max_depth, current_depth + 1)
            except PermissionError:
                print(f"{prefix}└── [Permission Denied]")

        print_tree(model_path)

    # Storage information
    print("\n💾 Storage Information:")
    model_path = Path(nlp._path)
    try:
        total_size = sum(f.stat().st_size for f in model_path.rglob("*") if f.is_file())
        print(f"   Total model size: {total_size / (1024*1024):.1f} MB")

        if verbose:
            # Largest files
            large_files = []
            for f in model_path.rglob("*"):
                if f.is_file():
                    size = f.stat().st_size
                    large_files.append((f.name, size))

            large_files.sort(key=lambda x: x[1], reverse=True)
            print("\n   Largest files:")
            for name, size in large_files[:5]:
                print(f"   - {name}: {size / (1024*1024):.1f} MB")
    except Exception as e:
        print(f"   Could not calculate size: {e}")

    return True


def main():
    """Main function with command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Inspect spaCy models and reveal their internal structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Inspect default model (en_core_web_sm)
  %(prog)s en_core_web_md            # Inspect specific model
  %(prog)s --list                    # List all available models
  %(prog)s en_core_web_lg --verbose  # Detailed inspection
        """,
    )

    parser.add_argument(
        "model",
        nargs="?",
        default="en_core_web_sm",
        help="spaCy model name to inspect (default: en_core_web_sm)",
    )

    parser.add_argument(
        "--list", "-l", action="store_true", help="List all installed spaCy models"
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed information including file structure",
    )

    parser.add_argument(
        "--version", action="version", version="spaCy Model Inspector 1.0.0"
    )

    args = parser.parse_args()

    if args.list:
        list_available_models()
        return

    success = inspect_spacy_model(args.model, args.verbose)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
