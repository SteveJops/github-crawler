import random
from global_imports import httpx, asyncio, logger, List, Dict, configs
from fetch_page import fetch_html
from links_handler import extract_repo_links
from collect_path import build_search_url


async def scrape(params: Dict) -> List[Dict[str, str]]:  # type: ignore
    """
    Scrape GitHub search page with proxy support.

    Args:
        params (Dict): A dictionary containing the following:
            keywords (List[str]): A list of keywords to search for.
            proxies (List[str]): A list of proxies to use.
            search_type (str): The type of search to perform (e.g., "repository", "issues", "wikis").

    Returns:
        List[Dict[str, str]]: A list of dictionaries, each containing a single key-value pair with the key being "url"
        and the value being a URL to a GitHub repository.
    """
    keywords, proxies, search_type = [params.get(opt, []) for opt in params.keys()]
    try:
        url = await build_search_url(keywords, search_type)
        logger.info(f"Url successfully scraped: {url}")
    except Exception as e:
        logger.error(f"Error building search URL: {e}")
        return []
    proxies = (
        proxies if proxies else random.choice(list(configs["proxies_config"].values()))
    )
    async with httpx.AsyncClient() as client:
        logger.info(f"Scraping GitHub search page: {url}")
        for proxy in proxies:
            page = await fetch_html(client, url, proxy)
            logger.info("Got fetched search page...")
            if page:
                links = await extract_repo_links(page)
                logger.info("Links successfully extracted")
                return [{"url": link} for link in links]


if __name__ == "__main__":
    import json
    import argparse

    parser = argparse.ArgumentParser(
        description="GitHub Search Scraper with Proxy Support"
    )
    parser.add_argument(
        "-k", "--keywords", type=str, nargs="+", help="Keywords to search for"
    )
    parser.add_argument("-p", "--proxies", type=str, nargs="+", help="Proxies to use")
    parser.add_argument(
        "-t", "--search-type", type=str, help="Type of search to perform"
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        help="Path to JSON config file with keywords, proxies, and type",
    )
    args = parser.parse_args()

    config = {}
    if args.config:
        with open(args.config) as f:
            config = json.load(f)

    if args.keywords:
        config["keywords"] = args.keywords

    if args.proxies:
        config["proxies"] = args.proxies

    if args.search_type:
        config["search_type"] = args.search_type

    results = asyncio.run(scrape(config))
    print(json.dumps(results, indent=2))
