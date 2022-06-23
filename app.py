from crypt import methods
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()
app = Flask(__name__)

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


def example():
   pass

# 로그인 기능 구현 영역 - 끝

###################################################################

# 회원가입 기능 구현 영역 - 시작

@app.route('/signup')
def signup():
   '''
   TODO - 김동영님 : 회원가입 페이지 함수

   이 함수는 회원가입 페이지를 렌더링하는 함수 입니다.

   회원가입 관련 기능은 아래에 작생해주세요!!

   '''
   return render_template('signup.html')


def example():
   pass

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
   posts = list(db.gallerys.find({},{'_id':False}))

   return render_template('home.html', posts=posts)

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

   address_receive = request.form['address']
   star_point_receive = request.form['star_point']
   title_receive = request.form['title']
   description_receive = request.form['description']
   link_receive = request.form['link']
   nickname_receive = request.form['nickname']
   img_url_receive = request.form['img_url']

   board_list = list(db.community.find({},{'_id':False}))
   count = len(board_list) + 1

   doc = {
       'num': count,
       'address': address_receive,
       'star_point': star_point_receive,
       'title': title_receive,
       'description': description_receive,
       'link': link_receive,
       'nickname': nickname_receive,
       'img_url': img_url_receive,
   }

   try:
      db.community.insert_one(doc)
      return jsonify({"result" : True})
   except:
      return jsonify({"result" : False})

# 게시글 생성 기능 구현 영역 - 끝

###################################################################

# 게시글 삭제 기능 구현 영역 - 시작

@app.route('/delete_board/<num>', methods=["DELETE"])
def delete_board():
   num = request.args.get("num")
   try:
      db.community.delete_one({'num' : int(num)})
      return jsonify({"result" : True})
   except:
      return jsonify({"result" : False})

# 게시글 삭제 기능 구현 영역 - 끝

###################################################################


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)