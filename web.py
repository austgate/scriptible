from flask import Flask, request, render_template, Markup

import difftext, json

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/compare")
def compare():
    return render_template('compare.html')


@app.route("/difference", methods=['GET', 'POST']) #, 'PATCH', 'PUT', 'DELETE' to be supported
def difference():
    out =''
    if request.method == 'POST':
        #html, plan and forms - perhaps need to remove the plain at some point
        if request.headers['Content-Type'] == 'text/plain' or request.headers['Content-Type'] == 'application/html' or request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            firsttxt = request.form['old'].split()
            secondtxt = request.form['new'].split()
            
            d = difftext.differenceText(firsttxt, secondtxt)
            diff = d.diff_text()
            
            line = 1
            for ln in diff.split('\n'):

                if ln.startswith('-'):
                    out += Markup('<span id="first">'+ln[1:]+'</span>')
                elif ln.startswith('+'):
                    out += Markup('<span id="second">'+ln[1:]+'</span>')
                elif ln.startswith('?'):
                    pass
                else:
                    out +=ln

            
            return render_template('difference.html', out=out)
        elif request.headers['Content-Type'] == 'application/json':
            out = json.dumps({ "error": "Content-Type Not Supported Yet!" })
        elif request.headers['Content-Type'] == 'application/xml':
            out = '<?xml version="1.0"?><error>Content-Type Not Supported Yet!</error>'
        else:
            out = "415 Unsupported Media Type ;)" + request.headers['Content-Type']
        return out
    else:
        return '405 Method not supported yet'


if __name__ == "__main__":
    app.run(debug=True)