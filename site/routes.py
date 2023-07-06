from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from books_inventory.forms import BookForm
from books_inventory.models import Book, db 
from books_inventory.helpers import random_joke_generator



site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    #print('look at thos cool project. Would you just look at it')  
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    bookform = BookForm()

    try:
        if request.method == 'POST' and bookform.validate_on_submit():
            name = bookform.name.data
            description = bookform.description.data
            price = bookform.price.data
            author = bookform.author.data
            genre = bookform.genre.data
            publisher = bookform.publisher.data
            edition = bookform.edition.data
            language = bookform.language.data
            cost_of_prod = bookform.cost_of_prod.data
            series = bookform.series.data
            if bookform.dad_joke.data:
                random_joke = bookform.dad_joke.data
            else:
                random_joke = random_joke_generator()
            user_token = current_user.token 

            book = Book(name, description, price, author, genre, publisher, 
                          edition, language, cost_of_prod, series, random_joke, user_token)
            
            db.session.add(book)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Drone not created, please check your form and try again.') 
    
    user_token = current_user.token 
    books = Book.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=bookform, books=books )


    