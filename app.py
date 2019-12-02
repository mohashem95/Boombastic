from flask import Flask ,  render_template, json, url_for, request, session
from flask_mail import Mail , Message
#from waitress import serve
#import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mohashem95@gmail.com'
app.config['MAIL_PASSWORD'] = 'iadgzzumsxtqibev'

mail = Mail(app)


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
    return render_template('restaurants.html', title='Restaurants', rests=rests)


@app.route('/signup')
@app.route('/register')
def signup():
    return render_template('signup.html', title='Register')


@app.route('/one_meal/<string:one_meal>')
def meal(one_meal):
    return render_template('meals.html',one_meal=meal_name(meals, one_meal) , title=one_meal + 'meal')


@app.route('/menu/<string:menu>')
def menu_list(menu):
    return render_template('menu.html',menu=meals_type(meals, menu), title=menu + 'menu')     







@app.route('/', methods=['POST'])
def send_mail():
    user_mail = request.form["user_mail"]
    user_message = request.form["user_message"]

    msg = Message('hello', sender= 'noreply@demo.com' , recipients= [user_mail])
    msg.body = f'''{user_message}'''
    mail.send(msg)
    return home() 


with open('../BOOMBASTIC/data.json') as m:
    meals = json.load(m)


with open('../BOOMBASTIC/restaurants.json') as r:
    rests = json.load(r)


def meals_type(meals, m_type):
    for i in range(0, len(meals)):
        if(meals[i]['restaurant'] == 'Mcdonalds' and m_type == 'Mcdonalds'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['restaurant'] == 'KUDO' and m_type == 'KUDO'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['restaurant'] == 'Siction B' and m_type == 'Siction B'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['restaurant'] == 'Albaik' and m_type == 'Albaik'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['restaurant'] == 'Dominos pizza' and m_type == 'Dominos pizza'):
            yield meals[i]
            json.dumps(meals[i])



def meal_name(meals, m_name):
    for i in range(0, len(meals)):
        if(meals[i]['name'] == 'BBQ Angus' and m_name == 'BBQ Angus'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Chicken mac' and m_name == 'Chicken mac'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'McRoyal' and m_name == 'McRoyal'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Chicken combo' and m_name == 'Chicken combo'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Beef combo' and m_name == 'Beef combo'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Cheese omelet combo' and m_name == 'Cheese omelet combo'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'B' and m_name == 'B'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'A' and m_name == 'A'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'V' and m_name == 'V'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Fish fillet meal' and m_name == 'Fish fillet meal'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Jumbo shrimp mea' and m_name == 'Jumbo shrimp mea'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Albaik chicken meal' and m_name == 'Albaik chicken meal'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Dynamite Philly Cheese Steak' and m_name == 'Dynamite Philly Cheese Steak'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Meatzza' and m_name == 'Meatzza'):
            yield meals[i]
            json.dumps(meals[i])
        elif(meals[i]['name'] == 'Margherita' and m_name == 'Margherita'):
            yield meals[i]
            json.dumps(meals[i])

print("-- DEBUG MODE ----")
app.run(debug=True, port='5555')
            
#if __name__ == '__main__':
     #print("--PRODUCTION MODE ---")
     #p = os.environ.get('PORT')
     #serve(app, host='0.0.0.0', port=p)






