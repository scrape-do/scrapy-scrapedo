
from scrapydo import scrapy, scrapedo


class ScrapedoSampleCrawler(scrapy.Spider):
    name = "Scrape-do Sample Crawler"
    def __init__(self):
        super().__init__(scrapedo.RequestParameters(
        token="TOKEN", # Get your Scrape.do token from: dashboard.scrape.do
        params={
            "geoCode":"us",
            "super":False,
            "render":True,
            "playWithBrowser":[{"Action":"Click","Selector":"#manpage > div.mp > ul > li:nth-child(3) > a"},{"Action":"Wait","Timeout":2000},{"Action":"Execute","Execute":"document.URL"}],
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
        
    
        
