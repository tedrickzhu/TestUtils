#encoding = utf-8

import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
testjson = open('/home/zzy/Documents/document4.json')

test = json.load(testjson)

print test["casefolder"]