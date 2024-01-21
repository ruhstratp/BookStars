from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import uuid
import jwt
from datetime import datetime, timedelta, date
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'A&&A'
app.config['CORS_HEADERS'] = 'Content-Type'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'book_stars.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
db = SQLAlchemy(app)

class BlogMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_of_the_week_id = db.Column(db.Integer, db.ForeignKey('book_of_the_week.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(2000), nullable=False)

class BookOfTheWeek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image_url = db.Column(db.String(2500), nullable = False)
    publish_year = db.Column(db.Integer, nullable=False)
    page_count = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_public = db.Column(db.Boolean, nullable=False)
    text = db.Column(db.String(2000), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    score = db.Column(db.Float, nullable=False)

class ReviewLikes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    like = db.Column(db.Boolean,  nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer, nullable = False)
    user_name = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)

# with app.app_context():
#    db.create_all()
#    db.session.commit()

def populate_tables():
    book_list = []
    new_book = Book(name='The Power of Now',
                    author='Eckhart Tolle',
                    description='In the first chapter, Tolle introduces readers to enlightenment and its natural enemy, the mind. He awakens readers to their role as a creator of pain and shows them how to have a pain-free identity by living fully in the present. The journey is thrilling, and along the way, the author shows how to connect to the indestructible essence of our Being, "the eternal, ever-present One Life beyond the myriad forms of life that are subject to birth and death."',
                    image_url='https://m.media-amazon.com/images/I/417VRErnKPL._AC_SY780_.jpg',
                    rating=0,
                    publish_year=2004,
                    page_count=236,
                    publisher='New World Library')  
              
    db.session.add(new_book)  
    book_list.append(new_book)
    new_book = Book(name='How to win friends and influence people',
                    author='Dale Carnegie',
                    description='Dale Carnegie’s rock-solid, time-tested advice has carried countless people up the ladder of success in their business and personal lives. One of the most groundbreaking and timeless bestsellers of all time, How to Win Friends & Influence People will teach you:six ways to make people like you, twelve ways to win people to your way of thinking, nine ways to change people without arousing resentment.',
                    image_url='https://m.media-amazon.com/images/I/41OksZQYt+L._SX320_BO1,204,203,200_.jpg',
                    rating=0,
                    publish_year=1998,
                    page_count=320,
                    publisher='Pocket Books')                 
    db.session.add(new_book) 
    book_list.append(new_book)
    new_book = Book(name='The 5 love languages',
                    author='Gary Chapman',
                    description='Falling in love is easy. Staying in love—that\'s the challenge. How can you keep your relationship fresh and growing amid the demands, conflicts, and just plain boredom of everyday life?In this book, you\'ll discover the secret that has transformed millions of relationships worldwide. Whether your relationship is flourishing or failing, Dr. Gary Chapman\'s proven approach to showing and receiving love will help you experience deeper and richer levels of intimacy with your partner—starting today.',
                    image_url='https://m.media-amazon.com/images/I/51c0ewv4OML._SX417_BO1,204,203,200_.jpg',
                    rating=0,
                    publish_year=2015,
                    page_count=208,
                    publisher='Northfield Publishing')                 
    db.session.add(new_book)
    book_list.append(new_book) 
    new_book = Book(name='1984',
                    author='George Orwell',
                    description='A startling and haunting novel, 1984 creates an imaginary world that is completely convincing from start to finish. No one can deny the novel’s hold on the imaginations of whole generations, or the power of its admonitions—a power that seems to grow, not lessen, with the passage of time.',
                    image_url='https://m.media-amazon.com/images/I/41aM4xOZxaL._SX277_BO1,204,203,200_.jpg',
                    rating=0,
                    publish_year=1961,
                    page_count=328,
                    publisher='Signet Classic')                 
    db.session.add(new_book) 
    book_list.append(new_book)
    new_book = Book(name='Kafka on the shore',
                    author='Haruki Murakami',
                    description='A startling and haunting novel, 1984 creates an imaginary world that is completely convincing from start to finish. No one can deny the novel’s hold on the imaginations of whole generations, or the power of its admonitions—a power that seems to grow, not lessen, with the passage of time.',
                    image_url='https://m.media-amazon.com/images/I/3190fsfp48L._SX321_BO1,204,203,200_.jpg',
                    rating=0,
                    publish_year=2005,
                    page_count=505,
                    publisher='Vintage')                 
    db.session.add(new_book)
    book_list.append(new_book)
    new_book = Book(name='The Great Gatsby',
                    author='F.Scott Fitzgerald',
                    description='The story primarily concerns the young and mysterious millionaire Jay Gatsby and his quixotic passion for the beautiful Daisy Buchanan. Considered to be Fitzgerald\'s magnum opus, The Great Gatsby explores themes of decadence, idealism, resistance to change, social upheaval, and excess, creating a portrait of the Jazz Age or the Roaring Twenties that has been described as a cautionary tale regarding the American Dream.',
                    image_url='https://m.media-amazon.com/images/I/51-b1lX+vYL.jpg',
                    rating=0,
                    publish_year=1925,
                    page_count=214,
                    publisher='Unabridgd')                 
    db.session.add(new_book)
    book_list.append(new_book)
    new_book = Book(name='To Kill a Mockingbird',
                    author='Harper Lee',
                    description='A gripping, heart-wrenching, and wholly remarkable tale of coming-of-age in a South poisoned by virulent prejudice, it views a world of great beauty and savage inequities through the eyes of a young girl, as her father—a crusading local lawyer—risks everything to defend a black man unjustly accused of a terrible crime.',
                    image_url='https://m.media-amazon.com/images/I/51IXWZzlgSL._SX330_BO1,204,203,200_.jpg',
                    rating=0,
                    publish_year=2002,
                    page_count=336,
                    publisher='Harper Perennial')                 
    db.session.add(new_book)
    book_list.append(new_book)
    new_book = Book(name='Pride and Prejudice',
                    author='Jane Austen',
                    description='When Elizabeth first meets eligible bachelor Fitzwilliam, she thinks him arrogant and conceited; he is indifferent to her. When she later discovers that Darcy has involved himself in the relationship between his friend Bingley and her sister Jane, she is determined to dislike him more than ever. In the sparkling comedy of manners that follows, Jane shows us the folly of judging by first impressions and superbly evokes the friendships, gossip and snobberies of provincial middle-class life.',
                    image_url='https://m.media-amazon.com/images/I/51IXWZzlgSL._SX330_BO1,204,203,200_.jpg',
                    rating=0,
                    publish_year=2002,
                    page_count=480,
                    publisher='Penguin Books')                 
    db.session.add(new_book)
    book_list.append(new_book) 

    today = date.today()
    days_to_tuesday = 1 - today.weekday()
    start_date = today + timedelta(days=days_to_tuesday)
    all_books = Book.query.all()

    for book, i in zip(all_books, range(len(all_books))):
        new = BookOfTheWeek(book_id=book.id, start_date=start_date + timedelta(weeks=i))
        db.session.add(new)

    hashed_password = generate_password_hash('123', method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), user_name='alex', password=hashed_password)
    db.session.add(new_user)
    hashed_password = generate_password_hash('123aaa', method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), user_name='ana', password=hashed_password)
    db.session.add(new_user)
    hashed_password = generate_password_hash('zxcv', method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), user_name='paty', password=hashed_password)
    db.session.add(new_user)
    hashed_password = generate_password_hash('123', method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), user_name='mirela', password=hashed_password)
    db.session.add(new_user)
    hashed_password = generate_password_hash('123', method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), user_name='dia', password=hashed_password)
    db.session.add(new_user)

    new_review = Review(book_id=8, user_id=2, is_public=True, text='Though the novel is more than 200 years old, its plot and characters have maintained their appeal, especially among fans of happy-ending romances.', rating=4, score=0)
    db.session.add(new_review)
    new_review = Review(book_id=8, user_id=1, is_public=True, text='A classic, but it bored me to death. Read it for school, do not recommand', rating=1, score=0)
    db.session.add(new_review)
    new_review = Review(book_id=1, user_id=1, is_public=True, text='This is not a book you read for self-denial. It makes a mockery of such books, in fact. The self-help books that give your mind a focus, a mission, a purpose, the ego a cause, yeah, this isn\'t that.', rating=5, score=0)
    db.session.add(new_review)
    db.session.commit()

