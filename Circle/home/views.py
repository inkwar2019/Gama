from django.shortcuts import render,redirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post,Notification
from user.models import User




class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title' , 'body','price','discount','image']
    success_message = "Post created successfully"
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title' , 'body','image']
    success_message = "Post updated successfully"
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    success_message = "Post deleted successfully"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'home/about.html')


class Notifications(LoginRequiredMixin,ListView):
    model = Notification
    template_name = 'home/notification.html'
    context_object_name = 'notifications'
    ordering = ['-date']
    paginate_by = 15

def loading(request,pk):
    noti1 = Notification(title=f'You request for {Post.objects.get(id=pk).author.username}\'s book.',post=Post.objects.get(id=pk),owner=request.user,customer=Post.objects.get(id=pk).author.username)
    noti2 = Notification(title=f'{request.user.username} request for your book.',post=Post.objects.get(id=pk),owner=Post.objects.get(id=pk).author,customer=request.user.username)
    noti1.save()
    noti2.save()
    return redirect('home')

def confirming(request,pk):
    noti = Notification.objects.get(id=pk)
    noti.confirmed = False
    noti.title += " (confirmed)"
    noti.save()
    noti1 = Notification(title=f'{noti.owner.username} confirmed your request.(Call him now:{noti.owner.profile.p_number})',post=noti.post,owner=User.objects.filter(username=noti.customer).first(),customer=noti.owner.username)
    noti1.save()
    return redirect('post-notifications')