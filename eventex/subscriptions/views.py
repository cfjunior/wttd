# coding: utf-8

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


#def subscribe(request):
#    return HttpResponse()
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            obj = Subscription(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
        else:
            return render(request,
                          'subscriptions/subscription_form.html',
                          {'form': SubscriptionForm()})
     
    else:
        return render(request,
                      'subscriptions/subscription_form.html',
                      {'form': SubscriptionForm()})

def detail(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})

