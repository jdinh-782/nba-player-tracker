from flask import Flask, render_template, request, flash, redirect
import players

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'  # should be some random long string

@app.route('/about.html')
def about_page():
    return render_template("about.html")

@app.route('/feedback.html')
def contact_page():
    return render_template("feedback.html")

# home page
@app.route('/', methods=["GET", "POST"])
def main():
    # Once the query, after the ?, gets whatever the query is inputted (i.e ?player=Bradley Beal), Bradley Beal will
    # be our argument
    name = request.args.get("search_box")

    if name is None:
        name = "LeBron James"
    else:
        if name == "" or players.get_playerID(name) is None:
            flash("Could not find player in database. Please specify in First Last name format!")
            return redirect("/")

    player_names = players.get_allPlayers()
    player_name = players.get_playerName(name)
    df, url = players.creating_dataframe(players.get_playerID(name))
    return render_template("index.html", player_name=player_name, data=df.to_html(), image_url=url, player_names=player_names)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

