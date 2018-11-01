#encoding = utf-8

import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
jsonfile = open("/home/zzy/Documents/BioASQ-trainingDataset5b.json")
filequery = open('/home/zzy/Documents/4queryargs.txt', 'w+')
filedocument = open('/home/zzy/Documents/document4.json', 'w')

jsonstring = json.load(jsonfile)
question = jsonstring["questions"]

number2_zero = 'zhuzhengyi'
relative_one = 'zhuyuanzhang'
queries =[]

ques_ele_nums = len(question)
for i in range(ques_ele_nums):
    question_ele = question[i]
    qid = question_ele["id"]
    snipp_ele_nums = len(question_ele["snippets"])
    for j in range(snipp_ele_nums):
        snippet_ele = question_ele["snippets"][j]
        documentid = str(snippet_ele["document"]).split('/')[-1]
        text = str(snippet_ele["text"])
        filequery.write(str(qid)+","+number2_zero+","+documentid+","+relative_one+"\n")
        queries_ele = {"number":documentid,"text":text}
        queries.append(queries_ele)

documentstring = {"casefolder":"true","queries":queries}
print type(documentstring)
# print documentstring
# with open("/home/zzy/Documents/document5.json","w") as f:
#     json.dump(documentstring,f)
documentjson = json.dump(documentstring,filedocument)
#filedocument.write(str(documentstring))

print question[0]["id"]
print str(question[0]["snippets"][0]["document"]).split('/')[-1]
print question[0]["snippets"][0]["text"]

jsonfile.close()
filequery.close()
filedocument.close()


