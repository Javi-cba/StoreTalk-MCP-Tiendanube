"""Store tools: info of the connected store."""

from fastmcp import FastMCP
from mcp.types import ToolAnnotations

from src.mcp_server import context
from src.mcp_server.tools.store.schemas import StoreDetails, summarize


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(title="Get store info", readOnlyHint=True, openWorldHint=True)
    )
    async def get_store_info() -> StoreDetails:
        """Get the connected store: name, public URL/domain, language, currency and contact.

        Call it whenever you need the store name, its domain or a link to the storefront or
        to a product (use `product_url_template` with the product handle). Never guess the
        domain.
        """
        ctx = await context.get_store_context()
        store = await context.run_tiendanube(ctx, ctx.client.get_store)
        return summarize(store)
