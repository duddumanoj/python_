#reading from json file which is of the form [{"a":"s"},{"d":"r"}] and storing that file key-value pairs in dictionary c(i.e,c={})
import json
import os
d=["id","title","link","description","long_description","alt_titles","brand","tags","entities"]
CWD=os.getcwd()
JSON_CONFIG_FILE_PATH='%s/%s'%(CWD,'js.json')
c={}
try:
    with open(JSON_CONFIG_FILE_PATH)as data_file:
        c=json.load(data_file)

except IOError as e:
    print (e)
    exit(1)
print (c)



