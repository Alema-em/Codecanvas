# CodeStory

CodeStory is an interactive tool that helps visualize how Python code executes step by step.

It highlights code as it runs, simulates loop execution and generates AI explanations using a local LLM.

## Features

- Step-by-step execution simulation
- Line-by-line code highlighting
- Execution flow visualization
- AI powered code explanations using Ollama
- Interactive web interface

## Tech Stack

- Python
- Flask
- JavaScript
- Ollama (Local LLM)
- HTML / CSS

## Example

Input Python code like:

```python
i = 1
while i <= 5:
    square = i * i
    print(square)
    i += 1
