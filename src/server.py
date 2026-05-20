import os
import fastmcp

SKILLS_DIR = os.environ.get("SKILLS_DIR", "./skills")
PORT = int(os.environ.get("PORT", "8000"))

mcp = fastmcp.FastMCP("fastmcp-skill-server")

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=PORT)
