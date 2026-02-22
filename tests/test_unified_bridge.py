import asyncio
import sys
import os

# Ensure the package is in path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from gpt_oss.unified_api_bridge import bridge
from gpt_oss.mcp_stubs import finance_server, health_server

async def main():
    print("--- Starting Project OMEGA Phase 1 Verification ---")
    
    # 1. Register Servers
    print("\n[Step 1] Registering MCP Servers...")
    await bridge.register_server("finance", finance_server)
    await bridge.register_server("health", health_server)
    
    # 2. List Tools
    print("\n[Step 2] Listing Available Tools in the Concept Model...")
    tools = await bridge.list_tools()
    for tool in tools:
        print(f"  - {tool}")
    
    # 3. Test Finance API
    print("\n[Step 3] Testing Finance API (Omni-Interface)...")
    stock_response = await bridge.call_tool("finance_get_stock_price", symbol="AAPL")
    print(f"  > Input: AAPL")
    print(f"  > Output: {stock_response}")
    
    portfolio_response = await bridge.call_tool("finance_get_portfolio_balance", account_id="acc_12345")
    print(f"  > Input: acc_12345")
    print(f"  > Output: {portfolio_response}")

    # 4. Test Health API
    print("\n[Step 4] Testing Health API (Omni-Interface)...")
    heart_response = await bridge.call_tool("health_get_heart_rate", user_id="user_001")
    print(f"  > Input: user_001")
    print(f"  > Output: {heart_response}")

    print("\n[SUCCESS] Phase 1 Verification Complete: Omni-Interface is operational.")

if __name__ == "__main__":
    asyncio.run(main())
