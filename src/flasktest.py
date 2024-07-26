from flask import Flask, render_template, request
import iris

def search_person(search_param):
    sql="select ID,Name,Email,TOCHAR(DOB,'YYYY-MM-DD'), job from Test.Person WHERE Name like '%' || ? || '%'"
    stmt=iris.sql.prepare(sql)
    rset=stmt.execute(search_param)
    return rset

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("search.html",search_result="")

@app.route('/', methods=['POST'])
def search():
    search_param = request.form.get('search_param')
    if not search_param:
        return render_template("search.html", search_result="")
    
    result = search_person(search_param)
    return render_template("search.html", search_result=result)

if __name__ == '__main__':
    app.run(debug=True) 
