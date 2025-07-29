import argparse
from pathlib import Path

from docling.document_converter import DocumentConverter


def validate_file_path(path_str: str) -> Path:
    """Validate that the file path exists and return Path object."""
    path = Path(path_str)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")
    return path


def main(source: str):
    # Process the document
    converter = DocumentConverter()
    doc = converter.convert(source).document
    print(doc.export_to_markdown())
    # jsn: str = doc.export_to_dict()
    # print(json.dumps(jsn, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert documents using Docling.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", type=str, help="URL of the document to convert")
    group.add_argument(
        "--pdf_path", type=str, help="Local path to the PDF file to convert"
    )

    args = parser.parse_args()

    # Get the source (URL or validated file path)
    if args.url:
        source = args.url
    else:  # args.pdf_path is guaranteed to exist due to mutual exclusivity and required=True
        source = str(validate_file_path(args.pdf_path))
    main(source)
