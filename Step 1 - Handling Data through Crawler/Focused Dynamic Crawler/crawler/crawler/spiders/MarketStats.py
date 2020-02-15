import scrapy
from scrapy_splash import SplashRequest

class MarketstatsSpider(scrapy.Spider):
    name = 'MarketStats'
    allowed_domains = ['www.economictimes.indiatimes.com']

    def start_requests(self):
        urls = [
            'https://economictimes.indiatimes.com/marketstats/pageno-1,pid-59,sortby-currentYearRank,sortorder-asc,year-2018.cms',
            'https://economictimes.indiatimes.com/marketstats/pid-58,pageno-1,year-2017,sortorder-asc,sortby-CurrentYearRank.cms',
            'https://economictimes.indiatimes.com/marketstats/pid-57,pageno-1,year-2016,sortorder-asc,sortby-CurrentYearRank.cms',
            'https://economictimes.indiatimes.com/marketstats/pid-56,pageno-1,year-2015,sortorder-asc,sortby-CurrentYearRank.cms',
            'https://economictimes.indiatimes.com/marketstats/pid-55,pageno-1,year-2014,sortorder-asc,sortby-CurrentYearRank.cms',
        ]
        for url in urls:
            yield SplashRequest(url, self.parse, args={'wait': 3})

    def parse(self, response):
        for stats in response.xpath("//div[@class='dataList']"):
            yield {
                'Rank': stats.css(".dataList ul>li:nth-child(n+1)::text").extract_first(),
                'Company': stats.css(".dataList ul>li:nth-child(n+3)>a::text").extract_first(),
                'Revenue': stats.css(".dataList ul>li:nth-child(n+4)::text").extract_first(),
                'PAT': stats.css(".dataList ul>li:nth-child(n+6)::text").extract_first(),
                'MCAP': stats.css(".dataList ul>li:nth-child(n+8)::text").extract_first(),
            }
