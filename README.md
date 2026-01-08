# MCP Deployment Server

A Model Context Protocol (MCP) server providing deployment operations.

## Features

- **add**: Add two numbers together

## Installation

### Using uvx (recommended)

```bash
uvx --from . -m src
```

### Using pip

```bash
pip install -e .
```

## Usage

### Running the server

```bash
python -m src
```

Or if installed via pip:

```bash
mcp-deployment
```

### Available Tools

#### add

Adds two numbers together.

**Arguments:**
- `a` (int): The first number
- `b` (int): The second number

**Returns:**
- (int): The sum of the two numbers

## Development

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd mcp-server
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

### Building

```bash
pip install hatchling
python -m build
```

## Requirements

- Python >= 3.8
- mcp

## License

MIT

