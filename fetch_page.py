from global_imports import httpx, logger


async def fetch_html(client: httpx.AsyncClient, url: str, proxy: str) -> str:
    """
    Fetch HTML content from a URL using an httpx.AsyncClient.

    Args:
        client (httpx.AsyncClient): The AsyncClient to use.
        url (str): The URL to fetch.
        proxy (str): The proxy to use for the request.

    Returns:
        str: The HTML content of the page, or an empty string on failure.
    """
    try:
        response = await client.get(
            url,
            timeout=10.0,
        )
        response.raise_for_status()
        logger.info(f"Request succeeded for {url} using proxy {proxy}")
        return response.text
    except Exception as e:
        logger.error(f"Request failed for {url} using proxy {proxy}: {e}")
    return ""
