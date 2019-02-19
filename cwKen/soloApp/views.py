from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# default music root
def music(request):
    return HttpResponse("This is a bad request!")

# singer number 1 with snippet of info
def John_Legend(request):
    return HttpResponse("John Roger Stephens (born December 28, 1978), known professionally as John Legend")
# singer number 2 with snippet of info
def Brain_Mcknight (request):
    return HttpResponse("Brian McKnight is an American R&B singer-songwriter, arranger, producer, and musician.")
# rapper number 3 with snippet of info
def Lil_Wayne (request):
    return HttpResponse("Dwayne Michael Carter Jr., known professionally as Lil Wayne, is an American rapper.")