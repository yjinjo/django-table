from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from third.models import Restaurant, Review
from third.forms import RestaurantForm, ReviewForm
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


def detail(request, id):  # restaurant의 id (pk)를 직접 url path parameter을 통해 전달 받습니다."
    if id:
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, "third/detail.html", {"item": item, "reviews": reviews})
    # 만약 id가 없는 경우(예를 들어 새로운 글 post등), 리스트 화면으로 넘어갑니다.
    return HttpResponseRedirect("/third/list/")


def delete(request):
    if "id" in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get("id"))
        item.delete()
    return HttpResponseRedirect("/third/list")


def review_create(request, restaurant_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)  #
        if form.is_valid():  # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
            form.save()  # save 메소드로 입력받은 데이터를 레코드로 추가합니다.
        return redirect("restaurant-detail", id=restaurant_id)  # 전화면으로 이동합니다.

    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={"restaurant": item})
    return render(request, "third/review_create.html", {"form": form, "item": item})


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()
    return redirect("restaurant-detail", id=restaurant_id)  # 전 화면으로 이동합니다.


def review_list(request):
    reviews = (
        Review.objects.all().select_related().order_by("-created_at")
    )  # 모든 리뷰를 받은 다음에 최신순으로 정렬합니다.
    paginator = Paginator(reviews, 10)  # 한 페이지에 10개씩 표시합니다.

    page = request.GET.get("page")  # query params에서 page 데이터를 가져옵니다.
    items = paginator.get_page(page)  # 해당 페이지의 아이템으로 필터링 합니다.

    context = {"reviews": items}
    return render(request, "third/review_list.html", context)
