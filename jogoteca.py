from flask import Flask, render_template

app = Flask(__name__)

class jogos:
        def __init__(self, nome, categoria, console):
                self.nome = nome
                self.categoria = categoria
                self.console = console


jogo1 = jogos('God of War', 'Ação', 'Playstation')
jogo2 = jogos('CSGO', 'Ação', 'PC')
jogo3 = jogos('GTA', 'Ação', 'PC')
lista = [jogo1, jogo2, jogo3]

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html',titulo='Novos Jogos')

app.run()
