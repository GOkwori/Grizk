from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def custom_404(request, exception):
    """ Custom 404 error handler """
    return render(request, '404.html', status=404)


def custom_500(request):
    """ Custom 500 error handler """
    return render(request, '500.html', status=500)


def custom_403(request, exception):
    """ Custom 403 error handler """
    return render(request, '403.html', status=403)
