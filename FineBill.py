import os
import csv


def get_files(path: str) -> list:
    file_list = list()
    for file_name in os.listdir(path):
        if file_name.endswith(".csv"):
            file_list.append(file_name)
    return file_list


def merge_file(file_list: list):
    started = False
    for file_name in file_list:
        with open(f'./ZiCeBill/{file_name}', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            with open('FineBill.csv', 'a') as new_file:
                field_names = ['账目', '金额', '日期']
                csv_writer = csv.DictWriter(new_file, fieldnames=field_names)
                if not started:
                    csv_writer.writeheader()
                    started = True
                for line in csv_reader:
                    if not('总和' in line['账目']) and (line['类型'] == '迟到') and not(line['账目'] == ''):
                        del line['类型']
                        del line['结余']
                        del line['备注']
                        line['日期'] = ''.join(line['日期'].split('/'))
                        csv_writer.writerow(line)


class MyBill(object):
    def __init__(self, path: str):
        self.path = path
        self.bill_list = list()
        self.load_csv()
        self.total_dict = dict()
        self.get_total()
        print(self.total_dict)

    def load_csv(self):
        with open(self.path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                self.bill_list.append(line)

    @staticmethod
    def get_date(bill_dict: dict):
        return int(bill_dict['日期'])

    def csv_sorted_date(self):
        self.bill_list.sort(key=self.get_date)
        with open('FineBillByDate.csv', 'w') as new_file:
            field_names = ['账目', '金额', '日期']
            csv_writer = csv.DictWriter(new_file, fieldnames=field_names)
            csv_writer.writeheader()
            for line in self.bill_list:
                csv_writer.writerow(line)

    def get_total(self):
        for ppl in self.bill_list:
            if ppl['账目'] not in self.total_dict:
                self.total_dict[ppl['账目']] = int(float(ppl['金额']))
            else:
                self.total_dict[ppl['账目']] += int(float(ppl['金额']))

    def csv_sorted_total(self):
        sorted_list = list()
        for name in self.total_dict:
            sorted_list.append([name, self.total_dict[name]])
        sorted_list.sort(key=lambda x: x[1])
        with open('FineBillByTotal.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file)
            for line in sorted_list:
                csv_writer.writerow(line)


if __name__ == "__main__":
    # files = get_files("/Users/mac/Desktop/learning/ZiCeBill")
    # merge_file(files)
    a = MyBill('FineBill.csv')
    a.csv_sorted_date()
    a.csv_sorted_total()
