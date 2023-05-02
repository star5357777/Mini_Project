from django.shortcuts import render
import bcrypt
def main(request):
    return render(request, 'main.html')
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
        # 암호 해쉬화 변수 저장
        if not (new_user.Username and wcpassword1 and wcpassword2):
            res_data['error'] = '모든 값을 입력 필요'

        elif wcpassword1 != wcpassword2:
            res_data['error'] = '비밀번호 불일치'

        else:
            # 암호 해쉬 화
            hashed_password = bcrypt.hashpw(wcpassword1.encode("utf-8"), bcrypt.gensalt())
            # 암호 변수 저장
            new_user.password = hashed_password
            # 이게 저장 하는 것을 의미
            new_user.save()
            # Username = request.Get.get('Username', None)
            # password = request.Get.get('password', None)
            # res_data가 있어야 쌓이는듯?
        return render(request, 'account_pg.html', res_data)
