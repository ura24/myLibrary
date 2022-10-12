from flask_app import db
from datetime import datetime


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)  # システムで使う番号
    title = db.Column(db.String(255))  # タイトル
    author = db.Column(db.String(255))  # 著者
    publisher = db.Column(db.String(255))  # 出版社
    page = db.Column(db.Integer) # ページ数
    category = db.Column(db.String(255))  # カテゴリー
    price = db.Column(db.Integer)  # 金額
    isbn = db.Column(db.Integer)  # isbnコード
    memo = db.Column(db.String(10000)) # 感想・メモ
    finished_at = db.Column(db.Date)  # 読了日
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.now)  # 登録日
    updated_at = db.Column(db.DateTime, nullable=False,default=datetime.now)  # 更新日