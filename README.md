# Experimenting with docling

<https://github.com/docling-project/docling>

A simple command-line tool for converting documents to markdown format using the [docling](https://github.com/docling-project/docling) library.


## Installation

   ```bash
   % git clone repository-url
   ```


## Usage

   ```bash
   % cd ./docling_try_01
   % uv run ./main.py --pdf_path path/to/your/document.pdf
   ```

   ...or...

   ```bash
   % cd ./docling_try_01
   % uv run ./main.py --url https://example.com/document.pdf
   ```
   
   ..either will yield markdown output to stdout.


## Note

- The project uses AI-models for conversion, so the initial install can take some time.

- Again because of the AI-model usage, running the conversion can take a few seconds.

---
