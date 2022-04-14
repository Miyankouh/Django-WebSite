from django.shortcuts import render
from datetime import date
# Create your views here.

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'django course',
        'author': 'Miyankouh',
        'image': 'django.png',
        'date': date(2022, 2, 10),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug': 'learning-python',
        'title': 'python course',
        'author': 'Miyankouh',
        'image': 'python.png',
        'date': date(2022, 3, 11),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug': 'learning-machine-learning',
        'title': 'ml course',
        'author': 'Miyankouh',
        'image': 'ml.png',
        'date': date(2022, 4, 14),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
]


def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html')


def single_post(request, slug):
    return render(request, 'blog/post-detail.html')
