import scrapy
import pdb
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from website_css_crawler.spiders.bestbuy import *

class GPUCrawler:
    # Copy-Constructor
    def __init__(self):
        # breakpoint()
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
        for site in range(0, 1):
            self.process.crawl(self.spiders[site])
            self.process.start()

def main():

    # Scrape website for url links to IN-STOCK GPUs'
    gpu_crawler = GPUCrawler()
    gpu_crawler.run_spiders()

if __name__=="__main__":
    main()
    exit()
