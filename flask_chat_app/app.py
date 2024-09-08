from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from models import db, Message  # models.pyからインポート

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'  # データベース設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # FlaskアプリにSQLAlchemyを初期化

# アプリが起動するたびにデータベースとテーブルを作成する
with app.app_context():
    db.create_all()  # 追加: テーブルを作成

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # HTMLテンプレートを返す

@socketio.on('message')
def handle_message(data):
    new_message = Message(content=data)  # Messageオブジェクトを作成
    db.session.add(new_message)           # セッションに追加
    db.session.commit()                   # データベースに保存
    emit('response', data, broadcast=True)  # 他のクライアントにメッセージを送信

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
