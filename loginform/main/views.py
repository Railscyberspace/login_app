from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404
#from django.template import loader
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #Templates = loader.get_Templates('main/index.html')
    context = {
        'latest_question_list': latest_question_list}
    #output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, 'main/index.html', context)

def detail(request ,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request, 'main/detail.html', {'question': question})
 
def results(request, question_id): 
     response = "You are looking at the results of question %s. "
     return HttpResponse(response % question_id)
 
def vote(request,question_id): 
    return HttpResponse("You are voting on question %s." % question_id)
     