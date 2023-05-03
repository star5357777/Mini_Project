from django.shortcuts import render
import bcrypt
from .models import account
def main(request):
    #이걸 로그인 되게 만들어야 함
    #로그인 페이지 받아옴
    if request.method == 'GET':
     return render(request, 'main.html')
    elif request.method == 'POST':
        # 이 것을 가지고 메시지를 나오게 할 수 있음
        res_data = {}
        # db user 테이블
        get_user = account()

        # user , 비밀번호 가져옴
        Username = request.POST.get('Username', None)
        wcpassword = request.POST.get('password', None)
        if Username and wcpassword :
              try:
                  # db를 지정해주니까 갈 수 있는듯
                  User =  account.objects.get(Username = Username)
              except User.DoesNotExist:
              #except User.DoesNotExist:
               res_data['error'] = '사용자 아이디가 없음'
               return

              if not bcrypt.checkpw(wcpassword.encode('utf-8'), User.password.encode("utf-8")):
                   res_data['error'] = '사용자 비밀번호가 틀림'
              else:
                   res_data['error'] = '로그인 성공'
              return render(request, "main.html", res_data)
# Create your views here.
def signup(request):
    # 그냥 페이지 불러 오는듯
    if request.method == 'GET':
        return render(request, 'signup.html')
    # 여기부터 회원 가입 데이터를 쌓는거
    elif request.method == 'POST':
        # 이 것을 가지고 메시지를 나오게 할 수 있음
        res_data = {}
        # account db 변수 설정?
        new_user = account()
        # 요청을 가져옴
        new_user.Username = request.POST.get('Username', None)
        wcpassword1 = request.POST.get('password1', None)
        wcpassword2 = request.POST.get('password2', None)
        #비밀번호 불일치 할 때
        if wcpassword1 != wcpassword2:
            res_data['error'] = '비밀번호 불일치'

        else:
            # 암호 해쉬 화 .decode를 붙여야 나중에 로그인시 invaild salt를 피함
            hashed_password = bcrypt.hashpw(wcpassword1.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
            # 암호 변수 저장
            new_user.password = hashed_password
            # 이게 저장 하는 것을 의미
            new_user.save()
            # res_data가 있어야 쌓이는듯?
        return render(request, 'signup.html', res_data)
