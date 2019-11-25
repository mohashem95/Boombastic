from flask import Flask ,  render_template


app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html', title='home')

@app.route('/about')
@app.route('/aboutus')
def about():
    return render_template('about.html', title='About Us')

@app.route('/contact')
@app.route('/contactus')
def contact():
    return render_template('contact.html', title='Contact Us')

@app.route('/login')
@app.route('/signin')
def login():
    return render_template('login.html', title='Login')

@app.route('/restaurants')
@app.route('/restaurantslist')
def restaurants():
    return render_template('restaurants.html', title='Restaurants')

@app.route('/signup')
@app.route('/register')
def signup():
    return render_template('signup.html', title='Register')



app.run(debug=True, port='5555')