#populate_tables()

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'authorization-token' in request.headers:
           token = request.headers['authorization-token']
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
           current_user = User.query.filter_by(public_id=data['public_id']).first()
       except:
           return jsonify({'message': 'token is invalid'})
       return f(current_user, *args, **kwargs)
   return decorator

@app.route('/register', methods=['POST'])
def signup_user(): 
   data = request.get_json() 
   hashed_password = generate_password_hash(data['password'], method='sha256')
   new_user = User(public_id=str(uuid.uuid4()), user_name=data['name'], password=hashed_password)
   db.session.add(new_user) 
   db.session.commit()   
   return jsonify({'message': 'registered successfully'})

@app.route('/login', methods=['POST']) 
def login_user():
   auth = request.authorization  
   if not auth or not auth.username or not auth.password: 
       return make_response('could not verify', 401, {'Authentication': 'login required"'})   
   user = User.query.filter_by(user_name=auth.username).first()  
   if check_password_hash(user.password, auth.password):
       token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.utcnow() + timedelta(minutes=50)}, app.config['SECRET_KEY'], "HS256")
       return jsonify({'token' : token})
   return make_response('could not verify',  401, {'Authentication': '"login required"'})

@app.route('/book', methods=['POST'])
@token_required
def create_book(current_user):
   data = request.get_json()
   new_book = Book(name=data['name'], author=data['author'], description=data['description'], image_url=data['imageUrl'], rating=0, publish_year=data['publish_year'], page_count=data['page_count'], publisher=data['publisher']) 
   db.session.add(new_book)  
   db.session.commit() 
   return jsonify({'message' : 'new books created'})

