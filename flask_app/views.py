from datetime import datetime, date, time
from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.book import Book
from flask_app import db


@app.route('/')
def home():
    books = Book.query.all()
    return render_template('flask_app/home.html', books=books)


@app.route('/book_add', methods=['GET', 'POST'])
def book_add():
    if request.method == 'GET':
        books = Book.query.all()
        return render_template('flask_app/book_add.html', books=books)
    if request.method == 'POST':
        form_title = request.form.get('title')
        form_publisher = request.form.get('publisher')
        form_author = request.form.get('author')
        form_category = request.form.get('category')
        form_price = request.form.get('price', type=int)
        form_page = request.form.get('page', type=int)
        form_isbn = request.form.get('isbn', type=int)
        form_memo = request.form.get('memo')
        form_finished_at = request.form.get('finished_at')
        book = Book(
            title=form_title,
            publisher=form_publisher,
            author=form_author,
            category=form_category,
            price=form_price,
            page=form_page,
            isbn=form_isbn,
            memo=form_memo,
            finished_at=form_finished_at,
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/<int:id>')
def book_detail(id):
    book = Book.query.get_or_404(id)
    return render_template('flask_app/book_detail.html', book=book)


@app.route('/<int:id>/edit', methods=['GET'])
def book_edit(id):
    book = Book.query.get(id)
    return render_template('flask_app/book_edit.html', book=book)


@app.route('/<int:id>/update', methods=['POST'])
def book_update(id):
    book = Book.query.get(id)
    book.title = request.form.get('title')
    book.author = request.form.get('author')
    book.publisher = request.form.get('publisher')
    book.category = request.form.get('category')
    book.price = request.form.get('price', type=int)
    book.page = request.form.get('page', type=int)
    book.isbn = request.form.get('isbn', type=int)
    book.memo = request.form.get('memo')
    # book.finished_at = datetime.now()
    book.finished_at = datetime.strptime(request.form.get('finished_at'), '%Y-%m-%d')
    book.updated_at = datetime.now()
    db.session.merge(book)
    db.session.commit()
    return redirect(url_for('home'))
