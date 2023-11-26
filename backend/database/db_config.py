```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

# Update the below fields as per your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```