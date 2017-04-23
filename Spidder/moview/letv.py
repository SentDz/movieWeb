import urllib2
import json
from pymongo import MongoClient

base_url = "http://list.le.com/apin/chandata.json?c=1&d=1&md=&o=17&s=1&p="
count = 22
index = 1
client = MongoClient('127.0.0.1', 27017)
db_name = 'assest'
db = client[db_name]
letv = db['letv']

while(index <= count):
    url = base_url + str(index)
    index += 1
    response = urllib2.urlopen(url)
    bc = response.read()
    j = json.loads(bc)
    for a in j['data_list']:
        name =  a['name']
        print name
        description = a['description']
        tag = a['tag']
        duration = a['duration']
        ispay = a['ispay']
        subCategoryName = a['subCategoryName']
        category = a['category']
        area = a['area']
        aid = a['aid']
        vids = a['vids']
        videoTypeName = a['videoTypeName']
        images = a['images']
        lgName = a['lgName']
        directory = a['directory']
        obj = {"name":name,"description":description,"tag":tag,"duration":duration,"ispay":ispay,"subCategoryName":subCategoryName,
               "category":category,"area":area,"aid":aid,"vids":vids,"videoTypeName":videoTypeName,"lgName":lgName,"directory":directory,"images":images}
        letv.insert(obj)
