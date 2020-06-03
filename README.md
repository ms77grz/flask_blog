# flask_blog

export FLASK_APP=flaskblog.py
export FLASK_DEBUG=1

flask run

pip install email-validator

to generate a random secret key
import secrets
secrets.token_hex(16)
