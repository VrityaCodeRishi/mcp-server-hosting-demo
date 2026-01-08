from mcp.server import FastMCP

app = FastMCP("deployment")

@app.tool()
def add(a: int, b: int) -> int:
    """Add two numbers
    Args:
        a: The first number
        b: The second number
    Returns:
        The sum of the two numbers
    """
    return a + b