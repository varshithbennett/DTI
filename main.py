from flask import Flask, render_template, request, redirect, url_for
import logging
from abilities import key_value_storage


from flask import Flask, render_template
from gunicorn.app.base import BaseApplication

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/deliver")
def deliver():
    return render_template("deliver.html")

@app.route("/receive")
def receive():
    return render_template("receive.html")

@app.route("/")
def home_route():
    return render_template("home.html")

@app.route("/register")
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Store user data in key-value storage
        result = key_value_storage('store', 'user_data', email, password)
        if result['upstream_service_result_code'] == 201:
            return redirect(url_for('home_route'))
        else:
            return "Error storing user data", 500
    return render_template("register.html")

@app.route("/parcel", methods=['GET', 'POST'])
def parcel():
    if request.method == 'POST':
        logger.info(f"Parcel registered: {request.form['name']} for {request.form['location']}")
        return render_template("parcel_success.html")
    return render_template("parcel.html")

@app.route("/success", methods=['POST'])
def success():
    return render_template("success.html")

@app.route("/food")
def food():
    return render_template("food.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Retrieve user data from key-value storage
        user_data = key_value_storage('retrieve', 'user_data', email, '')
        if user_data['kv_pairs']:
            stored_password = user_data['kv_pairs'][0]['value']
            if password == stored_password:
                return redirect(url_for('home_route'))
            else:
                return "Invalid password", 403
        else:
            return "User not found", 404
    return render_template("login.html")

@app.route("/orders", methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        # TODO: Implement logic to process registration and login data, then display orders
        # For now, simply logging the data received
        logger.info(f"Data received: {request.form}")
        return render_template("orders.html")
    return render_template("orders.html")


class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


# Do not remove the main function while updating the app.
if __name__ == "__main__":
    options = {"bind": "%s:%s" % ("0.0.0.0", "8080"), "workers": 4, "loglevel": "info", "accesslog": "-"}
    StandaloneApplication(app, options).run()
