# Program: GPU-Crawler
Description: Crawl ecommerce websites to check 30XX RTX GPU's are instock (Eventually)

## Dependencies
1. selenium 3.5 
2. WebDriver: https://github.com/mozilla/geckodriver/releases ; Version: https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux32.tar.gz
3. Scrapy 2.4

## Steps to run:
1. <code>git clone https://github.com/ActIII03/GPU-Crawler </code>
2. <code> sudo docker-compose up </code>

## To-do List:
1. bestbuy.py - scrape add-to-cart url when not "Sold Out"
2. implement method to check if in-stock == true for every item in items.json, add to list of stocked to prep for text message 
3. Add text message capability with add-cart option 
