from pprint import pprint
from flask_app import app, render_template, redirect, request, session
from flask_app.model.user_model import User
# @app.route('/')
# def index():
#     return redirect ('/users/new')

# @app.route('/users/new')
# def new_user():
#     return render_template('create.html')

# @app.post('/users')
# def insert_info():
#     session['first_name']= request.form['first_name']
#     session['last_name']= request.form['last_name']
#     session['email']= request.form['email']
#     # return takes in a route only
#     return redirect('/users')


# @app.get('/users')
# def result():
#     return render_template('result.html')

@app.route('/')
def index():
    return redirect ('/users/new')

# display form to create a user
@app.get('/users/new')
def new_user():
    return render_template('new_user.html')

# process form and create a user
@app.post('/users')
def create_user():
    data = {
        # 'id ': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    user_id = User.save(data)
    print(f'**** CREATED - USER ID: {user_id} ****')
    return redirect('/users')


# display all users
@app.get('/users')
def all_users():
    users = User.find_all()
    print(f'**** FOUND - ALL USERS: ****')
    pprint(users)
    return render_template('all_users.html', users = users)



# display one user by id
@app.get('/users/<int:user_id>')
def one_user(user_id):
    data = {
        'id': user_id
    }
    user = User.find_by_id(data)
    print(f'**** FOUND - USER ID: {user.id} ****')
    return render_template('one_user.html', user = user)

# process form and update a user by id
@app.post('/users/<int:user_id>/update')
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.find_by_id_and_update(data)
    print(f'**** UPDATED - USER ID: {user_id} ****')
    return redirect(f'/users/{user_id}')



# display form to edit a user by id
@app.get('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        'id': user_id
    }
    user = User.find_by_id(data)
    print(f'**** FOUND - USER ID: {user.id} ****')
    return render_template('edit_user.html', user = user)




# delete one user by id
@app.get('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.find_by_id_and_delete(data)
    print(f'**** DELETED - USER ID: {user_id} ****')
    return redirect('/users')