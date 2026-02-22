from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server for Health
mcp = FastMCP("health")

@mcp.tool()
async def get_heart_rate(user_id: str) -> str:
    """Get the latest heart rate reading for a user."""
    # Simulated data
    if user_id == "user_001":
        return "Latest Heart Rate: 72 bpm (Resting)"
    return "User not found."

@mcp.tool()
async def get_medical_history(user_id: str) -> str:
    """Retrieve summary of medical history."""
    if user_id == "user_001":
        return "History: No major allergies. 2024 Annual Checkup: All Clear."
    return "User not found."

if __name__ == "__main__":
    mcp.run()
