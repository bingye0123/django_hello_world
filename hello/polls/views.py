#====================================================================================
# from django.shortcuts import render

# # Create your views here.

# from django.http import HttpResponse,HttpResponseRedirect
# from .models import Question,Choice
# from django.template import loader
# from django.shortcuts import render,get_object_or_404
# from django.http import Http404

# # from django.urls import reverse ## this is for django 1.10
# from django.core.urlresolvers import reverse ## use this instead for django 1.9

# ## use the default template
# # def index(request):
# #     latest_question_list=Question.objects.order_by('-pub_date')[:5]
# #     output=', '.join([x.question_text for x in latest_question_list])
# #     return HttpResponse(output)
# # 	# return HttpResponse("Hello world. You are at the polls index!")


# ## use the costom template: polls/templates/polls/index.html
# # def index(request):
# #     latest_question_list=Question.objects.order_by('-pub_date')[:5]
# #     template=loader.get_template('polls/index.html')
# #     context={
# #         'latest_question_list': latest_question_list,
# #     }
# #     return HttpResponse(template.render(context,request))

# ## use render shortcut
# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     context={
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html',context=context)


# ## raise a 404 error
# # def detail(request,question_id):
# #     try:
# #         question=Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist!")
# #     return render(request, 'polls/detail.html',{'question': question})
# #     # return HttpResponse("You are looking at question %s." % question_id)

# ## A shortcut: get_object_or_404()¶
# def detail(request, question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request,question_id):
#     response="You are looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     try:
#         selected_choice=question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError,Choice.DoesNotExist):
#         # redisplay the question voting form
#         return render(request, 'polls/detail.html',{'question': question,'error_message': "You did not select a choice!",})
#     else:
#         selected_choice.votes+=1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
#     # return HttpResponse("You are voting on question %s." % question_id)

# def results(request, question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html',{'question': question})
#====================================================================================




#====================================================================================
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
# # from django.urls import reverse ## this is for django 1.10
from django.core.urlresolvers import reverse ## use this instead for django 1.9
from django.views import generic

from .models import Choice, Question
from django.utils import timezone


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		# """Return the last five published questions."""
		# return Question.objects.order_by('-pub_date')[:5]
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		# redisplay the question voting form
		return render(request, 'polls/detail.html',{'question': question,'error_message': "You did not select a choice!",})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
	# return HttpResponse("You are voting on question %s." % question_id)
#====================================================================================





