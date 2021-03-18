import scrapy
import os
import pdb
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from website_css_crawler.spiders.bestbuy import *
from utils import notification

class GPUCrawler:
    # Copy-Constructor
    def __init__(self):
        settings_file_path = "website_css_crawler.settings"
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        self.spiders = [ 
                InstockGPU,
        ]
        self.spider_count = 1

    # Run list of spiders
    def run_spiders(self):
        #breakpoint()
        self.process.crawl(self.spiders[0])
        self.process.start()

# Main driver of application
def main():

    # Scrape ecommerce website(s) for GPU data
    gpu_crawler = GPUCrawler()
    gpu_crawler.run_spiders()
    # Clean data and notify 
    not_sys = notification.NotificationSys()
    not_sys.run()


if __name__=="__main__":
    main()
    exit()
