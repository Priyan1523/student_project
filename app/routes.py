from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Room, MessReview, ForumPost, RoommateFeedback

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('base.html')

# Feature 1: Registration & Login
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username pehle se exist karta hai!')
            return redirect(url_for('main.register'))
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('main.profile'))
        flash('Sahi credentials dalein!')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

# Feature 1 & 8: Profile and Feedback Handling
@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        if 'update_profile' in request.form:
            current_user.full_name = request.form.get('full_name')
            current_user.course = request.form.get('course')
            current_user.location = request.form.get('location')
            current_user.food_habit = request.form.get('food_habit')
            current_user.smoking_preference = request.form.get('smoking_preference')
            current_user.study_habit = request.form.get('study_habit')
            current_user.bio = request.form.get('bio')
            db.session.commit()
            flash('Profile update ho gayi!')
        elif 'submit_feedback' in request.form:  # Feature 8 integrated
            fb = RoommateFeedback(
                target_user_id=int(request.form['target_user_id']),
                rating=int(request.form['rating']),
                feedback_text=request.form['feedback_text']
            )
            db.session.add(fb)
            db.session.commit()
            flash('Anonymous feedback submit ho gaya!')
    users = User.query.filter(User.id != current_user.id).all()
    feedbacks = RoommateFeedback.query.filter_by(target_user_id=current_user.id).all()
    return render_template('profile.html', users=users, feedbacks=feedbacks)

# Feature 2: Listings
@main.route('/rooms')
def rooms():
    query = request.args.get('search', '')
    if query:
        all_rooms = Room.query.filter(Room.location.contains(query) | Room.title.contains(query)).all()
    else:
        all_rooms = Room.query.all()
    return render_template('rooms.html', rooms=all_rooms)

# Feature 3: Roommate Finder
@main.route('/roommates')
@login_required
def roommates():
    matches = User.query.filter(
        User.id != current_user.id,
        (User.food_habit == current_user.food_habit) | 
        (User.smoking_preference == current_user.smoking_preference) |
        (User.study_habit == current_user.study_habit)
    ).all()
    return render_template('roommates.html', matches=matches)

# Feature 4: Mess Reviews
@main.route('/mess', methods=['GET', 'POST'])
@login_required
def mess():
    if request.method == 'POST':
        review = MessReview(
            user_id=current_user.id,
            mess_name=request.form['mess_name'],
            rating=int(request.form['rating']),
            hygiene_rating=int(request.form['hygiene_rating']),
            review_text=request.form['review_text']
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('main.mess'))
    reviews = MessReview.query.all()
    return render_template('mess.html', reviews=reviews)

# Feature 5 & 6: Forum & Complaints
@main.route('/forum', methods=['GET', 'POST'])
@login_required
def forum():
    if request.method == 'POST':
        post = ForumPost(
            user_id=current_user.id,
            category=request.form.get('category', 'Discussion'),
            title=request.form['title'],
            content=request.form['content']
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created!')
        return redirect(url_for('main.forum'))
    posts = ForumPost.query.order_by(ForumPost.created_at.desc()).all()
    return render_template('forum.html', posts=posts)

# Feature 7: Guides
@main.route('/resources')
def resources():
    return render_template('resources.html')

# Feature 9: Transport & Local Services
@main.route('/local-info')
def local_info():
    return render_template('local_info.html')