@app.route('/books', methods=['GET'])
def get_books():
   books = Book.query.all()
   output = []
   for book in books:
       book_data = {}
       book_data['id'] = book.id
       book_data['name'] = book.name
       book_data['author'] = book.author
       book_data['imageUrl'] = book.image_url
       book_data['description'] = book.description
       book_data['publishYear'] = book.publish_year
       book_data['pageCount'] = book.page_count
       book_data['publisher'] = book.publisher
       book_data['rating'] = book.rating
       output.append(book_data)
 
   return jsonify({'listOfBooks' : output})

@app.route('/book/<int:bookId>')
@token_required
def get_book(current_user, bookId):
    book = Book.query.filter_by(id=bookId).first()
    if not book:  
       return jsonify({'message': 'book does not exist'})

    result = {}
    has_written_review = False
    book_data = {}
    book_data['id'] = book.id
    book_data['name'] = book.name
    book_data['author'] = book.author
    book_data['imageUrl'] = book.image_url
    book_data['description'] = book.description
    book_data['publishYear'] = book.publish_year
    book_data['pageCount'] = book.page_count
    book_data['publisher'] = book.publisher
    book_data['rating'] = book.rating
    result['bookData'] = book_data

    rev = Review.query.filter_by(book_id=bookId, is_public=True).all()
    reviews = []
    for review in rev:
        review_likes = ReviewLikes.query.filter_by(user_id=current_user.id, review_id=review.id).first()
        review_owner = User.query.filter_by(id=review.user_id).first()
        review_data = {}
        review_data['id'] = review.id
        review_data['bookId'] = review.book_id
        review_data['userId'] = review.user_id
        review_data['isPublic'] = review.is_public
        review_data['text'] = review.text
        review_data['rating'] = review.rating
        review_data['score'] = review.score
        review_data['userName'] = review_owner.user_name
        if review_likes:
            review_data['likedByUser'] = review_likes.like == True
            review_data['dislikedByUser'] = review_likes.like == False
        reviews.append(review_data)

        this_user = User.query.filter_by(id=current_user.id).first()
        if this_user.id == review_owner.id:
            has_written_review = True
    book_data['userHasWrittenReview'] = has_written_review
    result['reviews'] = reviews

    return jsonify(result)

@app.route('/add_review/<int:bookID>', methods=['POST'])
@token_required
def add_review(current_user, bookID):
    data = request.get_json()
    new_review = Review(book_id=bookID, user_id = current_user.id, is_public=data['isPublic'], text=data['text'], rating=data['rating'], score=0)
    db.session.add(new_review)  
    if data['rating']:
        sum = data['rating']
        nr_of_ratings = 1
        all_reviews = Review.query.filter(Review.rating!=0).filter_by(book_id=bookID).all()
        for rev in all_reviews:
            sum += rev.rating
            nr_of_ratings += 1
        book = Book.query.filter_by(id=bookID).first()
        book.rating = sum / nr_of_ratings
    db.session.commit() 
    return jsonify({'message' : 'new review created'})

