import json
#This is the user and password for my Project 2 instance
from neo4j import GraphDatabase
# graph.py
from auth import AUTH

# ... your code using username and password ...

with GraphDatabase.driver("neo4j://127.0.0.1:7687", auth=AUTH) as driver:
    driver.verify_connectivity()

#this opens the files and gathers data from the downloads. 
with open(r'sedac_downloads_1st_week 1.jsonl', 'r', encoding='utf-16') as f:
        i = 1
        for line in f:
            print(line)
            download = json.loads(line)
            user_id = download['user_id']
            file_name = download['message']['download']['object']
            file_size = download['message']['download']['size']
            #file_range = download['message']['download']['range']
            file_range = True
            if download['message']['download']['range'] == 'None':
                file_range = False     
            print(f'{i} user: {user_id} name: {file_name} range: {file_range}') 
            i = i + 1
            summary = driver.execute_query("""
                MERGE (a:User {id: $userId})
                MERGE (b:File {filename: $fileName, filerange: $fileRange})
                MERGE (a)-[r:DOWNLOADED]->(b)
                ON CREATE SET r.times = 1, r.fileRange = $fileRange
                ON MATCH SET r.times = r.times + 1, r.fileRange = $fileRange   
                """,
                userId=user_id, fileName=file_name, fileRange=file_range,
    database_="neo4j",
).summary
            