from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from cms.models import Story, Category

def category(request, slug):
    """Given a category slug, display all items in a category."""
    category = get_object_or_404(Category, slug=slug)
    story_list = Story.objects.filter(category=category)
    heading = "Category: %s" % category.label
    return render_to_response("cms/story_list.html", locals())

def search(request):
    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    if 'q' in request.GET:
        term = request.GET['q']
        story_list = Story.objects.filter(Q(title__contains=term) | Q(markdown_content__contains=term))
        heading = "Search results"
    return render_to_response("cms/story_list.html", locals())
