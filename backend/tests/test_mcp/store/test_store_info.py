import respx

from tests.test_mcp.conftest import BASE_URL, Harness

STORE = {
    "id": 999,
    "name": {"es": "Mi Tienda"},
    "main_language": "es",
    "main_currency": "ARS",
    "original_domain": "mitienda.mitiendanube.com",
    "url_with_protocol": "https://mitienda.com.ar",
    "domains": ["mitienda.com.ar"],
    "logo": "//dcdn-us.mitiendanube.com/stores/999/logo.png",
    "country": "AR",
}


@respx.mock
async def test_store_info_with_domain_and_product_link(harness: Harness) -> None:
    respx.get(f"{BASE_URL}/store").respond(200, json=STORE)
    data = await harness.call("get_store_info")
    assert data["name"] == "Mi Tienda"
    assert data["url"] == "https://mitienda.com.ar"
    assert data["original_domain"] == "mitienda.mitiendanube.com"
    assert data["product_url_template"] == "https://mitienda.com.ar/productos/{handle}/"
    assert data["logo_url"] == "https://dcdn-us.mitiendanube.com/stores/999/logo.png"


@respx.mock
async def test_store_info_falls_back_to_original_domain(harness: Harness) -> None:
    store = {**STORE, "url_with_protocol": None, "domains": [], "main_language": "pt"}
    respx.get(f"{BASE_URL}/store").respond(200, json=store)
    data = await harness.call("get_store_info")
    assert data["url"] == "https://mitienda.mitiendanube.com"
    assert data["product_url_template"] == "https://mitienda.mitiendanube.com/produtos/{handle}/"


@respx.mock
async def test_store_info_works_without_scopes(harness: Harness) -> None:
    harness.set_scopes("read_orders")
    respx.get(f"{BASE_URL}/store").respond(200, json=STORE)
    data = await harness.call("get_store_info")
    assert data["store_id"] == 999
