from dashboard import app

app.debug = True
#app.jinja_env.cache = {}
app.run(host='0.0.0.0', port=5000)
