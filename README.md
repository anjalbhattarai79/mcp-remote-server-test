# FastMCP Demo

This is a small demo project showing how to use FastMCP to create a minimal MCP server.

What it offers
- A minimal FastMCP server named "My MCP Server".
- One exposed tool: `greet(name: str) -> str` which returns a greeting string.
- Runs using HTTP transport on port 8000 by default.

How to run
1. Ensure Python is installed.
2. Install dependencies (example):
   pip install fastmcp
3. Start the server:
   python my_server.py

Usage example (curl)
- Request:
  curl -X POST http://localhost:8000/greet -H "Content-Type: application/json" -d '{"name":"Anjal"}'
- Example response:
  Hello From Fast MCP, Mr.Anjal!

Notes
- This repo is a demonstration only. Update and expand tools as needed for real applications.
- Adjust transport or port in `my_server.py` if required.
