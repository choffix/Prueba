from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('Date.html', {'current_date': now})

#Primera forma con templates#
#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse
#import datetime

#as def current_datetime(request):
 #   now = datetime.datetime.now()
 #   t = get_template('Date.html')
 #   html = t.render(Context({'current_date': now}))
 #   return HttpResponse(html)
#Sin Templates#
#from django.http import HttpResponse
#import datetime

#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>La Hora es... %s.</body></html>" % now
#   return HttpResponse(html)"""