from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from third.models import Restaurant
from third.forms import RestaurantForm
from django.http import HttpResponseRedirect


def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)  # 한 페이지에 5개씩 표시합니다.

    page = request.GET.get("page")  # query params에서 page 데이터를 가져옵니다.
    items = paginator.get_page(page)  # 해당 페이지의 아이템으로 필터링합니다.

    context = {"restaurants": items}
    return render(request, "third/list.html", context)


def create(request):
    if request.method == "POST":
        form = RestaurantForm(
            request.POST
        )  # request의 POST 데이터들을 바로 RestaurantForm에 담을 수 있습니다.
        if form.is_valid():  # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
            form.save()  # save 메소드로 입력받은 데이터를 레코드로 추가합니다.
        return HttpResponseRedirect("/third/list/")  # 리스트 화면으로 이동합니다.
    form = RestaurantForm()
    return render(request, "third/create.html", {"form": form})


def update(request):
    if request.method == "POST" and "id" in request.POST:
        # item = Restaurant.objects.get(pk=request.POST.get("id"))
        item = get_object_or_404(Restaurant, pk=request.POST.get("id"))
        form = RestaurantForm(request.POST, instance=item)  # instance 인자(수정대상) 지정

        if form.is_valid():
            form.save()
    elif "id" in request.GET:
        # item = Restaurant.objects.get(pk=request.GET.get("id"))
        item = get_object_or_404(Restaurant, pk=request.GET.get("id"))
        form = RestaurantForm(instance=item)
        return render(request, "third/update.html", {"form": form})

    return HttpResponseRedirect("/third/list/")
