from bs4 import BeautifulSoup
from global_imports import List


async def extract_repo_links(page: str) -> List[str]:
    """
    Extract links to repositories from the given HTML of a GitHub search page.

    The links are absolute URLs to the repositories.
    """
    soup = BeautifulSoup(page, "html.parser")
    links = []
    for tag in soup.select("h3 a"):
        href = tag.get("href")
        if href and href.startswith("/"):  # type: ignore
            links.append(f"https://github.com{href}")
    return links
