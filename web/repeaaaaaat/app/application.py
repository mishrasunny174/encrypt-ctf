from flask import Flask, render_template, request, render_template_string
import random

app = Flask(__name__)

app.secret_key = "cf49d97a5680998cbddbee283eeb03adbeda772b"

@app.route("/lol_no_one_will_see_whats_here")
def troll1():
    return render_template("troll1.html")

@app.route("/what_are_you_searching_for")
def troll2():
    return render_template("troll2.html")

@app.route("/", methods=["GET"])
def inject():
    hints = ["Lz9zZWNyZXQ9ZmxhZw==", "L2xvbF9ub19vbmVfd2lsbF9zZWVfd2hhdHNfaGVyZQ==", 
             "d2hhdF9hcmVfeW91X3NlYXJjaGluZ19mb3IK"];
    hint = hints[random.randint(0, len(hints)-1)]
    secret = request.args.get("secret", default="")
    template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>repeaaaaaat</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script>
        function repeat() {
            for(var i=0; i<10; i++) {
            lol = document.createElement("img")
            lol.src = "/static/lol.png"
            var shit = document.getElementById('shit')
            shit.appendChild(lol)
            }
        }
    </script>
    </head>
    <body onscroll=repeat()>
        Hello,<div id="shit">
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
            <img src='/static/lol.png'>
        </div> %s
        <!-- %s -->
    </body>
</html>                         """ % (secret, hint)
    return render_template_string(template)


if __name__ == "__main__":
    app.run(debug=True)
