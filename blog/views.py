from django.shortcuts import render

posts=[
    {
        'author':'Jack Racher',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'March 31st 2022'
    },
    {
        'author':'Jack Ryan',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'April 1st 2022'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
