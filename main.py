from re import S
from flask import Flask, request
from flask import render_template
import json
import os
import crypt
from dataclasses import dataclass

from werkzeug.utils import redirect
from pro import acc 

class settings:
    def get(o):
        with open("settings.json", "r") as f:
            a = json.load(f)
        print(a[o])
        return a[o]
    def edit(a,b):
        spath = "settings.json"
        def write_json(data):
            with open(spath, "w") as f:
                json.dump(data,f,indent=4)
        with open(spath, "r+") as f:
            data = json.load(f)
            data[a] = b
            #data = data.update(temp)
        write_json(data)
    pk = get("pk")
    id = get("id")
    path = f".data/ids/{id}.id"
#settings.edit("pk","testp")  
# 
@dataclass()
class stns:
    pk:str
    id:str
    path:str 
id = acc.get("id")
test = stns(settings.pk,settings.id,f".data/ids/{id}.id" )

print(test.pk)
settings.get("pk")

#a = pa("dan","pkt/privkey.key")
def ac():
    print(acc)
ac()
#get presets
presets = []
def get_presets():
    
    with open(".data/presets.json", "r") as f:
            a = json.load(f)
    for i in a:
        presets.append(i)

acounts = []
get_presets()

def get_acounts():
    try:
        acounts.clear()
        with open(test.path, "r") as f:
            a = json.load(f)
            a = a["acounts"]
            for i in a:
                for i in i:
                    acounts.append(i)
    except:
        pass
get_acounts()    




app = Flask(__name__)
data = ["hi","hello","yandex"]
@app.route("/",methods=["GET","POST"])
def home():
    get_acounts() 
    return render_template("index.html",acounts=acounts, presets = presets)

@app.route("/hh/")
def neww():
    return render_template("dd.html",data = presets )




@app.route("/new-acount/")
def new():
    
    return render_template("new-acount.html",data = data)




@app.route("/view/")
def view():
    acounts = []
    with open(test.path, "rb") as f:
        a = json.load(f)

        a = a["acounts"]#[1]
        # for i in range(len(a)):
        #     print("a")
        # print(len(a))
        # print(type(a))
        # print(a)
        # print('')
        for i in a:
            for i in i:
                acounts.append(i)
        print(acounts)
    return render_template("view.html", acounts=acounts, presets = presets)



@app.route("/view/<name>/", methods=["GET","POST"])
def decrypt(name):
    
    nd = acc.view(name)

    
    if request.method == ["GET", "POST"]:
        print("hii")
    
    if request.method == "POST":
        req = request.form
        if req["value"] == "delete":
            acc.delete(name)
            acc.rcb()
            return redirect("/")
        #print(req)
    
    return render_template("viewd.html", data=nd, presets = presets, name=name)


       
@app.route("/new/", methods=["GET","POST"])
def nnew():
    if request.method == "POST":
        req = request.form
        #acc.pr(req)
        if req.get("act") == "go":

                if req["master_name"] == "":
                    return("enter name")

                else:
                    print(len(req["master_name"]))
                    print(req["master_name"])
                    #req = list(request.form.listvalues())
                    req = request.form.to_dict().items()
                    #print(req)
                    #
                    l = []
                    for i in req:
                        l.append(i)
                        #print(i)
                    #print(l)
                    acc.add_dict(l)
        elif req.get("act") == "add":
            req = dict(request.form)
            acc.add_preset(req)
    return render_template("test.html", presets = presets)


@app.route("/preset/<name>/", methods=["GET","POST"])
def preset(name):

    if name == "new":
        if request.method == "GET":
            print("hi,\n method was get")
        
        if request.method == "POST":
            req = request.form
            

        return render_template("new-preset.html",presets = presets)
    else:
        
        with open(".data/presets.json", "r") as f:
            a = json.load(f)
        pms = a[name]
        if request.method == "GET":
            print("hi,\n method was get")
        
        if request.method == "POST":
            req = request.form
            if req.get("act") == "pass_gen":
                acc.get_password()
                return("hi")

            if req.get("act") == "go":

                if req["master_name"] == "":
                    return("enter name")

                else:
                    print(len(req["master_name"]))
                    print(req["master_name"])
                    req = request.form.to_dict().items()
                    l = []
                    for i in req:
                        l.append(i)
                    acc.add_dict(l)
        return render_template("new-acount.html",data = pms, presets = presets)

ids = acc.get_id()
@app.route("/settings/",methods=["GET","POST"])
def settingss():

    
    if request.method == "POST":
            req = request.form
            if req.get("iid"):
                id = req["iid"]
                patht = f".data/ids/{id}.id"
                settings.edit("path",f".data/ids/{id}.id")
                test.id = settings.get("id")
                ac()
                if os.path.isfile(patht):

                    settings.edit("id",id)
                    test.id = settings.get("id")
                    test.path = f".data/ids/{test.id}.id"
                    ac()
            if req.get("i"):
                if req["i"] == "id":
                    id = req["id"]
                    print(id)
                    patht = f".data/ids/{id}.id"
                    if os.path.isfile(patht):
                        settings.edit("id",id)
                        test.id = id
                        test.path = f".data/ids/{id}.id"
                        ac()
                        
                    
                    
                if req["i"] == "pr_key":
                    il = req["pr_key"]
                    settings.edit("pk",il)
                    test.pk = il
                    ac()
            if req.get("gen"):
                if req["gen"] == "gen":
                    crypt.create_keys(".data")

            if req.get("ii"):
                print(req)
                if req["ii"] == "name":
                    d = req["name"]
                    p =f'.data/ids/{d}.id'
                    print(d)
                    if not os.path.isfile(p):
                        def write_json(data):
                            with open(p, "w") as f:
                                json.dump(data,f,indent=4)
                        with open('.data/ids/template.json', "r+") as f:
                            data = json.load(f)
                        write_json(data)

    return render_template("settings.html", id = test.id, ids=acc.get_id(), pk = test.pk)




if __name__ == "__main__":

    #app.debug = True
    app.run()
    #view()