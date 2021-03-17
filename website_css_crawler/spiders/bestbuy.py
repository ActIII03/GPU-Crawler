import scrapy
import pdb
import logging
from scrapy.http import Request

class InstockGPU(scrapy.Spider):
    name = "BestBuyGPU"
    start_urls = [
            'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%202060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%202080%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DG',
    ]

    def __init__(self):
        self.count = 0

    def parse(self, response):
        logger = logging.getLogger('mycustomlogger')
        item_list = response.css('ol.sku-item-list .sku-item')       
        num_item = len(response.css('div.sku-title h4.sku-header a::text').getall())
        while self.count < num_item - 1:
            self.count += 1
            item = {
                'title': item_list[self.count].css('div.sku-title h4.sku-header a::text').get(),
                'sku': item_list[self.count].css('div.sku-attribute-title span.sku-value::text').extract()[1],
                'price':  item_list.css('div.priceView-hero-price.priceView-customer-price span::text').extract()[0],
                'in-stock': False,
            }
            # Check if stock
            if(item_list.css('button.btn::text').get()[1] == "Sold Out"):
               item['in-stock'] = True

            yield item

        next_page = response.css('li.page-item a.trans-button.page-number::attr(href)').get()
        if next_page is not None:
           yield Request(next_page, callback=self.parse)           

