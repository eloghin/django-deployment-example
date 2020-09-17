from django.shortcuts import render

def index(request):
    index_dict = {'title': 'Home page', 'text': 'Hello world', 'number': 100}
    return render(request, 'basic_app/index.html', context=index_dict)

def other(request):
    other_dict = {'title': 'Other page'}
    return render(request, 'basic_app/other.html', context=other_dict)

def relative(request):
    relative_dict = {'title': 'Relative Url page'}
    return render(request, 'basic_app/relative_url_templates.html', context=relative_dict)
