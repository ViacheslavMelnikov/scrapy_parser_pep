from itemadapter import ItemAdapter
import csv
import datetime


class PepParsePipeline:
    def process_item(self, item, spider):
        return item


class PepToCsvPipeline:
    def open_spider(self, spider):
        self.rezult = {}

    def process_item(self, item, spider):
        a = item['status']
        self.rezult.setdefault(a,0)
        self.rezult[a] += 1
        return item 

    def close_spider(self, spider):
        self.rezult=dict(sorted(self.rezult.items()))
        self.rezult['Total'] = sum(self.rezult.values())
        date_now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        name_file = f'results/status_summary_{date_now}.csv'
        with open(name_file, 'w', newline='') as output_file:
            fieldnames = ['Статус', 'Количество']
            dict_writer = csv.DictWriter(output_file, fieldnames)
            dict_writer.writeheader()
            for key in self.rezult.keys():
                dict_writer.writerow({'Статус':key, 'Количество': self.rezult[key]})