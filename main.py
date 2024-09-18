from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:/Users/Siris/Desktop/GitHub Projects 100 Days NewB/_24_0092__Day88_Pro_Portfolio_Project_Cafe_and_WiFi_Website__240917/NewProject/r00_env_START/r03/pythonProject1/instance/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Cafe model representing the 'cafe' table in the SQLite database
class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

@app.route('/')
def index():
    cafes = Cafe.query.all()
    return render_template('index.html', cafes=cafes)

# Route to handle filtered search
@app.route('/filter', methods=['GET'])
def filter_cafes():
    cafes_query = Cafe.query

    # Apply filters based on query parameters
    if request.args.get('has_wifi') == '1':
        cafes_query = cafes_query.filter(Cafe.has_wifi == True)
    if request.args.get('has_sockets') == '1':
        cafes_query = cafes_query.filter(Cafe.has_sockets == True)
    if request.args.get('can_take_calls') == '1':
        cafes_query = cafes_query.filter(Cafe.can_take_calls == True)

    cafes = cafes_query.all()

    # Dynamically render just the cafes grid
    return render_template('cafes_list.html', cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)
