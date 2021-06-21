from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
 return render_template("pagina_no_encontrada.html"), 404