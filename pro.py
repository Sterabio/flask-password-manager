import crypt
import json
import secrets
import string
import pyperclip
import os.path
import os

class acc:
    # def __init__(self):
    #     pass
    #         self.p_key = a["pk"]
    #         self.path = a["path"]
    def get(o):
        with open("settings.json", "r") as f:
            a = json.load(f)
        return a[o]        
    def list_acounts():
        arr = os.listdir("Acounts")
        for i in arr:
            i = i.replace(".json", "")
            print("-------")
            print(f"{i}")

    def view(name):
        p = acc.get("path")
        #try:
        with open(p,"rb") as f:
            a = json.load(f)
        # n = a["acounts"][name]
        # print(n)
        #for i in a["acounts"]:
        ds = {}
        for b in range(len(a["acounts"])):
            #if b ==
            #print(b)
            n = a["acounts"][b]
            #print(n)
            for i in n:
                if i == name:
                    #print(n[i])
                    x = n[i]
                    for i in x:
                        #print(x[i])
                        t = x[i]
                        t = t.encode('ISO-8859-1')
                        t = t.decode('unicode-escape').encode('ISO-8859-1')
                        t = crypt.decrypt_data(acc.get("pk"),t)
                        #print(t)
                        ds[i] = t
        return ds

    def add_dict(dict):
        print(dict)
        name = dict[0]
        print(type(name))
        name = name[1]
        d = {}
        del dict[0]
        print(dict)
        d[name] = {}
        print(name)
        for i in dict:
            v = i[1]
            
            ev = crypt.encrypt_data(v.encode())
            ev=str(ev)
            ev = ev[2:-1]
            d[name][i[0]] = ev
        #print(d)
        def write_json(data):
            with open(acc.get("path"), "w") as f:
                json.dump(data,f,indent=4)
        with open(acc.get("path"), "r+") as f:
            data = json.load(f)
            temp = data["acounts"]

            temp.append(d)
            #print(data)
            write_json(data)

    def copy(string):
        pyperclip.copy(string)
        
    def delete(name):
        def write_json(data):
            with open(acc.get("path"), "w") as f:
                json.dump(data,f,indent=4)
        with open(acc.get("path"), "r+") as f:
            data = json.load(f)
            # for b in range(len(data["acounts"])):
            n = data["acounts"]
            try:    
                for i in range(len(n)):
                    nt = (n[i])
                    print("hi")
                    print(list(nt.keys()))
                    nma = list(nt.keys())[0]
                    if nma == name:
                        #print(nma)
                        del n[i][nma]
                write_json(data)    
            except IndexError:
                print("index")
            
        try:
            acc.rcb()
        except:
            pass

    def rcb():
        def write_json(data):
            with open(acc.get("path"), "w") as f:
                json.dump(data,f,indent=4)
        with open(acc.get("path"), "r+") as f:
            data = json.load(f)
        n = data["acounts"]
        try:
            n.remove({})
        except:
            pass
        write_json(data)

    def get_password():
        password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(16)))
        pyperclip.copy(password)
        print(password)
        
    def pr(d):
        print(f"hi                     {d}")            

    def add_preset(d):
        def write_pjson(data):
            with open(".data/presets.json", "w") as f:
                json.dump(data,f,indent=4)
        with open(".data/presets.json", "r+") as f:
            data = json.load(f)
            name = d['master_name']
            # name = name[1]
            
            # temp[name] = ""

            # temp.append(d)
            print(name)
            temp = {}
            temp[name] = []
            del d['master_name']
            del d['act']
            for i in d:
                temp[name].append(i)
            print(temp)
            data.update(temp)
            print(data)
            write_pjson(data)
    def get_id():
        ids =[]
        for file in os.listdir(".data/ids/"):
            if file.endswith(".id"):
                ids.append(file.replace(".id",""))
                print(file)
        return ids