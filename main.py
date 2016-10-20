from flask import Flask
from pg import DB
db = DB(dbname='test', host='localhost', port=5432,
	 user='postgres', passwd='NBXSQMFQ')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<marquee>Hello, World!</marquee>'

@app.route("/pippo/<var1>/<var2>")
def pippizer(var1,var2 ):
	queryResult=db.query("select * from dbddl.piatto")	
	rows=queryResult.getresult()
	res=""
	for row in rows:
		res=res+"<div>"+str(row)+"</div>"
	return res
	

