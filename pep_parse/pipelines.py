import csv
import datetime
from collections import defaultdict

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_summary_dict = defaultdict(int)

    def process_item(self, item, spider):
        self.status_summary_dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.status_summary_dict['Total'] = sum(
            self.status_summary_dict.values())

        date_now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        name_file = f'{BASE_DIR}/results/status_summary_{date_now}.csv'
        with open(name_file, 'w', newline='') as output_file:
            fieldnames = ['Статус', 'Количество']
            dict_writer = csv.DictWriter(output_file, fieldnames)
            dict_writer.writeheader()
            dict_writer.writerows(
                [
                    {'Статус': key,
                     'Количество': value
                     } for key, value in self.status_summary_dict.items()])
