# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ReportPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('reports.db')
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("""drop table if exists reports""")
        self.curr.execute("""create table reports(
                            title text,
                            category text,
                            subcategory text,
                            datetime text,
                            link text,
                            image text,
                            content text
                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into reports values(?,?,?,?,?,?,?)""",
                          (item['title'][0],
                           item['category'][0],
                           item['subcategory'][0],
                           item['datetime'][0],
                           item['link'],
                           item['image'][0],
                           " ".join([item['content'][i] for i in range(len(item['content']))])))
        self.conn.commit()
