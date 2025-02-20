import os
import csv

"""
I used this code for removing the first line in every file' sunce it was problematic
"""

def add_columns(input_file, output_file, column_names, values):
	with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
		reader = csv.reader(infile, delimiter="\t")
		writer = csv.writer(outfile, delimiter="\t")

    # Write the header row   
		header = next(reader)
		header.extend(column_names)
		writer.writerow(header)

    # Write the data rows with the new column value
		for row in reader:
			row.extend(values)
			writer.writerow(row)
import csv

def delete_first_row(input_file, output_file):
	with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
		reader = csv.reader(infile)
		writer = csv.writer(outfile)
	# Skip the first row
		next(reader)

	# Write the remaining rows to the output file
		for row in reader:
			writer.writerow(row)
lst=[]
meta = open(r"/path/to/metadata.txt","r")
rd = csv.DictReader(meta, delimiter="\t", quotechar='"')
for row in rd:
	#if "BMC" in row["Sample"] or "CHTN" in row["Sample"]:
		#add_columns("/path/to/old-data-folder/"+row["Sample"]+".tsv","/path/to/new-data-folder/"+row["Sample"]+".tsv", ["hasCancer"],["False"])
	#else:
		#add_columns("/path/to/old-data-folder/"+row["Sample"]+".tsv","/path/to/new-data-folder/"+row["Sample"]+".tsv", ["hasCancer","Age (Range)","Gender","Diagnosis","Smoke Years","Tissue Source","Disease Stage"],["True",row["Age (Range)"],row["Gender"],row["Diagnosis"],row["Smoke Years"],row["Tissue Source"],row["Disease Stage"]])1
	delete_first_row("/path/to/old-data-folder/"+row["Sample"]+".tsv","/path/to/new-data-folder/"+row["Sample"]+".tsv")
meta.close()
print(lst)
