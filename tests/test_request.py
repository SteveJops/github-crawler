from global_imports import httpx, pytest
from unittest.mock import Mock, patch
from fetch_page import fetch_html  # replace 'your_module' with the actual module name


@pytest.mark.asyncio
async def test_fetch_html_success():
    client = httpx.AsyncClient()
    url = "https://www.example.com"
    proxy = "http://myproxy:8080"

    with patch.object(client, "get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html>Hello World!</html>"
        mock_get.return_value = mock_response

        result = await fetch_html(client, url, proxy)
        assert result == "<html>Hello World!</html>"


@pytest.mark.asyncio
async def test_fetch_html_invalid_url():
    client = httpx.AsyncClient()
    url = " invalid_url"
    proxy = "http://myproxy:8080"

    with patch.object(client, "get") as mock_get:
        mock_get.side_effect = httpx.InvalidURL("Invalid URL")

        result = await fetch_html(client, url, proxy)
        assert result == ""


@pytest.mark.asyncio
async def test_fetch_html_invalid_proxy():
    client = httpx.AsyncClient()
    url = "https://www.example.com"
    proxy = " invalid_proxy"

    with patch.object(client, "get") as mock_get:
        mock_get.side_effect = httpx.ProxyError("Invalid proxy")

        result = await fetch_html(client, url, proxy)
        assert result == ""


@pytest.mark.asyncio
async def test_fetch_html_timeout():
    client = httpx.AsyncClient()
    url = "https://www.example.com"
    proxy = "http://myproxy:8080"

    with patch.object(client, "get") as mock_get:
        mock_get.side_effect = httpx.TimeoutException("Timeout")

        result = await fetch_html(client, url, proxy)
        assert result == ""


@pytest.mark.asyncio
async def test_fetch_html_exception():
    client = httpx.AsyncClient()
    url = "https://www.example.com"
    proxy = "http://myproxy:8080"

    with patch.object(client, "get") as mock_get:
        mock_get.side_effect = Exception("Unexpected error")

        result = await fetch_html(client, url, proxy)
        assert result == ""
