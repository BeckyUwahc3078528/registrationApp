from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# from .models import Message
from .forms import InquiryForm


# Create your views here.
def home(request): 

  return render(request, 'studentApp/home.html', {'title': 'Welcome'})


def about(request): 

  return render(request, 'studentApp/about.html', {'title': 'About'})


# def contact(request): 

#   return render(request, 'studentApp/message_form.html', {'title': 'message-create'})
def contact(request): 

  return render(request, 'studentApp/submit_inquiry.html', {'title': 'submit_inquiry'})

def register(request): 

  return render(request, 'studentApp/register.html', {'title': 'register'})

def submit_inquiry(request):
  if request.method == 'POST':
    form = InquiryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('inquiry_success')  # Redirect to a success page
  else:
    form = InquiryForm()
  return render(request, 'studentApp/submit_inquiry.html', {'form': form})

def inquiry_success(request):
    return render(request, 'studentApp/inquiry_sucess.html')


# def enquiry(request):
#    # Get all reported issues
#   #Create a context dictionary to pass to the template
#   #Render the report.html template with the context
#   daily_enquiry = {'messages': Message.objects.all(), 'title': 'Enquiries Reported'}
#   return render(request, 'studentApp/enquiry.html', daily_enquiry)




# class PostListView(ListView):
#     model = Message
#     # ordering = ['-date_submitted']
#     template_name = 'studentApp/enquiry.html'
#     context_object_name = 'messages'
#     paginate_by = 10  # Optional pagination


# class PostDetailView(DetailView):
#   model = Message
#   template_name = 'studentApp/messageEnquiry_detail.html'

# class PostCreateView(LoginRequiredMixin, CreateView):
#   model = Message
#   fields = ['name', 'emailAddress', 'subject', 'description','author','date_subimtted']

#   def form_valid(self, form): 

#         form.instance.author = self.request.user
#         return super().form_valid(form)
  
# class PostUpdateView(LoginRequiredMixin, UpdateView): 
#   model = Message
#   fields = ['name', 'emailAddress', 'subject', 'description','author','date_subimtted']

#   def test_func(self):

#         message = self.get_object()

#         return self.request.user == message.author




    
