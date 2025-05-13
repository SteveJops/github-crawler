from collect_path import build_search_url
from links_handler import extract_repo_links
from global_imports import pytest, asyncio


@pytest.mark.asyncio
async def test_build_search_url():
    keywords = ["openstack", "nova"]
    url = await build_search_url(keywords, "Repositories")
    assert "openstack" in url and "nova" in url and "type=repositories" in url


@pytest.mark.asyncio
async def test_extract_repo_links():
    html = """
    <html>
        <body>
            <h3><a href="/user/repo1">Repo1</a></h3>
            <h3><a href="/user/repo2">Repo2</a></h3>
        </body>
    </html>
    """
    links = await extract_repo_links(html)
    assert links == ["https://github.com/user/repo1", "https://github.com/user/repo2"]
