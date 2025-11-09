# Prompt Engineering

A collection of self-contained Python scripts demonstrating prompt engineering patterns and best practices using the OpenAI API.

## Purpose

This repository hosts small, practical examples that show how to effectively use prompt engineering techniques with OpenAI's models. Each topic lives in its own folder with a single runnable script, making it easy to explore specific patterns without complex setup.

## Repository Structure

```
prompt-engineering/
├── examples/
│   ├── best-practices/          # Prompt engineering best practices
│   ├── code-generation/         # Code explanation and modification
│   ├── get-response/            # Basic usage examples
│   ├── getting-started/         # Introduction examples
│   ├── message-roles/           # OpenAI message role examples
│   ├── shot-prompting/          # Zero-shot, one-shot, few-shot examples
│   ├── structured-output/       # Generating structured formats
│   ├── text-analysis/           # Text categorization and entity extraction
│   └── text-transformation/     # Grammar, tone, and translation
├── utils/
│   └── openai_client.py        # Shared OpenAI helper functions
├── requirements.txt
├── .env.example
├── run_example.py              # Helper script for running examples
└── README.md
```

Each example follows a consistent pattern:
- Organized by topic area
- Self-contained, runnable scripts
- Minimal dependencies
- Clear, inspectable output to stdout

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alvincrespo/prompt-engineering.git
   cd prompt-engineering
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -e .
   ```

   This installs the project in editable mode, making the `utils` package importable from all example scripts.

4. **Set up your OpenAI API key:**

   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and add your API key:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

   Alternatively, export it directly:
   ```bash
   export OPENAI_API_KEY=sk-your-key-here
   ```

## Running the Examples

**Quick Start:** If this is your first time running examples, follow these steps:

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -e .
   ```

3. **Set up your OpenAI API key:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

**For subsequent runs:** Make sure your virtual environment is activated:

```bash
# Activate virtual environment (if not already activated)
source .venv/bin/activate
```

### Option 1: Using the run_example.py helper (Recommended)

The repository includes a helper script that automatically sets up the Python path:

```bash
python run_example.py examples/getting-started/script.py
```

### Option 2: Direct execution

Run scripts directly from the project root:

```bash
python examples/code-generation/explanation/detailed.py
```

All examples use:
- **Model:** `gpt-4o-mini` (fast and cost-effective)
- **Temperature:** `0` (deterministic responses)

## Code Pattern

All examples follow a consistent pattern for easy understanding:

```python
from utils.openai_client import get_response

# Simple prompt (string)
response = get_response("Your prompt here")
print(response)

# Advanced usage with message history (list of dicts)
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]
response = get_response(messages)
print(response)
```

The `get_response` helper function is defined in `utils/openai_client.py` and handles:
- OpenAI client initialization
- Loading environment variables from `.env`
- Making chat completion calls with `gpt-4o-mini` and `temperature=0`
- Supporting both simple string prompts and full message arrays

## Examples

### Best Practices
**Location:** `examples/best-practices/`
- `introduction.py` - Core prompt engineering principles and patterns

### Getting Started
**Location:** `examples/getting-started/`
- `script.py` - Minimal example to get started with prompt engineering

### Code Generation
**Location:** `examples/code-generation/`
- `explanation/` - Code explanation examples (generic and detailed)
- `modification/` - Code modification examples (single and multi-step)
- `input-output.py` - Input/output pattern examples
- `prompts.py` - Various code generation prompts

### Message Roles
**Location:** `examples/message-roles/`
- `script.py` - Using system, user, and assistant message roles

### Shot Prompting
**Location:** `examples/shot-prompting/`
- `zero-shot.py` - No examples provided
- `one-shot.py` - One example provided
- `few-shot.py` - Multiple examples provided
- `few-shot-assistant.py` - Using assistant role for examples

### Structured Output
**Location:** `examples/structured-output/`
- `conditional/` - Single and multiple conditional outputs
- `lists/` - Ordered and unordered list generation
- `custom-output.py` - Custom output formats
- `paragraphs.py` - Paragraph generation
- `tables.py` - Table generation

### Text Analysis
**Location:** `examples/text-analysis/`
- `categories/` - Text categorization (specified, unspecified, multiple)
- `entity-extraction/` - Extract specific entities and few-shot patterns

### Text Transformation
**Location:** `examples/text-transformation/`
- `adjustments/` - Tone adjustment (generic and targeted)
- `languages/` - Multi-language translation
- `grammar.py` - Grammar improvements
- `multi-step.py` - Multiple transformations in sequence

### Get Response Usage
**Location:** `examples/get-response/`
- `import-example.py` - Example of importing and using the get_response helper

## Contributing

When adding new examples:

1. Place the script in the appropriate category folder under `examples/`
2. Create subdirectories for related examples when it makes sense
3. Follow the established `get_response(prompt)` or `get_response(messages)` pattern
4. Keep dependencies minimal
5. Print results to stdout for easy inspection
6. Use `temperature=0` and `gpt-4o-mini` unless the example specifically requires different settings
7. Use the `run_example.py` script to test your examples

## Troubleshooting

**`ModuleNotFoundError: No module named 'utils'`**
- Use the `run_example.py` helper script: `python run_example.py examples/path/to/script.py`
- Or ensure you're running from the project root and have installed with `pip install -e .`

**`NameError: name 'overload' is not defined`**
- This has been fixed in the latest version. Make sure you've pulled the latest changes.

**401/403 API errors**
- Verify your `OPENAI_API_KEY` is set correctly in your `.env` file
- Check that your API key is valid and has available credits
- Never hardcode API keys in your scripts

**Empty or None responses**
- Inspect the `response.choices` structure before indexing
- Check the OpenAI API status if issues persist

## License

[MIT License Copyright (c) 2025](./LICENSE)
