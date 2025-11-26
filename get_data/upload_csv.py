import csv
import io
from insert.create_soldiers import create_all_soldiers


def load_csv(file):
    content = file.file.read().decode("utf-8")

    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    soldiers = create_all_soldiers(rows)





