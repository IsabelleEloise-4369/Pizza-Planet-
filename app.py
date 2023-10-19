# IMPORTAÇÃO DA CLASSE flask DO FRAMEWORK Flask
from flask import Flask, render_template, request, redirect
import random

# CRIA O OBJETO APP USANDO A CLASSE Flask
# ESSE APP SERA O MEU SERVIDOR
app = Flask(__name__)

emails_cadastrados = []

# ABAIXO CÓDIGO DA MINHA PÁGINA

#ROTA DA PÁGINA PRINCIPAL (INDEX)
@app.route("/")
def pagina_index():

    curiosidades = ["Somente nos Estados Unidos, estipula-se que são vendidas 350 fatias de pizza a cada segundo!",
                    "A palavra “pizza” vem do latim picea, que designa o objeto torrado pelo fogo.",
                    "A pizza pode ser assada em diferentes tipos de fornos, os três principais são: forno a carvão, forno a gás e forno a lenha para pizza."]

    foto_banner = ["pizza1.jpeg",
                   "pizza2.jpeg",
                   "pizza3.jpeg",
                   "pizza4.jpeg"]

    #RETORNA A PÁGINA INDEX QUE ESTÁ NA PASTA TEMPLATES
    return render_template("index.html",
                           foto_banner = random.choice(foto_banner),
                           curiosidades = random.choice(curiosidades))

@app.route("/sobre")
def pagina_sobre():
    return render_template("sobre.html")

@app.route("/newsletter", methods=["GET", "POST"])
def pagina_newsletter():
    if request.method == "GET":
        return render_template("newsletter.html")
    else:
        email = request.form["email"]
        if email == "":
            resultado = ("E-mail válido")
        else:
            emails_cadastrados.append(email)
            resultado = "Cadastro efetuado com sucesso"
        return render_template("newsletter.html", campo_resultado = resultado)


@app.route("/login", methods=["GET","POST"])
def pagina_login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        login = request.form["usuario"].upper()
        senha = request.form["senha"]
        if login == "" and senha == "":
             resultado  = ("Usuário e senha não cadastrados")
        if login == "GODOFREDO" and senha == "lindao":
            return redirect("/emails_cadastrados")
        else:
            resultado = "Cadastro não encontrado"
        return render_template("login.html", campo_resultado = resultado)



@app.route("/emails_cadastrados")
def pagina_emails_cadastrados():
    return render_template("emails_cadastrados.html", campo_emails = emails_cadastrados)



# INICIA, STARTA, RODA, LIGA O MEU SERVIDOR
# Debug=true SERVE PARA QUE VOCÊ NÃO TENHA QUE FICAR REINICINADO O SERVIDOR, BASTA SALVAR O ARQUIVO PARA QUE ELE REINICIE.

app.run(host= "0.0.0.0", port=8080)
