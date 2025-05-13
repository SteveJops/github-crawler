import urllib.parse
from typing import List
from global_imports import configs

GITHUB_SEARCH_URL = configs["GITHUB_SEARCH_URL"]


async def build_search_url(keywords: List[str], search_type: str) -> str:
    """
    Constructs a GitHub search URL based on the given keywords and search type.

    Args:
        keywords (List[str]): A list of keywords to include in the search query.
        search_type (str): The type of search to perform (e.g., "repository", "issues", "wikis").

    Returns:
        str: A formatted URL string for the GitHub search query.
    """

    search_type = (
        search_type if search_type.lower() in configs["search_type"] else "repositories"
    )
    query = "+".join(urllib.parse.quote_plus(kw) for kw in keywords)
    return f"{GITHUB_SEARCH_URL}?q={query}&type={search_type}"
