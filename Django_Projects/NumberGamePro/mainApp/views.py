from django.shortcuts import render, redirect
import random
def index(request):
    if 'answer' not in request.session:
        request.session['answer'] = random.randint(1, 10)
    if 'too_low' not in request.session:
        request.session['too_low'] = None
    if 'too_high' not in request.session:
        request.session['too_high'] = None
    if 'correct' not in request.session:
        request.session['correct'] = None

    context = {
        'too_low': request.session['too_low'],
        'too_high': request.session['too_high'],
        'correct': request.session['correct'],
    }
    return render(request, 'index.html', context)

def guess(request):
    request.session['too_low'] = False
    request.session['too_high'] = False
    request.session['correct'] = False

    if (int(request.POST['guess']) < request.session['answer']):
        request.session['too_low'] = True

    elif (int(request.POST['guess']) > request.session['answer']):
        request.session['too_high'] = True

    else:
        request.session['correct'] = True

    return redirect('/')

def delete(request):
    request.session.flush()
    return redirect('/')
