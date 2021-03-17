# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter


class JsonWriterPipeline:

    def open_spider(self, InstockGPU):
        self.file = open('items.json', 'w')

    def close_spider(self, InstockGPU):
        self.file.close()

    def process_item(self, item, InstockGPU):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item

