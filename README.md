# flask_blog
```bash
export FLASK_APP=flaskblog.py
export FLASK_DEBUG=1

flask run

pip install email-validator
```
### to generate a random secret key
```bash
import secrets
secrets.token_hex(16)
```
## Part 4 - Database with Flask-SQLAlchemy
```bash
db.create_all()
from flaskblog import User, Post
user_1 = User(username='Corey', email='C@demo.com', password='password')
user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
db.session.add(user_1)
db.session.add(user_2)
db.session.commit()
```
```bash
User.query.all()
[User('Corey', 'C@demo.com', 'default.jpg'), User('JohnDoe', 'jd@demo.com', 'default.jpg')]
User.query.first()
User('Corey', 'C@demo.com', 'default.jpg')
User.query.filter_by(username='Corey').all()
[User('Corey', 'C@demo.com', 'default.jpg')]
User.query.filter_by(username='Corey').first()
User('Corey', 'C@demo.com', 'default.jpg')
```
```bash
user = User.query.filter_by(username='Corey').first()
user
User('Corey', 'C@demo.com', 'default.jpg')
usrr.id
1
user = User.query.get(1)
user
User('Corey', 'C@demo.com', 'default.jpg')
```
```bash
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
```
```bash
post = Post.query.first()
post
Post('Blog 1', '2020-06-03 13:52:05.572596')
post.author
User('Corey', 'C@demo.com', 'default.jpg')
```
```bash
db.drop_all()
db.create_all()
User.query.all()
[]
Post.query.all()
[]
```
## Part 9 - Pagination
```bash
posts = Post.query.paginate()
posts.per_page
20
posts.page
1
for post in posts.items:
    print(post)
```

```bash
posts = Post.query.paginate(page=2)
posts.page
2
for post in posts.items:
    print(post)
```

```bash
posts = Post.query.paginate(per_page=5)
for post in posts.items:
    print(post)
posts.page
1
```

```bash
posts = Post.query.paginate(per_page=5, page=2)
posts.page
2
for post in posts.items:
    print(post)

posts.total
27
```
#### http://127.0.0.1:5000/?page=2

```bash
posts = Post.query.paginate(per_page=2, page=6)
for page in posts.iter_pages():
    print(page)
```

```html
...
{% for page_num in posts.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2) %}
...
```

```python
posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
```
## Part 10 - Email and Password Reset

```bash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
s = Serializer('secret', 30)
token = s.dumps({'user_id': 1}).decode('utf-8')
token
'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5MTY5MDQ0MiwiZXhwIjoxNTkxNjkwNDcyfQ.eyJ1c2VyX2lkIjoxfQ.M0qgbNs0Kin5Hqqnq3GNYHtmvrs3XeFvAXei06fyerIJ8YOz_VmAZ28Hrgsis5ot87yIBhjX0wcTJV7ikYFmew'
```

```
s.loads(token)
{'user_id': 1}
// after 30 seconds
s.loads(token)
...
itsdangerous.exc.SignatureExpired: Signature expired
```

## Part 10 - Email and Password Reset

```bash
pip install flask-mail
```
#### add into \__init\__.py:
```python
...
import flask_mail as Mail

...
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)
```

```bash
vim ~/.bashrc-personal
export EMAIL_USER="your_username@gmail.com"
export EMAIL_PASS="your_password"

source .bashrc-personal 
```
