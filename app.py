from flask import Flask,render_template,request,jsonify
import sqlite3
# from flask import Flask, render_template, request
import json
app = Flask(__name__, template_folder='templates', static_folder='assets')

# conn = sqlite3.connect('database.db')
# print ("Opened database successfully")
# conn.execute('CREATE TABLE orderdetails (username TEXT,address TEXT,city TEXT,zip TEXT,total TEXT)')
# cur = conn.cursor()
# # cur.execute("INSERT INTO itemcount (item,count) VALUES (?,?)",("Curries",10))
# conn.commit()
# print("Table created successfully")
# conn.close()



# conn = sqlite3.connect('database.db')
# print('Opened database successfully', flush=True)
# conn.execute('DROP TABLE IF EXISTS orderdetails')
# conn.commit()
# conn.close()

@app.route("/")
def home():
    return render_template('indexN.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/chart")
def chart():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from orderdetails")
    rows = cur.fetchall(); 
    return render_template('chart.html',rows=rows)

@app.route("/data")
def get_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM itemcount")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)



@app.route("/menu")
def menu():
    with open('launch.json', 'r') as f:
        data = json.load(f)
    return render_template('menu.html',rows = data)

@app.route("/cart")
def cart():
    return render_template('cart.html')
@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/placeOrder")
def placeorder():
    return render_template('placeorder.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
        try:
            nm = request.form['username']
            addr = request.form['address']
            city = request.form['city']
            pin = request.form['pin']
            total=request.form['total']
            print(nm,addr,city,pin,total)
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO orderdetails (username,address,city,zip,total) VALUES (?,?,?,?,?)",(nm,addr,city,pin,total))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
      
        finally:
            con.close()
            return render_template("result.html", msg=msg)
            
            

@app.route('/orderdetails')
def list():
   con = sqlite3.connect("database.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from orderdetails")
   
   rows = cur.fetchall(); 
   print(rows)
   return render_template("orderdetails.html",rows = rows)


@app.route('/myendpoint', methods=['POST'])
def receive_data():
    print("starting to insert")
    data = request.get_json()
    # for i in data:
    print(data)
    print(type(data))

    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    print("inserted")
    cur = con.cursor()
    for entry in data:
        cur.execute("select count from itemcount where item = ?", (entry['name'],))

        c = cur.fetchone()
        if not c:
            cur.execute("INSERT INTO itemcount (item,count) VALUES (?,?)",(entry['name'],entry['count']))
            c = 0
        else:
            c = c[0]
        cur.execute("UPDATE itemcount SET count = ? WHERE item = ?", (c+entry['count'], entry['name']))
    con.commit()
    con.close()    
    return