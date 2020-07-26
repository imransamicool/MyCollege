import csv, os
from MyCollege.config import FILE_PATH


def check_id(id_s):
    with open(FILE_PATH, mode='r', encoding='utf-8') as f:
        csv_row = csv.DictReader(f)
        for row in csv_row:
            flag = (True if int(row['Id']) == id_s else False)
            return flag


def age_check(age):
    if age < 8:
        return True
    else:
        return False


def add_to_csv(stud_dict):
    with open(FILE_PATH, 'a', encoding='utf-8', newline="") as fw:
        #csv_wr = csv.DictWriter(fw, fieldnames=stud_dict.keys())
        #csv_wr.writeheader()
        csv_wr = csv.DictWriter(fw, fieldnames=stud_dict.keys())
        csv_w = csv.writer(fw)
        header = ['Id', 'Name', 'Age', 'Subjects']
        #csv_rd = csv.reader(fw)
        if os.stat(FILE_PATH).st_size == 0:
            csv_w.writerow(header)
            csv_wr.writerow(stud_dict)
            return True
        else:
            csv_wr.writerow(stud_dict)
            return True


def fetch_print_csv():
    with open(FILE_PATH, 'r', encoding='utf-8') as fr:
        csv_rdr = csv.reader(fr)
        for dr in csv_rdr:
            print(dr)
