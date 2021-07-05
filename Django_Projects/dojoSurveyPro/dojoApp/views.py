from django.shortcuts import render
LANG = (
    "python","MERN", "HTML","Java"
)
LOC = (
    "San Jose","LA", "Alington", "Tulsa", "Chicago"
)
def index(request):
    context={
        "locations": LOC,
        "languages":LANG
        }

    return render(request, 'index.html', context)

def results(request):
    print(request.POST)

    print(request.POST['name'])
    print(request.POST['location'])
    print(request.POST['language'])
    print(request.POST['comments'])

    context = {
        "theirName": request.POST['name'],
        "theirLocation": request.POST['location'],
        "theirLanguage": request.POST['language'],
        "thierComments": request.POST['comments']
    }

    return render(request, "results.html", context)