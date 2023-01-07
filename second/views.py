from django.shortcuts import render
from django.http import HttpResponseRedirect
from second.models import Post
from .forms import PostForm


# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    form = PostForm()  # 인스턴스 생성
    return render(request, 'second/create.html', {'form': form})


def confirm(request):
    # request의 POST 데이터들을 바로 PostForm에 담을 수 있습니다.
    form = PostForm(request.POST)

    # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
    if form.is_valid():
        return render(request, 'second/confirm.html', {'form': form})
    # 데이터가 유효하지 않으면 다시 입력하는 form으로 되돌아갑니다.
    return HttpResponseRedirect('/second/create/')
