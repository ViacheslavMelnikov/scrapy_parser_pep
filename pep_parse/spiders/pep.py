import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        rows_scrapy = response.xpath(
            '//*[@id="numerical-index"]').css('tbody').css('tr')
        for row in rows_scrapy:
            link_pep = row.css('td')[1].css('a::attr(href)').get()
            yield response.follow(link_pep, callback=self.parse_pep)

    def parse_pep(self, response):
        num_pep = int(
            response.css('header').css('li+li+li::text').get().split()[1])
        data = {
            'number': num_pep,
            'name': response.css('h1.page-title::text').get().split(' – ')[1],
            'status': response.css(
                'dt:contains("Status")+dd').css('abbr::text').get(),
        }
        yield PepParseItem(data)
