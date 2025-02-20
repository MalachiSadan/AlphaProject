import csv
import os

"""
code used for creating the metadata file
"""
dir = r"/path/to/data"
tsv = open(r"/path/to/data/metadata.txt", "w")
wrt = csv.writer(tsv, delimiter="\t")
def indexer(lst, param):
        for i in lst:
                if param in i:
                        return lst.index(i)
        raise Error(param + " Is not in the list")
def rindexer(lst, param):
        return indexer(lst[::-1], param)
for filnm in os.scandir(dir):
	print(filnm.name[:-4])
	with open(os.path.join(dir,filnm)) as fd:
		rd = csv.DictReader(fd, delimiter="\t", quotechar='"')
		for row in rd:
                        txt = row["sample_tags"]
                        splt = txt.split(",")
                        try:
                                lst = [filnm.name[:-4]]
                                try:
                                        lst.append(splt[indexer(splt, "Age (Range)")][12:])
                                except:
                                        lst.append(r"N\A")
                                try:
                                        lst.append(splt[indexer(splt, "Biological Sex")][15:])
                                except:
                                        lst.append(r"N\A")
                                try:
                                        lst.append(splt[indexer(splt, "Diagnosis")][10:])
                                        lst.append("hasCancer")
                                except:
                                        lst.append(r"N\A")
                                        lst.append("noCancer")
                                try:
                                        lst.append(splt[indexer(splt, "Smoking Status")][15:])
                                except:
                                        lst.append(r"N\A")
                                try:
                                        lst.append(splt[indexer(splt, "Tissue Source")][14:])
                                except:
                                        lst.append(r"N\A")
                                try:
                                        lst.append(splt[indexer(splt, "stage")][12:])
                                except:
                                        lst.append(r"N\A")
                                wrt.writerow(lst)
                        finally:
                                break
tsv.close()
