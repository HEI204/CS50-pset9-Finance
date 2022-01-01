import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime, timezone

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
# if not os.environ.get("API_KEY"):
#    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session["user_id"]
    # Query the stock info that the user has bought
    user_stock_info = db.execute(
        "SELECT symbol, name, SUM(shares) as total_shares, price FROM purchase WHERE user_id = ? GROUP BY symbol", user_id)

    # Query the current cash of the user
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    total = user_cash
    for stock in user_stock_info:
        total += stock["price"] * stock["total_shares"]

    return render_template("index.html", user_stock_info=user_stock_info, user_cash=usd(user_cash),
                           total=usd(total), usd=usd, lookup=lookup, percentage=percentage)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add Cash"""

    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("add_cash.html", user_cash=usd(user_cash))

    added_cash = request.form.get("added_cash")
    new_total_cash = float(added_cash) + float(user_cash)
    db.execute("UPDATE users SET cash = ? WHERE id = ?", new_total_cash, session["user_id"])
    db.execute("INSERT INTO purchase(user_id, type, symbol, name, shares, price) VALUES(?, ?, ?, ?, ?, ?)",
                   session["user_id"], "ADD CASH", "N/A", "N/A", 1, float(added_cash))

    return render_template("add_cash.html",user_cash=usd(new_total_cash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via GET (as by clicking a link or via redirect)

    # New added for personal touch
    # If user click "buy" in index then auto filled in the corresponding stock symbol
    if request.method == "GET":
        temp = request.args.get("buy_symbol")
        if not temp:
            buy_symbol = ""
        else:
            buy_symbol = temp
        return render_template("buy.html", buy_symbol=buy_symbol)

    # method=="POST"
    stock_info = lookup(request.form.get("symbol"))

    try:
        number = int(request.form.get("shares"))
    except ValueError:
        return apology("Shares should be positive integer")

    # Validation for stock symbol and number of shares
    if not stock_info:
        return apology("Invalid symbol or This symbol does not exist")

    if number <= 0:
        return apology("Shares should be positive integer")

    # Extract the info of stock from lookup function
    stock_symbol = stock_info["symbol"]
    stock_name = stock_info["name"]
    stock_price = stock_info["price"]

    user_id = session["user_id"]

    # Query the cash info from the database
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    # Calculate the remaining cash after user buy the number of stock
    remaining_cash = user_cash - (stock_price * number)

    if remaining_cash < 0:
        return apology("You do not have enough cash to buy the stocks")

    # If user able to buy the number of share for that stock
    # Then update the cash for the user after bought the stock
    # Also insert the purchase info in the database
    else:
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_cash, user_id)
        db.execute("INSERT INTO purchase(user_id, type, symbol, name, shares, price) VALUES(?, ?, ?, ?, ?, ?)",
                   user_id, "BUY", stock_symbol, stock_name, number, stock_price)
        return redirect("/")


# New added for personal touch
@app.route("/changepassword", methods=["GET", "POST"])
def change_password():
    """Allow user to change their password"""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("changepassword.html")

    # User reached route via POST (as by submitting a form via POST)
    current_pw = request.form.get("current_password")
    new_pw = request.form.get("new_password")
    confirm_new_pw = request.form.get("confirm_new_password")

    # Check whether the input box for current password is empty or not
    if not current_pw:
        return apology("You should input your current password")

    # Check whether the current password is correct or not
    old_password = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
    if len(old_password) != 1 or not check_password_hash(old_password[0]["hash"], current_pw):
        return apology("invalid username and/or password", 403)

    # New password and Confirm New Password Validation
    if not new_pw:
        return apology("You should input your new password")
    elif not confirm_new_pw:
        return apology("You should input your password in 'Confirmation New Password'")
    elif new_pw != confirm_new_pw:
        return apology("Password does not match")

    # Update the the new password for that user in database
    hashed_new_pw = generate_password_hash(new_pw)
    db.execute("UPDATE users SET hash = ? WHERE id = ?", hashed_new_pw, session["user_id"])

    # Redirect the user to login form
    return redirect("/logout")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Query the required info for the history page from the database
    transaction_info = db.execute(
        "SELECT type, symbol, price, shares, timestamp FROM purchase WHERE user_id = ? ORDER BY timestamp DESC", session["user_id"])
    return render_template("history.html", transaction_info=transaction_info, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("quote.html")

    # User reached route via POST (as by submitting a form via POST)
    stock_info = lookup(request.form.get("symbol"))
    if not stock_info:
        return apology("Invalid symbol or This symbol does not exist")

    return render_template("quoted.html", name=stock_info["name"], price=usd(stock_info["price"]),
                           symbol=stock_info["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("register.html")

    # User reached route via POST (as by submitting a form via POST)
    username = request.form.get("username")
    pw = request.form.get("password")
    confirm_pw = request.form.get("confirmation")

    # Username and Password Validation
    if not username:
        return apology("You should input the username")
    elif not pw:
        return apology("You should input your password")
    elif not confirm_pw:
        return apology("You should input your password in 'Confirmation Password'")
    elif pw != confirm_pw:
        return apology("Password does not match")

    # Hash the password
    hashed_pw = generate_password_hash(pw)

    # Insert username and hashed password into the database
    try:
        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hashed_pw)
    # If the username already exist in the database
    except:
        return apology("Username registered by others already")

    # Redirect the user to login form
    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user_id = session["user_id"]

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":

        # New added for personal touch
        # If user click "sell" in the index then pre-select the corresponding stock
        temp = request.args.get("sell_symbol")
        if not temp:
            sell_symbol = ""
        else:
            sell_symbol = temp

        # Query the symbol from the purchase database for the user
        stock_symbol = db.execute("SELECT symbol FROM purchase WHERE user_id = ? GROUP BY symbol", user_id)

        return render_template("sell.html", stock_symbol=stock_symbol, sell_symbol=sell_symbol)

    # User reached route via POST (as by submitting a form via POST)
    # When user already selected their stock to sell in the drop-down list
    else:
        # Get the symbol from the drop-down list and the number of shares in sell.html
        selected_stock_symbol = request.form.get("symbol")
        number = int(request.form.get("shares"))

        selected_stock_price = lookup(selected_stock_symbol)["price"]
        selected_stock_name = lookup(selected_stock_symbol)["name"]

        if number <= 0:
            return apology("Shares should be positive integer")

        # Query the total number of share that you bought before
        current_own_shares = db.execute("SELECT SUM(shares) as total_shares FROM purchase WHERE user_id = ? AND symbol = ? GROUP BY symbol",
                                        user_id, selected_stock_symbol)[0]["total_shares"]

        if current_own_shares < number:
            return apology("You don't have enough shares to sell")

        # Query the current cash of the user
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # Update the cash of the user after they sell the stock
        db.execute("UPDATE users SET cash = ? WHERE id =?", (current_cash + (number * selected_stock_price)), user_id)

        # Update the purchase table in database for the sell action
        db.execute("INSERT INTO purchase(user_id, type, symbol, name, shares, price) VALUES(?, ?, ?, ?, ?, ?)",
                   user_id, "SELL", selected_stock_symbol, selected_stock_name, -number, selected_stock_price)

        return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

# Handle percentage output for index page
def percentage(value):
    """Format value as percentage. """
    return f"{value:,.2f}%"

