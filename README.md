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

python
i = 1
while i <= 5:
    square = i * i
    print(square)
    i += 1



#CodeStory will:

Simulate each loop iteration
Highlight the currently executing line
Show the output produced
Generate an AI explanation of the program

#Current Status

This project is currently a V1 prototype and supports only basic Python constructs such as:simple loops,basic conditionals,simple arithmetic operations
The current analyzer uses rule-based parsing and therefore only works reliably for simpler code snippets.

#Vision

The long-term goal of CodeStory is to become an AI tutor and debugger for computer science students.

Future versions aim to include:
-full Python AST-based analysis
-accurate execution tracing
-interactive debugging
-step-through variable tracking
-better AI explanations
-support for more programming constructs

Ultimately, CodeStory is intended to help students understand how code executes internally, similar to tools like Python Tutor but enhanced with AI explanations.

    square = i * i
    print(square)
    i += 1
