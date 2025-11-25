import asyncio
from fastmcp import Client

client = Client("https://demo-server.fastmcp.app/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Anjal"))