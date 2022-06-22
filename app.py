from flask import Flask, render_template
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
   return render_template('home.html')


def example():
   pass

# 게시글 조회 기능 구현 영역 - 끝

###################################################################

# 게시글 조회 기능 구현 영역 - 시작

@app.route('/input_board')
def input_board():
   '''
   TODO - 김선진 : 게시글 입력 페이지 함수

   이 함수는 게시글 입력 페이지를 렌더링하는 함수 입니다.

   게시글 조회 입력 기능은 아래에 작생해주세요!!

   '''
   return render_template('input_board.html')



def example():
   pass

# 게시글 조회 기능 구현 영역 - 끝

###################################################################


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)