# latex2mathml

Pure Python library for LaTeX to MathML conversion

## Installation

```bash
pip install latex2mathml
```

## Usage

### Python

```python
import latex2mathml.converter

latex_input = "<your_latex_string>"
mathml_output = latex2mathml.converter.convert(latex_input)
```

## Command-line

```bash
% latex2mathml -h
usage: latex2mathml [-h] [-V] [-b] [-t TEXT | -f FILE | -s]

Pure Python library for LaTeX to MathML conversion

options:
  -h, --help            show this help message and exit
  -V, --version         Show version
  -b, --block           Display block

required arguments:
  -t TEXT, --text TEXT  Text
  -f FILE, --file FILE  File
  -s, --stdin           Stdin
```

## Key Features

- Pure Python implementation
- Converts LaTeX mathematical expressions to MathML format
- Supports both programmatic usage and command-line interface
- Can process text input, file input, or stdin
- Block display option available

## Basic Usage Examples

### Convert LaTeX string to MathML
```python
import latex2mathml.converter

# Simple fraction
latex = r"\frac{1}{2}"
mathml = latex2mathml.converter.convert(latex)

# Quadratic formula
latex = r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"
mathml = latex2mathml.converter.convert(latex)
```

### Command-line usage
```bash
# Convert text directly
latex2mathml -t "\frac{1}{2}"

# Convert from file
latex2mathml -f input.tex

# Convert from stdin
echo "\frac{1}{2}" | latex2mathml -s

# Display as block
latex2mathml -t "\frac{1}{2}" -b
```