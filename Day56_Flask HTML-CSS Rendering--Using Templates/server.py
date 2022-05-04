from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # the home page route/url
def home_page():
    return render_template('index.html')    # render the html template we downloaded from HTML5UP when on the home page

if __name__ == "__main__":
    app.run(debug=True)     # ran in debug mode to see my changes quicker/easier.
