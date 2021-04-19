import csv
import pandas as pd
import io

def threetier_convert(csv_file, outdir):
    # lines = csv.reader(csv_file, delimiter=',', quotechar='"', skipinitialspace=True)

    # t = """id;value
    # 0;123,123
    # 1;221,323,330
    # 2;32,001"""
    # pd.read_csv(io.StringIO(t)
    trainingSet = pd.read_csv('data/'+csv_file, thousands=',', sep=',', encoding="UTF8", quotechar='"', skipinitialspace=True)

    trainingSet.to_csv(outdir +"/"+csv_file)