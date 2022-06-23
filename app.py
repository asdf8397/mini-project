from crypt import methods
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import certifi
import jwt
import datetime
import hashlib
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename

ca = certifi.where()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient("mongodb+srv://admin:emm05235@cluster0.umzeh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)

db = client.sparta

###################################################################

# 로그인 기능 구현 영역 - 시작

@app.route('/')
def signin():
   '''
   TODO - 김동영님 : 로그인 페이지 함수

   이 함수는 로그인 페이지를 렌더링하는 함수 입니다.

   로그인 관련 기능은 아래에 작생해주세요!!

   '''
   return render_template('signin.html')


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY,
                           algorithm='HS256')  # jwt는 암호화 해주는 코드: 암호화 jwt --- pyload값 id 또는 구분해주는 값으로 암호화된 값을 encording해주는 것
        # .decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

# 로그인 기능 구현 영역 - 끝

###################################################################

# 회원가입 기능 구현 영역 - 시작

@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,  # 아이디
        "password": password_hash,  # 비밀번호
        "profile_name": username_receive,  # 프로필 이름 기본값은 아이디
        "profile_pic": "",  # 프로필 사진 파일 이름
        "profile_pic_real": "profile_pics/profile_placeholder.png",  # 프로필 사진 기본 이미지
        "profile_info": ""  # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

# 회원가입 기능 구현 영역 - 끝

###################################################################

# 게시글 조회 기능 구현 영역 - 시작

@app.route('/home')
def home():
   '''
   TODO - 김선진 : 게시글 조회 페이지 함수

   이 함수는 게시글 조회 페이지를 렌더링하는 함수 입니다.

   게시글 조회 관련 기능은 아래에 작생해주세요!!

   '''

   token_receive = request.cookies.get('mytoken')

   try:
      payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
      username = payload["id"]
      posts = list(db.community.find({},{'_id':False}))
      return render_template('home.html', posts=posts)
   except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
      return redirect(url_for("/"))


# 게시글 조회 기능 구현 영역 - 끝

###################################################################

# 게시글 생성 기능 구현 영역 - 시작

@app.route('/input_board', methods=["GET"])
def input_board_page_render():
   '''
   TODO - 김선진 : 게시글 입력 페이지 함수

   이 함수는 게시글 입력 페이지를 렌더링하는 함수 입니다.

   게시글 조회 입력 기능은 아래에 작생해주세요!!

   '''
   return render_template('input_board.html')


@app.route('/input_board', methods=["POST"])
def input_board():

   print(request.form)
   
   address_receive = request.form['address']
   star_point_receive = request.form['star_point']
   title_receive = request.form['title']
   description_receive = request.form['description']
   link_receive = request.form['link']

   board_list = list(db.community.find({},{'_id':False}))
   count = len(board_list) + 1

   token_receive = request.cookies.get('mytoken')
   try:
      payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
      username = payload["id"]

      file = request.files["file"]
      filename = secure_filename(file.filename)
      extension = filename.split(".")[-1]
      file_path = f"profile_pics/{username}.{extension}"
      file.save("./static/" + file_path)

      doc = {
       'id': count,
       'address': address_receive,
       'star_point': star_point_receive,
       'title': title_receive,
       'description': description_receive,
       'link': link_receive,
       'nickname': username,
       'img_url': file_path,
      }
      db.community.insert_one(doc)
      return jsonify({"result" : True})
   except Exception as e:
      print(e)
      return jsonify({"result" : False})

# 게시글 생성 기능 구현 영역 - 끝

###################################################################

# 게시글 삭제 기능 구현 영역 - 시작

@app.route('/delete_board', methods=["DELETE"])
def delete_board():
   id = request.form["id"]
   nickname = request.form["nickname"]
   print(id, nickname)
   try:
      db.community.delete_one({'id' : int(id), "nickname":nickname})
      return jsonify({"result" : True})
   except Exception as e:
      print(e)
      return jsonify({"result" : False})

# 게시글 삭제 기능 구현 영역 - 끝

###################################################################


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)