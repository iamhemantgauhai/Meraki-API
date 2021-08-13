
import requests,json
from pprint import pprint
url = "http://saral.navgurukul.org/api/courses"
re = requests.get(url)
b=re.json()
list1=[]
list2=[]
for i in b:
    k=1
    for j in b[i]:
        hh=str(k)+". "+j["name"]
        k+=1
        list1.append(hh)
        list2.append(j["id"])
        print(hh)
pp = int(input("enter input - select your course    :     "))
pp -= 1
ids = list2[pp]
req = requests.get("http://saral.navgurukul.org/api/courses/"+ids+"/exercises")
w = req.text
war = json.loads(w)
data_d = war["data"]
num = 1
list3 = []
for j in data_d:
    int_slugs="http://saral.navgurukul.org/api/courses/"+(ids)+"/exercise/getBySlug?slug="+j['slug']
    v = str(num)
    dr= v+"."+j['name']
    num=int(num)
    print (dr)
    dict = {v:int_slugs}
    list3.append(dict)
    j=j['childExercises']
    num1=1
    for k in j:
        z=str(num)+'.'+str(num1)
        print('          '+z, k['name']  )
        float_slugs="http://saral.navgurukul.org/api/courses/"+(ids)+"/exercise/getBySlug?slug="+k['slug']
        dic={z:float_slugs}
        list3.append(dic)
        num1+=1
    num+=1
k = input("enter the question no    :  ")
for h in list3:
    for j,f in h.items():
        if str(j) == k:
            s = requests.get(f).text
            d = json.loads(s)
            hh = d["content"]
            bb = json.loads(hh)
            for u in bb:
                print(u["value"])