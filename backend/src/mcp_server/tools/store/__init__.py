"""Store tools (the connected store's name, domain and settings)."""

from fastmcp import FastMCP

from src.mcp_server.tools.store import info


def register(mcp: FastMCP) -> None:
    info.register(mcp)
