import asyncio
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
# In a real scenario, we would use an MCP Client to connect to these servers.
# For this "Self-Evolving Loop" demo, we will import the server instances directly 
# or simulate the client connection to local function tools if they were running processes.
# To keep this Python-native for the simulation, we will wrap the tools directly.

# We will treat the Bridge itself additionally as a FastMCP server that aggregates others?
# Or just a Python class that the Agent uses? The requirement says "unified_api_bridge.py that allows... to call any of these".

class UnifiedBridge:
    def __init__(self):
        self.servers: Dict[str, Any] = {}
        # Map: full_tool_name -> (mcp_instance, original_tool_name)
        self.tool_map: Dict[str, tuple] = {}

    async def register_server(self, name: str, server_module: Any):
        """
        Registers a Simulated MCP Server module.
        """
        print(f"Registering MCP Server: {name}")
        self.servers[name] = server_module
        
        if hasattr(server_module, 'mcp') and isinstance(server_module.mcp, FastMCP):
             tools = await server_module.mcp.list_tools()
             for tool in tools:
                 full_tool_name = f"{name}_{tool.name}"
                 self.tool_map[full_tool_name] = (server_module.mcp, tool.name)
                 print(f"  - Discovered Tool: {full_tool_name}")

    async def list_tools(self) -> List[str]:
        return list(self.tool_map.keys())

    async def call_tool(self, tool_name: str, **kwargs) -> str:
        if tool_name not in self.tool_map:
             return f"Error: Tool {tool_name} not found."
        
        mcp_instance, original_name = self.tool_map[tool_name]
        print(f"Bridge Routing: Calling {original_name} on {mcp_instance.name} with {kwargs}")
        
        try:
            # call_tool returns CallToolResult or similar structure which seemed to be (content, context)
            result = await mcp_instance.call_tool(original_name, arguments=kwargs)
            
            # The result from debug output was ([TextContent...], val)
            # The first element is the content list.
            content_list = result[0]
            
            # Extract text from content
            output_texts = []
            for content in content_list:
                if hasattr(content, 'text'):
                    output_texts.append(content.text)
                else:
                    output_texts.append(str(content))
            return "\n".join(output_texts)

        except Exception as e:
            return f"Error executing {tool_name}: {str(e)}"

# Singleton instance
bridge = UnifiedBridge()
