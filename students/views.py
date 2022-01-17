from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import StudentForm
from .models import StudentInfo, StudentAcademics

# Create your views here.

#create form for a record 
@login_required
def stud_create_form(request):
    form = StudentForm()
    context = {
        "form": form,
    }
    if request.method == "POST":
        form = StudentForm(request.POST)
        context['form'] = form
        if form.is_valid(): 
            roll_no = form.cleaned_data.get("roll_no")
            name = form.cleaned_data.get("name")
            stud_class = form.cleaned_data.get("stud_class")
            school = form.cleaned_data.get("school")
            mobile = form.cleaned_data.get("mobile")
            address = form.cleaned_data.get("address")
            maths = form.cleaned_data.get("maths")
            physics = form.cleaned_data.get("physics")
            chemistry = form.cleaned_data.get("chemistry")
            biology = form.cleaned_data.get("biology")
            english = form.cleaned_data.get("english")  
            #studinfo object
            stud_object = StudentInfo.objects.create(roll_no=roll_no,
            name=name, stud_class=stud_class, school=school, mobile=mobile, address=address)
            #studacademics object
            studmarks_object = StudentAcademics.objects.create(roll_no = StudentInfo.objects.get(roll_no=roll_no), maths=maths,
            physics=physics, chemistry=chemistry, biology=biology, english=english)

            context['object'] = stud_object
            context['marks_object'] = studmarks_object
            context['created'] = True
    return render(request, "create.html", context=context)

#search a record by student name fucntion
def stud_search_view(request):
    query = request.GET.get('q')      #<input type="text" name="q"/>
    qs = StudentInfo.objects.all()    
    if query is not None:
        lookups = Q(name__icontains=query)
        qs = StudentInfo.objects.filter(lookups)
    context = {
        "object_list": qs
    }
    return render(request, "search.html", context=context)


def stud_info_view(request):
    
    #from the database 
    stud_queryset = StudentInfo.objects.all()
    
    context = {
        "object_list": stud_queryset,
    }
    return render(request, "info_view.html", context=context)

@login_required
#studentinfo detail view
def studinfo_detail_view(request, roll_no=None):
    
    #from the database 
    studinfo_obj = None
    if roll_no is not None:
        studinfo_obj = StudentInfo.objects.get(roll_no=roll_no)
        context = {
        "object": studinfo_obj,
        }
    return render(request, "detail_info_view.html", context=context)

@login_required
def stud_detail_view(request, roll_no=None):

    #from the database
    studacademics_obj = None
    if roll_no is not None:
        studacademics_obj = StudentAcademics.objects.get(roll_no=roll_no)
        context = {
        "object": studacademics_obj,
        "roll_no_obj": studacademics_obj.roll_no,
        }
    return render(request, "detail_view.html", context=context)


#user register form
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context)


#user login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/info_view')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


#user logout view
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/info_view/")
    return render(request, 'accounts/logout.html', {})


