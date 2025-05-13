import unittest
from unittest.mock import patch
from main import scrape


class TestScrapeGithub(unittest.IsolatedAsyncioTestCase):
    @patch("main.build_search_url")
    @patch("main.fetch_html")
    @patch("main.extract_repo_links")
    async def test_valid_params(
        self, mock_extract_repo_links, mock_fetch_html, mock_build_search_url
    ):
        params = {
            "keywords": ["python", "github"],
            "proxies": ["proxy1", "proxy2"],
            "search_type": "repository",
        }
        mock_build_search_url.return_value = (
            "https://github.com/search?q=python+github&type=repository"
        )
        mock_fetch_html.return_value = "<html>...</html>"
        mock_extract_repo_links.return_value = [
            "https://github.com/user/repo1",
            "https://github.com/user/repo2",
        ]

        result = await scrape(params)
        self.assertEqual(
            result,
            [
                {"url": "https://github.com/user/repo1"},
                {"url": "https://github.com/user/repo2"},
            ],
        )

    @patch("main.build_search_url")
    async def test_missing_params(self, mock_build_search_url):
        params = {}
        with self.assertRaises(KeyError):
            await scrape(params)

    @patch("main.build_search_url")
    async def test_invalid_params(self, mock_build_search_url):
        params = {"keywords": "invalid", "proxies": "invalid", "search_type": "invalid"}
        with self.assertRaises(TypeError):
            await scrape(params)

    @patch("build_search_url")
    @patch("fetch_html")
    @patch("extract_repo_links")
    async def test_no_proxies(
        self, mock_extract_repo_links, mock_fetch_html, mock_build_search_url
    ):
        params = {"keywords": ["python", "github"], "search_type": "repository"}
        mock_build_search_url.return_value = (
            "https://github.com/search?q=python+github&type=repository"
        )
        mock_fetch_html.return_value = "<html>...</html>"
        mock_extract_repo_links.return_value = [
            "https://github.com/user/repo1",
            "https://github.com/user/repo2",
        ]

        result = await scrape(params)
        self.assertEqual(
            result,
            [
                {"url": "https://github.com/user/repo1"},
                {"url": "https://github.com/user/repo2"},
            ],
        )

    @patch("main.build_search_url")
    async def test_failed_url_building(self, mock_build_search_url):
        params = {
            "keywords": ["python", "github"],
            "proxies": ["proxy1", "proxy2"],
            "search_type": "repository",
        }
        mock_build_search_url.side_effect = Exception("Failed to build URL")

        result = await scrape(params)
        self.assertEqual(result, [])

    @patch("main.build_search_url")
    @patch("main.fetch_html")
    async def test_failed_page_fetching(self, mock_fetch_html, mock_build_search_url):
        params = {
            "keywords": ["python", "github"],
            "proxies": ["proxy1", "proxy2"],
            "search_type": "repository",
        }
        mock_build_search_url.return_value = (
            "https://github.com/search?q=python+github&type=repository"
        )
        mock_fetch_html.side_effect = Exception("Failed to fetch page")

        result = await scrape(params)
        self.assertEqual(result, [])

    @patch("main.build_search_url")
    @patch("main.fetch_html")
    @patch("main.extract_repo_links")
    async def test_empty_page_content(
        self, mock_extract_repo_links, mock_fetch_html, mock_build_search_url
    ):
        params = {
            "keywords": ["python", "github"],
            "proxies": ["proxy1", "proxy2"],
            "search_type": "repository",
        }
        mock_build_search_url.return_value = (
            "https://github.com/search?q=python+github&type=repository"
        )
        mock_fetch_html.return_value = ""
        mock_extract_repo_links.return_value = []

        result = await scrape(params)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
