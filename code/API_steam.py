from flask import Flask, render_template



def steam_dashboard():
    pass


page_link = 'homepage.html'

# https://api.steampowered.com/<interface>/<method>/v<version>/
steam_api_request_url = "http://api.steampowered.com"

## go get the API stuff here
dashboard_content = "testing!!!!!"

app = Flask(__name__)
print("app initiated. name of app is: ", __name__)

# only used to display the API stuff for now
@app.route("/")
def homepage():
    return render_template(page_link,
                           dashboard=dashboard_content)



if __name__ == '__main__':
    app.run(debug=True, port=5000)