import jsonlines

# Reading a JSONL file
with jsonlines.open('sedac_downloads_1st_week 1.jsonl') as reader:
    for obj in reader:
        print(obj)

# Alternatively, handle potential errors:
with jsonlines.open('sedac_downloads_1st_week 1.jsonl', broken=True) as reader: # Skips broken lines
    for obj in reader:
        print(obj)

# This code reads and handles errors within the code. 
