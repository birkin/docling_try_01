"""
Experiments with docling: <https://github.com/docling-project/docling>

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
from docling_core.types.doc import DoclingDocument  # just for the type-hint

# from docling.datamodel.docling_document import DoclingDocument

if platform.system() == "Darwin":  # Darwin is the system name for macOS
    warnings.filterwarnings(
        "ignore",
        message="'pin_memory' argument is set as true but not supported on MPS now",
    )


def validate_file_path(path_str: str) -> Path:
    """
    Validates that the file path exists and return Path object.
    """
    path = Path(path_str)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")
    return path


def main(source: str) -> None:
    """
    Flow:
    - Instantiates a DocumentConverter
    - Converts the document to a DoclingDocument
    - Exports the document to markdown
    - Prints the markdown

    Interesting note: when the line `doc: DoclingDocument = converter.convert(source).document` is run,
    the `source` has not yet been identified as a url or filepath.

    I have a memory of Mark Pilgrim, in his online-book "Dive into Python", doing something similar.
    """
    ## process the document
    converter = DocumentConverter()
    doc: DoclingDocument = converter.convert(source).document
    ## create and output the markdown
    markdown: str = doc.export_to_markdown()
    print(markdown)
    # jsn: str = doc.export_to_dict()
    # formatted_json: str = json.dumps(jsn, indent=2)
    # print(formatted_json)


if __name__ == "__main__":
    ## handle args
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
