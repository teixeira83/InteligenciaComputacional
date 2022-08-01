import scrapy

class SoccerSpider(scrapy.Spider):
    name = 'soccer'
    start_url = 'https://ge.globo.com/'
    start_urls = [start_url]
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)
    
    def parse(self, response): 
        serie_a = response.xpath('//div[@id="Série A"]/div/div/a/@title').extract()
        serie_b = response.xpath('//div[@id="Série B"]/div/div/a/@title').extract()
        
        #como sao 20 times em cada divisao 
        #foi utilizado a quantidade de times para percorrer todos os
        #elementos encontrados no site
        for i in range(20):
            yield {
                'times da serie A': serie_a[i],
                'times da serie B': serie_b[i]
            }