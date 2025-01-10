## accounts는 정배님 파일입니다.
---
## 프로필 부분도 포스트맨으로 확인하니 팔로우 등록 및 취소와 본인의 프로필에서 팔로우와 팔로워 확인도 정상적이였습니다.
---
## main 페이지는 승진님 파일 입니다.
---
## 기존 URL은 "http://127.0.0.1:8000/main/" 작성해야 메인페이지로 이동 되었는데 이러면 기존 article과 user와 다른 게 없어보여 네이버도 https://www.naver.com/를 하면 바로 메인 페이지가 뜨는 것 처럼 url 주소를 바꿔서 http://127.0.0.1:8000/를 쳐도 main 페이지로 이동되게 했습니다.
---
## 비밀 번호 기능 추가하였습니다.
---
## 게시글과 댓글 좋아요 기능 추가와 프로필에서 어떤 게시글과 댓글에 좋아요 했는지 확인가능하게 하였습니다.
---
## 게시글과 댓글 좋아요를 한 목록들을 프로필에서 볼 때 제공되는 정보의 종류를 수정했습니다.


#### 게시글 좋아요의 기존 정보 목록:
- 게시글 제목
- 이미지
- 평점
- 작성자 고유 ID(author_id)

#### 게시글 좋아요의 바뀐 정보 목록:
- 게시글 제목
- 영화 제목
- 이미지
- 평점
- 작성자 닉네임(username)


#### 댓글 좋아요의 기존 정보 목록:
- 댓글을 작성한 게시글 제목
- 작성일
- 작성 내용

#### 게시글 좋아요의 바뀐 정보 목록:
- 댓글을 작성한 게시글 제목
- 작성일
- 작성 내용
- 작성자 닉네임(username)

---
## AI앱의 models.py 생성했습니다. 필드는 serializers.py에서 user_question(사용자 질문) 필드만 가져다가 처리하여 사용자 질문이 form-data로 같이 들어오면 결과를 serializers.py에서 처리하면 되지 않을까 싶습니다. 
---
## 이전에는 게시글 상세 조회하면 해당 게시글에 작성된 댓글을 보려면 다른 방식을 사용해야 해당 게시글에 적힌 댓글 정보를 제공했지만 수정 된 코드는 게시글을 상세 조회하면 해당 게시글에 작성된 댓글도 같이 제공되도록 수정함
---
## 게시글 상세 페이지를 누르면 30분마다 조회수가 증가하도록 기능 추가
---
## 게시글 상세 페이지를 누르면 게시글 및 댓글에 받은 좋아요 수의 총 개수를 표시하도록 기능 추가
---
## 가상환경 문제로 파일 못 쓸 뻔 하다가 미리 백업해둔 파일로 복구함
---