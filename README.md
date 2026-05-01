# 🧬 BioSeq Toolkit

A lightweight Python-based bioinformatics tool designed for DNA sequence analysis. This toolkit allows users to input sequences manually or via FASTA files to perform essential genomic calculations.

## 🚀 Features

*   **Dual Input Modes**: Support for manual sequence entry or reading directly from `.fsta` / `.fasta` files.
*   **DNA Analysis**: Calculates sequence length and GC Content percentage.
*   **Transcription & Translation**: Converts DNA to RNA and translates sequences into Amino Acid (protein) chains.
*   **Reverse Complement**: Generates the 3' to 5' reverse complement of the input DNA.
*   **Motif Searching**: Locates specific patterns (like "ATG") and returns all index positions.
*   **Mutation Detection**: Compares two sequences of equal length to identify point mutations.
*   **Automated Reporting**: Generates a clean `bioseq_report.txt` file after every run.

## 🛠️ Installation & Requirements

1.  **Python 3.x**: Ensure you have Python installed.
2.  **No External Dependencies**: This toolkit uses standard Python libraries, so no `pip install` is required!

## 📖 How to Use

1.  Clone this repository or download `bioseq_toolkit.py`.
2.  Place your FASTA files in the same project folder for easy access.
3.  Run the script:
    ```bash
    python bioseq_toolkit.py
    ```
4.  Follow the on-screen prompts to select your input method and search for motifs.

## 📋 Example Output

After running an analysis, the `bioseq_report.txt` will look like this:
```text
=====================================================
               REPORT FOR: FASTA File
=====================================================
Original DNA: ATGC...
Sequence Length: 720 bp
GC Content: 55.69%
Protein Sequence: MK...*
...



## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
