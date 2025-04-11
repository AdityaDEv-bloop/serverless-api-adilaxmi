from models.user import User,engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# ===================================================================================
# CREATE

# If there is data in the database, dont add more data
print('Count of total Users are', session.query(User).count())
if session.query(User).count() < 1:
    # Create one new User
    user = User(name='admin', phone="+916290873065",email = "admin@admin.com", password = '#Aditya220192')
    session.add(user)
    session.commit()

# ===================================================================================
# READ
# query all users
users = session.query(User).all()
print(users)

user = session.query(User).filter_by(id=1).one_or_none()
print(user)

# Get first user from the data
user_first = session.query(User).first()
print('First User: ', user_first)