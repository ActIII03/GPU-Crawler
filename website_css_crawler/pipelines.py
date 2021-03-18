# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import pdb
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter


class JsonWriterPipeline:

    file = None

    def open_spider(self, spider):
        self.file = open('items.json', 'w+b')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting() 
        self.file.close()

    def process_item(self, item, spider):
        for i in range(0, len(item)):
            self.exporter.export_item(item[i])
        return item

