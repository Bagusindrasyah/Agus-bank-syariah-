from flask import Flask, render_template, request

app = Flask(__name__)

# Data akun pengguna
accounts = {
    "user1": {
        "balance": 10000,
        "pin": "1234"
    },
    "user2": {
        "balance": 20000,
        "pin": "5678"
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_balance", methods=["POST"])
def check_balance():
    username = request.form["username"]
    pin = request.form["pin"]
    if username in accounts and accounts[username]["pin"] == pin:
        balance = accounts[username]["balance"]
        return f"Saldo Anda: Rp{balance}"
    else:
        return "Username atau PIN tidak valid"

@app.route("/deposit", methods=["POST"])
def deposit():
    username = request.form["username"]
    pin = request.form["pin"]
    amount = float(request.form["amount"])
    if username in accounts and accounts[username]["pin"] == pin:
        accounts[username]["balance"] += amount
        return f"Berhasil melakukan deposit sebesar Rp{amount}"
    else:
        return "Username atau PIN tidak valid"

@app.route("/withdraw", methods=["POST"])
def withdraw():
    username = request.form["username"]
    pin = request.form["pin"]
    amount = float(request.form["amount"])
    if username in accounts and accounts[username]["pin"] == pin and accounts[username]["balance"] >= amount:
        accounts[username]["balance"] -= amount
        return f"Berhasil melakukan penarikan tunai sebesar Rp{amount}"
    else:
        return "Username, PIN, atau saldo tidak valid"

if __name__ == "__main__":
    app.run(debug=True)
