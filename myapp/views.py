from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.forms import LogForm

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

def home(request):
    path=request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response=HttpResponse()
    response.headers['Age'] = 20

    msg = f'''<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User-Agent: {user_agent}
        <br>Path info: {path_info}
        <br>Response header: {response.headers}
        
    '''
    
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def menuitem(request, dish):
    items={
        'pasta': 'pasta is a type of noodles made from combinations',
        'falafel': 'falafel is a deep fried patties',
        'cheesecake': 'cheesecake is a type of dessert made with cream cheese',
    }

    discription=items[dish]

    return HttpResponse(f"<h2>{dish}</h2>"+ discription)

def say_hello(request):
    return HttpResponse("Hello World!")

def homepage(request):
    return HttpResponse("Welcome to the Little Lemon restaurant!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    newmenu = {'mains': [
        {'name': "falafel", 'price': "12"},
        {'name': "shawarma", 'price': "15"},
        {'name': "gyro", 'price': "10"},
    ]}
    return render(request, 'menu.html', newmenu)

def about(request):
    about_content = {'about': 'Based in LA, CA. Little Lemon'}
    return render(request,"about.html", about_content)