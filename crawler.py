import scrapy
import os
import sys
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
    def run_spiders(self) -> "None":
        self.process.crawl(self.spiders[0])
        self.process.start()
# Main driver of application that intakes phone number as argv
def main() -> "None":
    # Intake desired phone number
    phone_number = sys.argv[1]
    if(phone_number == None):
        print("Please provide desired phone number via docker-compose's cmd argv\n")
        print("Example: python3 crawler.py <phone_number\n")
        quit()
    # Scrape ecommerce website(s) for GPU data
    gpu_crawler = GPUCrawler()
    gpu_crawler.run_spiders()
    # Wrangle data for textfile and notify via SMS
    not_sys = notification.NotificationSys()
    not_sys.run(phone_number)

if __name__=="__main__":
    main()
    exit()

