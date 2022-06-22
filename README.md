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

## 💻 Skill Set
<div align="center">

| Front | Back | Database | Infra |
| :---: | :---: | :---: | :---: |
| [<img src= "https://images.velog.io/images/offdutybyblo/post/65c734fd-077c-4a68-8b3b-557c52428511/htmljscss.jpeg" width = "200">]| [<img src="https://images.velog.io/images/new_wisdom/post/4a0259ee-b980-484b-8bf4-25eb4705459f/flask.png" width = "200">]| [<img src="https://t1.daumcdn.net/cfile/tistory/9923593359840EC50A" width = "200" >]| [<img src="http://wildpup.cafe24.com/wp-content/uploads/2014/12/ec2.png" width = "200" >]|
| html,css,javascript | Flask | Mongo DB | AWS EC2 |
 
</div>

## 선정 이유

### 1. 부동산 거래 앱의 허위 매물이 많다!

실제 다방, 직방 같은 온라인 부동산 거래 플랫폼에 보면 허위 매물이 많다. 

그러나 이를 공유할 수 있는 커뮤니티나 플랫폼이 없어서 관련 정보를 찾기가 어렵다.

따라서 부동산 관련 허위 매물 및 기타 정보를 공유할 수 있는 커뮤니티를 구현하고자 한다.

![Untitled](https://user-images.githubusercontent.com/66009926/174543867-d4e9589e-62b5-43f9-b489-08efdea41c18.png)

# 와이어 프레임

![Slide1](https://user-images.githubusercontent.com/66009926/174580256-28ad6745-c79a-4715-98de-b094d28d78fd.jpg)
![Slide2](https://user-images.githubusercontent.com/66009926/174580271-8823a247-7312-4373-87fd-74cbcefb5c46.jpg)
![Slide3](https://user-images.githubusercontent.com/66009926/174580275-5c4fa344-8d86-4d06-af8e-b966e95bd552.jpg)
![Slide4](https://user-images.githubusercontent.com/66009926/174580277-8b7d602c-1054-4dfb-8e6f-77c5f14960f7.jpg)


# 상세 기능

| 기능 명 | Method | URL | Request | Response |
| --- | --- | --- | --- | --- |
| 로그인 기능 | POST | /signin | { </br> &nbsp;&nbsp;&nbsp;&nbsp;“id” : string, </br> &nbsp;&nbsp;&nbsp;&nbsp;“pw” : string </br>} | { </br> &nbsp;&nbsp;&nbsp; &nbsp;“result” : 0 or 1 </br>} |
| 회원가입 기능 | POST | /signup | {</br> &nbsp;&nbsp;&nbsp; &nbsp;“id” : string,</br> &nbsp;&nbsp;&nbsp; &nbsp;“pw” : string,</br> &nbsp;&nbsp;&nbsp; &nbsp;“nickname” : string</br>} | { </br> &nbsp;&nbsp;&nbsp; &nbsp;“result” : 0 or 1 </br>} |
| 게시글 조회 | GET | /posts | {</br> &nbsp;&nbsp;&nbsp; &nbsp; “address” : string</br>} | {</br> &nbsp;&nbsp;&nbsp; &nbsp;“posts” : [ ] </br>} |
| 게시글 등록 | POST | /posts | {</br> &nbsp;&nbsp;&nbsp; &nbsp; “address” : string, </br> &nbsp;&nbsp;&nbsp; &nbsp; “star_point” : integer, </br> &nbsp;&nbsp;&nbsp; &nbsp; “title” : string, </br> &nbsp;&nbsp;&nbsp; &nbsp; “description” : string, </br> &nbsp;&nbsp;&nbsp; &nbsp; “link” : string, </br> &nbsp;&nbsp;&nbsp; &nbsp; ”nickname” : string </br>} | {</br> &nbsp;&nbsp;&nbsp; &nbsp;“result” : 0 or 1</br>} |
| 게시글 삭제 | DELETE | /posts/{id} | {</br> &nbsp;&nbsp;&nbsp; &nbsp;“id” : integer,</br> &nbsp;&nbsp;&nbsp; &nbsp;“nickname” : string </br>} | {</br> &nbsp;&nbsp;&nbsp; &nbsp;“result” : 0 or 1</br>} |
