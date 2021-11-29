#!/usr/bin/env python
# encoding: utf-8
import json

def jsonify(x):
    return x

def query_records(name):
    print(name)
    with open('./data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            #print("type record", type(record))
            #print("type of name", type(name))
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

def create_record(record):
    with open('./data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('./data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

def update_record(record):
    new_records = []
    with open('./data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('./data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
def delete_record(record):
    new_records = []
    with open('./data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('./data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

#query_records("alice")
new_record = {"name": "satya", "email": "satya@patch.com"}
#create_record(new_record)
#update_record(new_record)
#delete_record(new_record)
#query_records("satya")