@app.route('/get_my_reviews', methods=['GET'])
@token_required
def get_my_reviews(current_user):
    reviews = Review.query.filter_by(user_id=current_user.id).all()
    reviews_list = []
    for review in reviews:
        review_data = {}
        review_data['id'] = review.id
        review_data['bookId'] = review.book_id
        review_data['userId'] = review.user_id
        review_data['isPublic'] = review.is_public
        review_data['text'] = review.text
        review_data['rating'] = review.rating
        review_data['score'] = review.score
        reviews_list.append(review_data)
        
    return jsonify({'myReviews': reviews_list})

@app.route('/appreciate_review/<int:reviewId>', methods=['POST'])
@token_required
def appreciate_review(current_user, reviewId):
    data = request.get_json()
    review_like_exists = ReviewLikes.query.filter_by(review_id=reviewId, user_id=current_user.id).first()
    if review_like_exists:
        if review_like_exists.like != data['like']:
            review = Review.query.filter_by(id=reviewId).first()
            review.score += 1 if data['like'] == True else -1
            review_like_exists.like = data['like']
    else:
        new_review_like = ReviewLikes(review_id=reviewId, user_id=current_user.id, like=data['like'])
        review = Review.query.filter_by(id=reviewId).first()
        review.score += 1 if data['like'] == True else -1
        db.session.add(new_review_like)  
    db.session.commit() 
    return jsonify({'message' : 'new (dis)like for review added'})

@app.route('/top_reviews', methods=['GET'])
def top_reviews():
    reviews = Review.query.filter_by(is_public=True).order_by(Review.score.desc()).limit(3).all()
    reviews_list = []
    for review in reviews:
        user = User.query.filter_by(id=review.user_id).first()
        review_data = {}
        review_data['id'] = review.id
        review_data['bookId'] = review.book_id
        review_data['userName'] = user.user_name
        review_data['isPublic'] = review.is_public
        review_data['text'] = review.text
        review_data['rating'] = review.rating
        review_data['score'] = review.score
        reviews_list.append(review_data)

    return jsonify({'topReviews': reviews_list})

@app.route('/book_of_the_week', methods=['GET'])
def book_of_the_week():
    now = datetime.now()
    book_of_week = BookOfTheWeek.query.filter(BookOfTheWeek.start_date<=now).order_by(BookOfTheWeek.start_date.desc()).first()
    book_data = {}

    if now.weekday():
        book_data['sendMessage'] = False
        book_data['time'] = (book_of_week.start_date + timedelta(days=6)).timestamp()
    else:
        book_data['sendMessage'] = True
        book_data['time'] = (book_of_week.start_date + timedelta(days=7)).timestamp()

    book = Book.query.filter_by(id=book_of_week.book_id).first()
    book_data['name'] = book.name
    book_data['bookId'] = book.id
    
    return jsonify({"bookData": book_data})

@app.route('/chat', methods=['GET', 'POST'])
@token_required
def chat(current_user):
    if request.method == 'GET':
        messages_list = []
        now = datetime.now()
        book_of_week = BookOfTheWeek.query.filter(BookOfTheWeek.start_date<=now).order_by(BookOfTheWeek.start_date.desc()).first()
        messages = BlogMessage.query.filter_by(book_of_the_week_id=book_of_week.book_id).order_by(BlogMessage.id.asc())
        for m in messages:
            user = User.query.filter_by(id=m.user_id).first()
            message_data = {}
            message_data['userId'] = m.user_id
            message_data['userName'] = user.user_name
            message_data['message'] = m.message
            messages_list.append(message_data)
        messages_list.reverse()
        return jsonify({"chat": messages_list})
    else:
        now = datetime.now()
        book_of_week = BookOfTheWeek.query.filter(BookOfTheWeek.start_date<=now).order_by(BookOfTheWeek.start_date.asc()).first()
        data = request.get_json()
        newMessage = BlogMessage(book_of_the_week_id=book_of_week.id, user_id=current_user.id, message=data['message'])
        db.session.add(newMessage)
        db.session.commit()
        return jsonify({"message": "message added to chat!"})

if  __name__ == '__main__': 
    app.run(debug=True)