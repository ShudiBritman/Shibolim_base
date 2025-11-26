import csv
import io
import json
from insert.create_soldiers import create_all_soldiers
from fastapi import UploadFile


def load_csv(file:UploadFile):
    content = file.file.read().decode("utf-8")

    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    soldiers = create_all_soldiers(rows)
    soldiers = json.dumps(soldiers)
    return soldiers





