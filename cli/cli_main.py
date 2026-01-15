# cli/cli_main.py

import sys
import os

# Agregar la carpeta raíz al path para que los imports funcionen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cli.commands import analyze_code  # tu import original
import argparse

def main():
    parser = argparse.ArgumentParser(description="AI Dev Platform CLI")
    parser.add_argument("file", help="File to analyze")
    args = parser.parse_args()
    
    # Solo un ejemplo de análisis
    print(f"Analyzing file: {args.file}")
    analyze_code(args.file)

if __name__ == "__main__":
    main()
