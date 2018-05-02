from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Entry
from .forms import EntryForm
# Create your views here.


def index(request):
	toDo = Entry.objects.all().order_by('-id')

	context = {"toDo":toDo}
	return render(request,"index.html",context)

def new_todo(request):
	if request.method != "POST":
		form = EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")

	context = {"form":form}
	return render(request, "new_todo.html", context)

def delete_todo(request,id):
	Entry.objects.filter(id=id).delete()
	return HttpResponseRedirect("/")
