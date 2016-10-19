from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'activity' in request.session:
        request.session['activity'] = []
    return render(request, "ninjagold/index.html")

def process_money(request, building):
    context = {
        'farm' :random.randint(10,20),
        'cave' :random.randint(5,10),
        'house' :random.randint(2,5),
        'casino' :random.randint(-50,50)
    }
    if building in context:
        result = context[building]
        request.session['gold'] = request.session['gold'] + result
        time = datetime.strftime(datetime.now(), '%Y-%m-%d %I:%M:%S %p')
        result_dictionary = {
            'class': "green" if result > 0 else "red",
            'activity': "You went to the {} and {} {} gold! at {}".format(building, "lost" if result < 0 else "gained", result, time)
        }
        request.session['activity'].append(result_dictionary)
        return redirect('/', building)

def reset(request):
    if request.method == "POST":
        del request.session['gold']
        del request.session['activity']
    return redirect ('/')
