from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to the best Pitches Site'
    return render_template('index.html', title = title)

@main.route('/pickUpLines/')
def pickUpLines():
    '''
    View categories page function that returns the pickUpLines category and its data
    '''
    pitches = Pitch.get_pitches('pickUpLines')
    return render_template('pickUpLines.html', pitches = pitches)    

@main.route('/product/')
def product():
    '''
    View categories page function that returns the product pitch category and its data
    '''
    pitches = Pitch.get_pitches('product')
    return render_template('product.html', pitches = pitches)        

@main.route('/interview/')
def interview():
    '''
    View categories page function that returns the interview pitch category and its data
    '''
    pitches = Pitch.get_pitches('interview')
    return render_template('interview.html', pitches = pitches)     

@main.route('/promotion/')
def promotion():
    '''
    View categories page function that returns the promotion pitch category and its data
    '''
    pitches = Pitch.get_pitches('promotion')
    return render_template('promotion.html', pitches = pitches)


@main.route('/review/new/', methods = ['GET','POST'])
def new_review():
     '''
     Function that creates new pitches
     '''
     review = ReviewForm() 

     if form.validate_on_submit():
         review = form.content.data
         category_id = form.category_id.data
         new_review = Review(review = review, category_id = category_id)

         new_review.save_review()
         return redirect(url_for('main.index'))

     return render_template('new_review.html', new_review_form = form, category = category)     