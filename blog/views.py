
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib import messages
from django.http import Http404
from django.db.models import Count

# class BlogList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog.html'
#     context_object_name = 'blog_list'
#     paginate_by = 6

def Error (request):
    return render(request, 'error.html' ,)

def custom_404(request, exception):
    return render(request, 'error.html')
def custom_500(request):
    return render(request, 'error.html')
# def custom_500(request):
#     return render(request, '505')

# def error_404_view(request, exception):
#     return render(request, 'error.html')

def BlogList (request):
    template_name = 'blog.html'
    # blog_list = Post.objects.all()
    blog_list = Post.objects.filter(status=1).order_by('-created_on')
    blog_latest = Post.objects.filter(status=1).order_by('-created_on')[:2]
    page = request.GET.get('page', 1)
    x = blog_list.count()
    y = x/2
    paginator = Paginator(blog_list,y) # Show 25 contacts per page.]
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-created_on')
    else:
        posts = Post.objects.all()
    # if not query:
    #     return messages.warning('This is full')
    if not posts:
        messages.warning(request, 'No content found!.') 
        


    return render(request, template_name, {"blog_list":blog_list, 'posts': posts, 'blog_latest':blog_latest})

class BlogSearchView(generic.ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-created_on')
            return posts
        else:
            posts = Post.objects.all()
            return posts


        # if not query:
        #     object_list =Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-created_on')
        #     return object_list
        # return HttpResponse("This is for testing the validation")



# i want to paginate this list if they are more than 9 ---------->>>




    # def get_queryset(self):
    #     if 'q' in self.request.GET:
    #         q = self.request.GET['q']
    #         # query = self.request.GET.get('q')
    #         return Post.objects.filter(title__icontains=q).order_by('-created_on')
    #     else:
    #         return render(self, 'blog.html')
            # return render("Hello World!")
            # return render_to_response('error.html')
        # return redirect(Error)

        # else:
        #     data = Post.objects.all()
        # context = {'data':data}
        # return render(request, 'blog.html')

    # def get_queryset(self):
    #     # if self.request.GET == 'q':
    #         q = self.request.GET['q']
    #         if q in self.request.GET:
    #             return Post.objects.filter(title__icontains=q).order_by('-created_on')
    #         else:
    #             return HttpResponse("Not found")



# class BlogDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog-single.html'
#     context_object_name = 'blog_detail'

# def Footer(request):
#     template_name = 'base.html'
#     footer_list = Post.objects.all()[:2]
#     return render(request, template_name, {"footer_list":footer_list})

def post_detail(request, slug):
    template_name = 'blog-single.html'
    blog_latest = Post.objects.filter(status=1).order_by('-created_on')[:2]
    blogside = Post.objects.all().order_by('-created_on')[:4]
    post = get_object_or_404(Post, slug=slug)
    post.views += 1
    post.save()
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        "blogside":blogside, 'blog_latest':blog_latest,
    }

    return render(request, template_name, context)




