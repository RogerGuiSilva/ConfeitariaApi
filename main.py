import os

from flask import Flask
from cardapio import buscar_cardapio

app = Flask(__name__)

@app.route("/")
def hello_world():
  return {
    "message": "Api rodando"

  }

@app.route("/cardapio")
def cardapio():
  return buscar_cardapio()
  

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))