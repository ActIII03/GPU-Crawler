import scrapy
import logging

class InstockGPU(scrapy.Spider):
    name = "BestBuyGPU"
    base_url = 'https://api.bestbuy.com/click/~/'
    start_urls = [
            'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%202060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%202080%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DG',
    ]
    def __init__(self):
        self.count = 0
        self.page_number = 0
    # Scrape Bestbuy's GPU page
    def parse(self, response):
        logger = logging.getLogger('mycustomlogger')
        yield self.parse_listing(response)
        next_page = response.css('a.sku-list-page-next::attr(href)').get()
        logger.info("Getting information from: %s", next_page)
        if next_page is not None:
            yield scrapy.Request(url=next_page, callback=self.parse_listing, dont_filter=True)           
            del(next_page)
    # Parse individual listings for: (i) title (ii) sku (iii) price (iv) in-stock (bool) (v) item-info URL
    def parse_listing(self, response):
        item_list = response.css('ol.sku-item-list .sku-item')
        found_items = {}
        num_item = len(response.css('div.sku-title h4.sku-header a::text').getall())
        index = 0
        while index <= num_item - 1:
            item = {
                'title': item_list[index].css('div.sku-title h4.sku-header a::text').get(),
                'sku': item_list[index].css('div.sku-attribute-title span.sku-value::text').extract()[1],
                'price':  item_list.css('div.priceView-hero-price.priceView-customer-price span::text').extract()[0],
                'in-stock': False,
                'sku': self.base_url + item_list[index].css('div.sku-attribute-title span.sku-value::text').extract()[1] + "/cart",
            }
            # Check if stock
            if(item_list.css('button.btn::text').get()[1] == "Sold Out"):
               item['in-stock'] = True
            found_items[self.count] = item
            index += 1
            self.count += 1
        return found_items
