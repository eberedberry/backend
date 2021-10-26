from django.shortcuts import render, HttpResponse

# Create your views here.
def test_view(request):
    # return HttpResponse("I am avery nice view")
    # print(request.user)
    return render(request, "test.html")

def homepage_view(request):
    return HttpResponse("I am hope page")
