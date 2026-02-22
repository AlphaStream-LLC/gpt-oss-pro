import asyncio
from mcp.server.fastmcp import FastMCP

m = FastMCP("test_server")

@m.tool()
async def my_tool(x: int) -> int:
    return x * 2

async def main():
    print("Listing tools:")
    tools = await m.list_tools()
    for t in tools:
        print(t)
    
    print("Calling tool:")
    # Note: call_tool usually expects tool name and arguments
    result = await m.call_tool("my_tool", arguments={"x": 5})
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
