from django.shortcuts import render

# Create your views here.
def cometchat_view(request):
       return render(request, 'cometchat/index.html')

