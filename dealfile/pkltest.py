import cPickle as pickle
class people:
    id = 0
    name='y'
    def add(self):
        self.id+=1
        self.name="yang"
#man = people()
#print man.name
kk = [people(), people()]
kk[1].add()
#print man.name
with open('test.txt','wb') as f:
    pickle.dump(kk, f)
fid = open('test.txt')
temp = pickle.load(fid)
fid.close()
print temp[1].name
print temp[0].name