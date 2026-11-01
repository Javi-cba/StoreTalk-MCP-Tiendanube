"""Output models of the store tools."""

from pydantic import BaseModel, Field

from src.schemas.stores import absolute_url
from src.services.tiendanube.models import TNStore, localize

# Storefront path of a product page by store language (Tiendanube theme routes).
_PRODUCT_PATH = {"es": "productos", "pt": "produtos", "en": "products"}


class StoreDetails(BaseModel):
    store_id: int
    name: str | None
    url: str | None = Field(description="Public storefront URL, e.g. 'https://mitienda.com.ar'.")
    original_domain: str | None = Field(description="The '<name>.mitiendanube.com' domain.")
    custom_domains: list[str]
    product_url_template: str | None = Field(
        description="Build product links replacing {handle} with the product handle."
    )
    language: str | None
    currency: str | None
    country: str | None
    email: str | None
    contact_email: str | None
    phone: str | None
    logo_url: str | None
    plan: str | None


def summarize(store: TNStore) -> StoreDetails:
    language = store.main_language
    url = _store_url(store)
    path = _PRODUCT_PATH.get((language or "es").split("_")[0])
    return StoreDetails(
        store_id=store.id,
        name=localize(store.name, language),
        url=url,
        original_domain=store.original_domain,
        custom_domains=store.domains,
        product_url_template=f"{url}/{path}/{{handle}}/" if url and path else None,
        language=language,
        currency=store.main_currency,
        country=store.country,
        email=store.email,
        contact_email=store.contact_email,
        phone=store.phone,
        logo_url=absolute_url(store.logo),
        plan=store.plan_name,
    )


def _store_url(store: TNStore) -> str | None:
    if store.url_with_protocol:
        return store.url_with_protocol.rstrip("/")
    domain = store.domains[0] if store.domains else store.original_domain
    if not domain:
        return None
    return domain.rstrip("/") if domain.startswith("http") else f"https://{domain.rstrip('/')}"
