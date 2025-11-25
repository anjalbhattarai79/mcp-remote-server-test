# 🚀 FastMCP Demo

This is a small demo project showing how to use FastMCP to create a minimal MCP server.

What it offers 🛠️
- A minimal FastMCP server named "My MCP Server".
- One exposed tool: `greet(name: str) -> str` which returns a greeting string.
- Example client showing a remote demo server URL: https://demo-server.fastmcp.app/mcp 📡

How to run locally 🔁
1. Ensure Python is installed.
2. Install dependencies:
   pip install fastmcp
3. Start the server locally:
   python my_server.py

Usage examples 🔧

- Local server (default):
  curl -X POST http://localhost:8000/greet -H "Content-Type: application/json" -d '{"name":"Anjal"}'
  - Example response:
    Hello From Fast MCP, Mr.Anjal!

- Remote demo server:
  You can use the provided demo server if you don't want to run it locally:
  curl -X POST https://demo-server.fastmcp.app/mcp/greet -H "Content-Type: application/json" -d '{"name":"Anjal"}'
  - Example response:
    Hello From Fast MCP, Mr.Anjal!

Client example 🧭
- The included client (my_client.py) is configured to call the remote demo server:
  client = Client("https://demo-server.fastmcp.app/mcp")

Notes ⚠️
- This repo is a demonstration only. Update and expand tools as needed for real applications.
- Adjust transport or port in `my_server.py` if required.
