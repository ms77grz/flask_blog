# flask_blog

export FLASK_APP=flaskblog.py
export FLASK_DEBUG=1

flask run

pip install email-validator

to generate a random secret key
import secrets
secrets.token_hex(16)

Part 4 - Database with Flask-SQLAlchemy
db.create_all()
from flaskblog import User, Post
user_1 = User(username='Corey', email='C@demo.com', password='password')
user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
db.session.add(user_1)
db.session.add(user_2)
db.session.commit()

User.query.all()
[User('Corey', 'C@demo.com', 'default.jpg'), User('JohnDoe', 'jd@demo.com', 'default.jpg')]
User.query.first()
User('Corey', 'C@demo.com', 'default.jpg')
User.query.filter_by(username='Corey').all()
[User('Corey', 'C@demo.com', 'default.jpg')]
User.query.filter_by(username='Corey').first()
User('Corey', 'C@demo.com', 'default.jpg')

user = User.query.filter_by(username='Corey').first()
user
User('Corey', 'C@demo.com', 'default.jpg')
usrr.id
1
user = User.query.get(1)
user
User('Corey', 'C@demo.com', 'default.jpg')

user.posts
[]
post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()
user.posts
[Post('Blog 1', '2020-06-03 13:52:05.572596'), Post('Blog 2', '2020-06-03 13:52:05.573070')]
for post in user.posts:
    print(post.title)
Blog 1
Blog 2

post = Post.query.first()
post
Post('Blog 1', '2020-06-03 13:52:05.572596')
post.author
User('Corey', 'C@demo.com', 'default.jpg')

db.drop_all()
db.create_all()
User.query.all()
[]
Post.query.all()
[]
