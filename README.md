# Scrapydo

Scrapy wrapper for running Scrapy spiders with Scrapedo API.

## Install

```bash
# get it from github
pip3 install git+https://github.com/scrape-do/scrapy-scrapedo

# or from pypi
pip3 install scrapy-scrapedo
```

## Usage

```python

from scrapydo import scrapy, scrapedo


class ScrapedoSampleCrawler(scrapy.Spider):
    name = "Scrape-do Sample Crawler"
    def __init__(self):
        super().__init__(scrapedo.RequestParameters(
        token="TOKEN", # Get your Scrape.do token from: dashboard.scrape.do
        params={
            "geoCode":"us",
            "super":False,
            "render":True, #don't forget to delete playWithBrowser parameters if you don't want to use render feature
            "playWithBrowser":[
                {"Action":"Click","Selector":"#manpage > div.mp > ul > li:nth-child(3) > a"},
                {"Action":"Wait","Timeout":2000},
                {"Action":"Execute","Execute":"document.URL"}
            ],
        }))
        
    def start_requests(self):
        urls = [
            'https://httpbin.co/',
        ]
        
        for url in urls:
            yield self.Request(url=url, callback=self.parse)
    def parse(self, response):
        print(response.body)
        print("target:",self.target_url(response))
            
````

You can also use the proxy mode to use the Scrape.do proxy service.

```python


from scrapydo import scrapy, scrapedo

class ScrapedoSampleCrawler(scrapy.Spider):
    name = "Scrape-do Sample Crawler"
    def __init__(self):
        super().__init__(scrapedo.RequestParameters(
        token="TOKEN", # Get your Scrape.do token from: dashboard.scrape.do
        params={
            "geoCode":"uk",
            "super":True,
        },
        proxy_mode=True,
        ))
    
    def start_requests(self):
        urls = [
            'https://httpbin.co/headers',
        ]
        
        for url in urls:
            yield self.Request(url=url, callback=self.parse)
    def parse(self, response):
        print(response.body)
        print("target:",self.target_url(response))
        
    

```
## Build

You may prefer to build the package from source code.

```bash

pip3 install setuptools wheel
python3 setup.py sdist bdist_wheel

```

Finally, you can install the package from the generated wheel file.

```bash
pip3 install dist/scrapy_scrapedo-0.1.4-py3-none-any.whl
```