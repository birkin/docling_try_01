"""
Experiments with docling: <https://>

Note: I believe this warning is related to PyTorch's DataLoader and MPS (Metal Performance Shaders) backend on macOS.
    The platform-check suppresses a harmless macOS warning which indicates that while pin_memory=True
    is set in the DataLoader, this feature isn't supported on MPS devices. The code will still
    work correctly, just without the performance optimization that pinned memory would provide.
"""

import argparse
import platform
import warnings
from pathlib import Path

from docling.document_converter import DocumentConverter

if platform.system() == "Darwin":  # Darwin is the system name for macOS
    warnings.filterwarnings(
        "ignore",
        message="'pin_memory' argument is set as true but not supported on MPS now",
    )


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

    ## get the source (URL or validated file path)
    if args.url:
        source = args.url
    else:  # args.pdf_path is guaranteed to exist due to mutual exclusivity and required=True
        source = str(validate_file_path(args.pdf_path))
    main(source)
