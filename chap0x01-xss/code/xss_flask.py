from flask import Flask, render_template, redirect, request, url_for, Response
from flask_bootstrap import Bootstrap
from urllib.parse import urlencode
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("xss_idx.html")


@app.route('/uploadurl', methods=['POST', 'GET'])
def uploadurl():
    if request.method == 'POST':
        if 'web' in request.form.keys():
            name = request.form['web']
        if 'url' in request.form.keys():
            url = request.form['url']
        return render_template("xss_show_url.html", name=name, url=url)
    return render_template("xss_idx.html")


@app.route('/showurl/<string:_url>')
def showurl(_url):
    if not (_url.startswith('http://') or _url.startswith('https://')):  
        _url="https://"+_url
        '''
        对特殊符号检测
        '''
        print(urllib.urlencode(_url))
    return redirect(_url)



if __name__ == "__main__":
    app.run(debug=True)
