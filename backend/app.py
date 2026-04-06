from flask import Flask
from flask_cors import CORS
from extensions import bcrypt, jwt

from routes.property_routes import property_bp
from routes.investment_routes import investment_bp
from routes.dividend_routes import dividend_bp
from routes.auth_routes import auth_bp
from routes.ml_routes import ml_bp
from routes.portfolio_routes import portfolio_bp   # ✅ ADD THIS

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret"

CORS(app)
bcrypt.init_app(app)
jwt.init_app(app)

@app.route("/")
def home():
    return "Backend Running ✅"

# ✅ REGISTER ALL ROUTES
app.register_blueprint(property_bp, url_prefix="/properties")
app.register_blueprint(investment_bp, url_prefix="/invest")
app.register_blueprint(dividend_bp, url_prefix="/dividend")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(ml_bp, url_prefix="/ml")
app.register_blueprint(portfolio_bp, url_prefix="/portfolio")  # ✅ THIS LINE

if __name__ == "__main__":
    app.run(debug=True)