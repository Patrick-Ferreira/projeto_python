from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if(request.form["num1"] != "" and request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]

            if(request.form["opc"] == "soma"):
                soma = int(num1) + int(num2)
                return str(soma)

            elif(request.form["opc"] == "subt"):
                subt = int(num1) - int(num2)
                return str(subt)

            elif(request.form["opc"] == "mult"):
                mult = int(num1) * int(num2)
                return str(mult)

            else:
                divi = int(num1) // int(num2)
                return str(divi)

        else:
            return "Informe um numero válido!"

#@app.route("/<int:id>")
#def home_id(id):
    #return str(id + 1)
#exibir em json
#elif(request.form["opc"] == "mult"):
        #mult = int(num1) * int(num2)
        #return {"Resultado": str(mult)}



@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")
#@app.route("/sobre")
#def sobre():
    #return "Sobre"

app.run(port=8080, debug=True)