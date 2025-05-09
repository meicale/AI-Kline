from mcp.server.fastmcp import FastMCP


# Initialize FastMCP server
mcp = FastMCP("AI-Kline")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)