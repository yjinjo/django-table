from django.shortcuts import render
from datetime import datetime

import random


# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def result(request):
    chosen = int(request.GET['number'])  # number 라는 값으로 전달 받은 데이터를 꺼내옵니다.

    results = []
    # 만약 수가 범위를 초과 하지 않으면 결과 값에 미리 선택한 수를 넣습니다.
    if 1 <= chosen <= 45:
        results.append(chosen)

    # 값을 꺼낼 박스를 마련합니다.
    box = []
    for num in range(1, 46):
        if num != chosen:  # 사용자가 선택하지 않은 값만 박스에 넣습니다.
            box.append(num)

    # 랜덤하게 뒤섞습니다.
    random.shuffle(box)

    # results 개수가 6개가 될 때 까지 값을 하나씩 꺼냅니다.
    while len(results) < 6:
        results.append(box.pop())

    context = {'numbers': results}
    return render(request, 'first/result.html', context)
