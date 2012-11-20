from flask import Flask, request

import difftext, json

app = Flask(__name__)

@app.route("/")
def index():
    return "App that to allow the differencing of files"

@app.route("/compare")
def compare():
    return """<html><head><title>Difference Form</title><style>#original {float:left} #compare {float:right}</style></head><body><div id="nav"><ul><li>Home</li><li>Compare</li></ul></div>'<form method="post" action="difference">
    <div id="original">First Text</div><textarea cols="75" rows="40" name="old" value=""></textarea>
    <div id="compare">Second Text</div><textarea cols="75" rows="40"  name="new" value=""></textarea>
    <input type="submit" value="submit" />
    </form></body></html>
    """


@app.route("/difference", methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def difference():
    out =''
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'text/plain':
            firsttxt = request.form['old'].split()
            secondtxt = request.form['new'].split()
            d = difftext.differenceText(firsttxt, secondtxt)
            diff = d.diff_text()
            
            out = '<!DOCTYPE html><head><title>Text Difference</title><style>#first {color: red;} #second{color:blue;}</style></head><body>'
            out += '<div id="nav"><ul><li>Home</li><li>Compare</li></ul></div>'
            for ln in diff.split('\n'):
    
                if ln.startswith('-'):
                    out += '<span id="first">'+ln[1:]+'</span>'
                elif ln.startswith('+'):
                    out += '<span id="second">'+ln[1:]+'</span>'
                elif ln.startswith('?'):
                    pass
                else:
                    out +=ln
            
            out += "</body></html>"
        elif request.headers['Content-Type'] == 'application/json':
            out = json.dumps({ "error": "Content-Type Not Supported Yet!" })
        elif request.headers['Content-Type'] == 'application/xml':
            out = '<?xml version="1.0"?><error>Content-Type Not Supported Yet!</error>'
        else:
            out = "415 Unsupported Media Type ;)"
        return out
    else:
        return '405 Method not supported yet'


if __name__ == "__main__":
    app.run(debug=True)