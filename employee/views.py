from .models import Employee
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import EmailForm

def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = cd['message']

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'employee/successfull.html', {

        'form': form,
        'messageSent': messageSent,

    })



class IndexView(ListView):
    model = Employee
    template_name = 'employee/index.html'
    context_object_name = 'index'


class SingleView(DetailView):
    model = Employee
    template_name = 'employee/single.html'
    context_object_name = 'post'


class PostsView(ListView):
    model = Employee
    template_name = 'employee/posts.html'
    context_object_name = 'post_list'


class AddView(CreateView):
    model = Employee

    template_name = 'employee/add.html'
    fields = '__all__'
    success_url = reverse_lazy('employee:posts')


class EditView(UpdateView):
    model = Employee
    template_name = 'employee/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('employee:posts')


class Delete(DeleteView):
    model = Employee
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('employee:posts')
    template_name = 'employee/confirm-delete.html'

