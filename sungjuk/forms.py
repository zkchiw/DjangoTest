from django.forms import ModelForm
from sungjuk.models import SungJuk

class SungJukForm(ModelForm):
    class Meta:
        model = SungJuk
        fields = ['name','kor','eng','mat']  # 폼 입력필드 정의
