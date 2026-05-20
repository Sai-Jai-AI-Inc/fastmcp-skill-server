import os
from pathlib import Path
import fastmcp

SKILLS_DIR = Path(os.environ.get("SKILLS_DIR", "./skills"))
PORT = int(os.environ.get("PORT", "8000"))

mcp = fastmcp.FastMCP("fastmcp-skill-server")


@mcp.tool()
def list_skills() -> list[str]:
    """List all available skill filenames."""
    if not SKILLS_DIR.is_dir():
        return []
    return sorted(p.name for p in SKILLS_DIR.iterdir() if p.is_file() and p.suffix == ".md")


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=PORT)
