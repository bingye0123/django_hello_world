from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
def post_create(request):
	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		print(form.cleaned_data.get("title"))
		instance.save()
		messages.success(request, "Successfully created!")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request, "Not Successfully created!")
	# if request.method=="POST":
	# 	print(request.POST)
	context={"form":form}
	return render(request, "post_form.html",context)
	# return HttpResponse("<h1>Create</h1>")

def post_detail(request,slug=None): # retrieve
	# return HttpResponse("<h1>Detail</h1>")
	instance=get_object_or_404(Post,slug=slug)
	context={
		"title": instance.title,
		"instance": instance
	}
	return render(request, "post_detail.html",context)

def post_list(request):
	# if request.user.is_authenticated():
	# 	context={"title": "My User List"}
	# 	return render(request, "index.html",context)
	# else:
	# 	context={"title": "List"}
	# 	return render(request, "index.html",context)
	queryset_list=Post.objects.all()#.order_by("-timestamp")

	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var="page"

	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context={
		"title": "List",
		"object_list": queryset,
		"page_request_var": page_request_var,
	}
	return render(request, "post_list.html",context)
	# return HttpResponse("<h1>List</h1>")



def post_update(request,slug=None):
	# return HttpResponse("<h1>Update</h1>")
	instance=get_object_or_404(Post,slug=slug)
	form=PostForm(request.POST or None, request.FILES or None ,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> updated!",extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context={
		"title": instance.title,
		"instance": instance,
		"form": form
	}
	return render(request, "post_form.html",context)

def post_delete(request,slug=None):
	instance=get_object_or_404(Post,slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted!")
	# return HttpResponseRedirect(instance.get_absolute_url())
	return redirect('posts:list')
	# return HttpResponse("<h1>Delete</h1>")








