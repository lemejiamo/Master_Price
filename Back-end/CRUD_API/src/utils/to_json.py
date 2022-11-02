from json import dumps
from datetime import datetime
import os
import csv


def to_json():
    files_csv = os.listdir("./docs/")
    for doc in files_csv:
        doc_path = "./docs/"+doc
        with open(doc_path, 'r') as csv_doc:
            index = 1
            reader = csv.DictReader(csv_doc)
        data = {}
        for row in reader:
            date = datetime.now()
            row['date_load'] = date.strftime("%m/%d/%Y, %H:%M:%S:%f")
            row['date_update'] = row['date_load']
            data[index] = row
            index = index + 1

        json_file = doc[:-4]+".json"
        with open(json_file, "w") as json:
            json.write(dumps(data, indent=4))

