from django.shortcuts import render
from sungjuk.forms import SungJukForm

def sungjuk(request):
    if request.method == 'GET' :
        return render(request, 'sungjuk/sungjuk_test.html')
    elif request.method == 'POST':
        form =SungJukForm(request.POST)
        sj = form.save(commit=False)
        sum = int(form['kor'].value()) + int(form['eng'].value()) \
              + int(form['mat'].value())
        avg = sum / 3
        grd = '가'
        if avg >= 90:
            grd = '수'
        elif avg >= 80:
            grd = '우'
        elif avg >= 70:
            grd = '미'
        elif avg >= 60:
            grd = '양'

        # 처리한 결과를 form 변수에 추가
        sj.tot = sum
        sj.avg = avg
        sj.grd = grd

        # 파생데이터를 form에 추가한 뒤에야
        # 비로소 save 함수 호출
        # sj.save()
        sj.save(using='mariadb')

        # 폼데이터와 처리결과를 dict 변수에 저장
        context = {'form': sj}
        return render(request, 'sungjuk/sungjuk_test.html', context)