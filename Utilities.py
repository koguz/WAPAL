import csv
import pickle

def save_list_as_csv(mylist:list, fname:str, d=','):
    with open(fname, 'w', newline='') as csvfile:
        sw = csv.writer(csvfile, delimiter=d)
        for row in mylist:
            sw.writerow(row)

