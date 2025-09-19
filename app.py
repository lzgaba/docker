from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá! Esta é uma API web simples em Flask."

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo à minha API."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
