# 🕷️ test-task-crawler

**GitHub Scraper with Proxy Support** – a fast, asynchronous CLI tool for scraping GitHub repository links from search results, built with `httpx`, `bs4`, and full proxy rotation support.

---

## 🚀 Features

- 🔍 Scrape GitHub search results for repositories, issues, or wikis  
- 🌐 Rotating proxy support to avoid rate limits  
- ⚡ Asynchronous HTTP requests with `httpx`  
- 📄 Supports both CLI arguments and JSON config files  
- 🧪 Comes with `pytest` and `unittest` test suite  

---

## 📦 Tech Stack

- Python 3.11.9  
- [httpx](https://www.python-httpx.org/) – asynchronous HTTP client  
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing  
- argparse, asyncio, json  
- Testing: `pytest`, `unittest`

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/SteveJops/test-task-crawler.git
cd test-task-crawler

# Install dependencies using Poetry
poetry install
```

## 🛠️ Usage
You can run the scraper either by passing arguments directly in the CLI or by supplying a JSON config file.

✅ CLI Mode

```bash
poetry run python main.py \
  --keywords github scraper \
  --search-type repository \
  --proxies 13.40.3.184:3128 40.76.69.94:8080
```

Then run:
```bash
poetry run python main.py --config path/to/config.json
```

## 🧠 Command-Line Arguments

| Flag                  | Description                                     | Example                               |
| --------------------- | ----------------------------------------------- | ------------------------------------- |
| `-k`, `--keywords`    | Keywords to search for                          | `--keywords github crawler`           |
| `-t`, `--search-type` | Type of search: `repository`, `issues`, `wikis` | `--search-type repository`            |
| `-p`, `--proxies`     | List of proxies to rotate through               | `--proxies 1.2.3.4:8080 5.6.7.8:3128` |
| `-c`, `--config`      | Path to a JSON config file                      | `--config ./config.json`              |

## 🧪 Running Tests

```bash
# Run all tests with pytest
poetry run pytest

# Or use built-in unittest
poetry run python -m unittest discover
```

## ⚙️ Default Config (Hardcoded)

```bash 
configs = {
    "GITHUB_SEARCH_URL": "https://github.com/search",
    "search_type": (
        "repository",
        "issues",
        "wikis",
    ),
    "proxies_config": {
        "proxy_1": "13.40.3.184:3128",
        "proxy_2": "13.40.152.64:3128",
        "proxy_3": "40.76.69.94:8080",
        "proxy_4": "18.175.118.106:999",
        "proxy_5": "52.194.186.70:1080",
        "proxy_6": "52.11.48.124:3128",
        "proxy_7": "3.10.207.94:4222",
        "proxy_8": "13.40.85.163:999",
        "proxy_9": "18.132.36.51:3128",
        "proxy_10": "99.79.124.70:80",
        "proxy_11": "123.18.118.89:8080",
        "proxy_12": "47.251.122.81:8888",
        "proxy_13": "54.184.124.175:14581",
        "proxy_14": "65.108.159.129:8081",
        "proxy_15": "159.65.245.255:80"
    }
}
```

## 👤 Author
Created by SteveJops(https://github.com/SteveJops)