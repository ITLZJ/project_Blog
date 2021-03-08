from django.test import TestCase

# Create your tests here.
from blog.models import Post

post_list = Post.objects.all().order_by('-created')
for i in post_list:
    print(i)