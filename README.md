# [Chapter 1] 10조 S.A(Starting Assignment) - 부동산 관련 커뮤니티

</br>

### 설명 : 부동산 거래앱의 허위 매물 방지를 위해 별점과 거래 후기를 남기는 커뮤니티입니다.

</br>

## 🧑‍💻 Member
<div align="center">

| 🧑 팀장 | 🧑 팀원 | 🧑 팀원 |
| :---: | :---: | :---: |
| [<img src= "https://github.com/KumohDaseong/2021_SwBank/blob/main/readme_img/kimseonjin.png" width = "200">](https://github.com/gimseonjin)| [<img src="https://avatars.githubusercontent.com/u/81272109?v=4" width = "200">](https://github.com/asdf8397)| [<img src="https://avatars.githubusercontent.com/u/107820634?v=4" width = "200" >](https://github.com/kangyunmi)|
| 김선진 | 김동영 | 강윤미 |
 


</div>

## 선정 이유

### 1. 부동산 거래 앱의 허위 매물이 많다!

실제 다방, 직방 같은 온라인 부동산 거래 플랫폼에 보면 허위 매물이 많다. 

그러나 이를 공유할 수 있는 커뮤니티나 플랫폼이 없어서 관련 정보를 찾기가 어렵다.

따라서 부동산 관련 허위 매물 및 기타 정보를 공유할 수 있는 커뮤니티를 구현하고자 한다.

![Untitled](https://user-images.githubusercontent.com/66009926/174543867-d4e9589e-62b5-43f9-b489-08efdea41c18.png)

# 와이어 프레임

# 상세 기능

| 기능 명 | Method | URL | Request | Response |
| --- | --- | --- | --- | --- |
| 로그인 기능 | POST | /signin | {
    “id” : string,
    “pw” : string
} | {
    “result” : 0 or 1
} |
| 회원가입 기능 | POST | /signup | {
    “id” : string,
    “pw” : string,
    “nickname” : string
} | {
    “result” : 0 or 1
} |
| 게시글 조회 | GET | /posts | {
    “address” : string
} | {
   “posts” : [ ] 
} |
| 게시글 상세 조회 | GET | /posts/{id} | {
    “id” : integer
} | {

”id” : integer, 

“address” : string,

“star_point” : integer,

“title” : string,

“description” : string,

“link” : string,

”nickname” : string

} |
| 게시글 등록 | POST | /posts | {

“address” : string,

“star_point” : integer,

“title” : string,

“description” : string,

“link” : string,

”nickname” : string

} | {
    “result” : 0 or 1
} |
| 게시글 삭제 | DELETE | /posts/{id} | {
    “id” : integer,
    “nickname” : string
} | {
    “result” : 0 or 1
} |

