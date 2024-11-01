from django.shortcuts import render
from datetime import datetime, timedelta
import python_weather

# Create your views here.
def index(request):

    today = datetime.now()

    # dates will be an empty array
    dates = []

    for i in range(-2, 3):
        date = today + timedelta(days=i)
        print(date.strftime('%A'))
        dates.append({
            'day': date.day,
            'month': date.strftime('%b'),
            'weekday': date.strftime('%A')
        })

    context = {
        'dates': dates
    }

    return render(request, 'index.html', context)