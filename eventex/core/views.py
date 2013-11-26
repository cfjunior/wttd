# coding: utf-8

from django.shortcuts import render
#Dry
#from django.shortcuts import render_to_response
#from django.template import RequestContext

#from django.conf import settings

##from django.http import HttpResponse
##from django.template import loader,Context

# Create your views here.
def home(request):
    return render(request, 'index.html')
#Dry
#def home(request):
#    context = RequestContext(request)
#    return render_to_response('index.html',context)

#antes Dry
#def home(request):
#    context = {'STATIC_URL': settings.STATIC_URL}
#    return render_to_response('index.html',context)



##def home(request):
##    t = loader.get_template('index.html')
##    c = Context()
##   
##    content = t.render(c)
##    
##    return HttpResponse(content)

