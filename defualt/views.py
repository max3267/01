from django.shortcuts import render
from django.views.generic import ListView, DetailView,RedirectView,CreateView,UpdateView
from django.urls import reverse
from .models import *

# Create your views here.
class PollList(ListView):
    model = poll





class PollDetail(DetailView):
    model = poll

    def get_context_data(self, **kwargs):
      ctx = super().get_context_data(**kwargs)
      ctx['options'] = Option.objects.filter(poll_id=self.kwargs['pk'])
      return ctx

class Pollvote(RedirectView):
    def get_redirect_url(self, **kwargs):
        opt = Option.objects.get(id=self.kwargs['oid'])
        opt.count += 1
        opt.save()
        return "/poll/{}/".format(opt.poll_id)

class PollCreate(CreateView):
    modle = Poll
    fields = ['subject']
    success_url = "/poll/"

class PollUpdate(UpdateView):
    modle = Poll
    fields = ['subject']
    success_url = "/poll/"



class OptionCreate(CreateView):
    modle = option
    fields =['title']

    def get_success_url(self):
        #return '/poll/'+str(self.kwargs['pid']+'/'
        return reverse('poll_view', kwargs={'pk':self.kwargs['pid']})

    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['pid']
        return super().form_valid(form)


    