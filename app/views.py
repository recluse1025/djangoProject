from django.shortcuts import render, HttpResponse, redirect
from .models import Record,Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def hello(request):
    return render(request, 'app/hello.html', {})

@login_required
def fronpage(request):
    record_form = RecordForm(initial={'balance_type':'支出'})
    records = Record.objects.filter()
    income_list = [record.cash for record in records if record.balance_type == '收入']
    outcome_list = [record.cash for record in records if record.balance_type == '支出']
    income = sum(income_list) if len(income_list) != 0 else 0
    outcome = sum(outcome_list) if len(outcome_list) != 0 else 0
    net = income - outcome
    # return render(request, 'app/index.html', {'records': records, 'income': income, 'outcome': outcome,
    #                                           'net': net})
    return render(request, 'app/index.html', locals())

@login_required
def settings(request):
    categories = Category.objects.filter()
    return render(request, 'app/settings.html', locals())

@login_required
def addCategory(request):
    if request.method == 'POST':
        posted_date = request.POST
        category = posted_date['add_category']
        Category.objects.get_or_create(category=category)
    return redirect('/settings')

@login_required
def deleteCategory(request, category):
    Category.objects.filter(category=category).delete()
    return redirect('/settings')

@login_required
def addRecord(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')

@login_required
def deleteRecord(request):
    if request.method == 'POST':
        id = request.POST['delete_val']
        Record.objects.filter(id=id).delete()
    return redirect('/')


# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...

def logout_view(request):
    logout(request)
    return redirect('/')

