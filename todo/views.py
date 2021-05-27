from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from todo.forms import TODOForm
from todo.models import TODO,CR
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
# Create your views here.
from django import forms
from django.contrib import messages
from datetime import date
@login_required(login_url='account')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        activeuser={
            "role":"onlystudent",
            "name":user.username
        }
        user = request.user
        t=User.objects.get(username=user)
        if CR.objects.filter(username=user):
            activeuser["role"]="cr"
        incoming=[]
        today = date.today()        
        r=str(today)
        year=""
        month=""
        date1=""
        j=0
        helper=""
        for i in r:
            if i != "-":
                helper+=i
            if i == "-":
                if j==4:
                    year=helper
                    helper=""
                elif j == 7:
                    month=helper
                    helper=""
                else:
                    date1=helper
            j+=1
        date1=helper       
        date_todos = TODO.objects.filter().order_by('end_date')
        completelen=0
        for k in date_todos:
            today2=str(k.end_date)
            year2=""
            month2=""
            date2=""
            j=0
            helper=""
            completelen+=1
            for i in today2:
                if i != "-":
                    helper+=i
                if i == "-":
                    if j==4:
                        year2=helper
                        helper=""
                    elif j == 7:
                        month2=helper
                        helper=""
                    else:
                        date2=helper
                j+=1
            date2=helper
            if year > year2 :
                continue
            elif year < year2:
                incoming.append(k.id)
                continue
            else:
                if month > month2:
                    continue  
                if month < month2:
                    incoming.append(k.id)                   
                    continue                
                else:
                    if date1>date2:
                        continue                     
                    else:
                        incoming.append(k.id)                     
                        continue 
        incominglen = len(incoming)
        completelen=completelen-incominglen
        return render(request, 'home.html', context={'p':t,'todos': date_todos,'activeuser':activeuser, 'incoming':incoming,'incominglen':incominglen,'completelen':completelen})
def team(request):
    if request.user.is_authenticated:
        user = request.user
        t=User.objects.get(username=user)
        activeuser={
            "role":"onlystudent",
            "name":user.username
        }
        if CR.objects.filter(username=user):
            activeuser["role"]="cr"
        todos = TODO.objects.all()       
    return render(request, 'team.html', context={'p':t,'todos': todos,'activeuser':activeuser})
@login_required(login_url='account')
def todo(request):
    if request.user.is_authenticated:
        user = request.user
        t=User.objects.get(username=user)
        activeuser={
            "role":"onlystudent",
            "name":user.username
        }
        p='pending'
        if CR.objects.filter(username=user):
            activeuser["role"]="cr"
        form = TODOForm()
        todos = TODO.objects.all()
        return render(request, 'todo.html', context={'p':t,'form': form,'activeuser':activeuser})
def contactus(request):
    return render(request, 'contact.html')
def account(request):
    if request.method == 'GET':       
        context = {
            'u':"",
            'p':""
        }
        return render(request, 'login.html', context=context)
    else:
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            loginUser(request, user)
            return redirect('home')
        else:
            context = {
             
                'u':username,
                'p':""
            }
            messages.info(request,'Please give correct username and password') 
            return render(request, 'login.html', context=context)
def signup(request):
    if request.method == 'GET':    
        context={
            "f":"",
            "l":"",
            "u":"",
            "p":"",
            "pa":"",
            "m":""
        }     
        return render(request, 'signup.html',context=context)
    else:       
        fn=request.POST['fname']
        ln=request.POST['lname']
        un=request.POST['uname']
        p=request.POST['pass']
        pa=request.POST['passwordagain']
        email=request.POST['email']
        context={
            "f":fn,
            "l":ln,
            "u":un,
            "p":p,
            "pa":pa,
            "m":email
        }   
        if User.objects.filter(username=un).exists():
            messages.info(request,'Username Taken')             
            return render(request, 'signup.html',context=context)
        else:
            if p==pa:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email Taken')               
                    return render(request, 'signup.html',context=context)
                else:
                    user =User.objects.create_user(username=un,password=p,email=email,first_name=fn,last_name=ln)
                    user.save()
                  
                    return redirect('account')
            else:
                messages.info(request,'Password Not Matching')
                return render(request, 'signup.html',context=context)
@login_required(login_url='account')
def add_todo(request):     
    if request.user.is_authenticated:
        user = request.user
        activeuser={
                "role":"onlystudent",
                "name":user.username
                }
        if CR.objects.filter(username=user):
            activeuser["role"]="cr" 
        else:
            pass
        if  activeuser["role"]=="cr": 
            titl=request.POST['todotitle']
            about=request.POST['about']
            course=request.POST['course']
            sd=request.POST['sdate']
            st=request.POST['stime']
            ed=request.POST['edate']
            et=request.POST['etime']
            u1=request.POST['url1']
            u2=request.POST['url2']   
            w1=request.POST['w1'] 
            w2=request.POST['w2'] 
                        
            todo = TODO(title=titl,about=about,course=course,start_date=sd,start_time=st,end_date=ed,end_time=et,url1=u1,url2=u2,w1=w1,w2=w2)
            todo.save()           
            return redirect('todo')
        #form = TODOForm(request.POST)        
        else:
            return redirect('home')
def signout(request):
    logout(request)
    return redirect('account')
def forgetpassword(request):
    return render(request, 'forgetpassword.html')
@login_required(login_url='account')
def deletetodo(request,id):
    if request.user.is_authenticated:
        user = request.user
        activeuser={
            "role":"onlystudent",
            "name":user.username
        }
        if CR.objects.filter(username=user):
            activeuser["role"]="cr"
        if activeuser["role"]=="cr":
            TODO.objects.get(pk=id).delete()
            todos = TODO.objects.all()  
            return redirect('home')    
        else:
            return redirect('home')
def edittodo(request,id):
    if request.user.is_authenticated:
        user = request.user
        t2=User.objects.get(username=user)   
        
        activeuser={
            "role":"onlystudent",
            "name":user.username
        }
        form = TODOForm()
        if CR.objects.filter(username=user):
            activeuser["role"]="cr"
        if activeuser["role"]=="cr":
            t=TODO.objects.get(pk=id)           
            s_date=str(t.start_date)
            s_time=str(t.start_time)
            e_date=str(t.end_date)
            e_time=str(t.end_time)
            editform={
            "id":t.id,
            "title":t.title,
            "about":t.about,
            "course":t.course,
            "s_d":s_date,
            "s_t":s_time,
            "e_d":e_date,
            "e_t":e_time,
            "url1":t.url1,
            "url2":t.url2,
            "w1":t.w1,
            "w2":t.w2,
            }           
            return render(request, 'edittodo.html', context={'p':t2,'editform':editform,'activeuser':activeuser})
        else:
            return redirect('home')
def updatetodo(request,id):    
    if request.user.is_authenticated:
        user = request.user
        activeuser={
            "role":"onlystudent",
            "name":user.username
        }        
        if CR.objects.filter(username=user):
            activeuser["role"]="cr"
        if activeuser["role"]=="cr":              
            todo=TODO.objects.get(pk=id)                    
            todo.title=request.POST['todotitle']
            todo.about=request.POST['about']
            todo.course=request.POST['course']
            todo.start_date=request.POST['sdate']
            todo.start_time=request.POST['stime']
            todo.end_date=request.POST['edate']
            todo.end_time=request.POST['etime']
            todo.url1=request.POST['url1']
            todo.url2=request.POST['url2']   
            todo.w1=request.POST['w1'] 
            todo.w2=request.POST['w2']           
            todo.save()             
            return redirect('home')
        else:
            return redirect('home')
def updateprofile(request):
    if request.user.is_authenticated:
        user = request.user
        if user.username==user.username:
            fn=request.POST['fname']
            ln=request.POST['lname']
            un=request.POST['uname']
            email=request.POST['email']
            context={
                "f":fn,
                "l":ln,
                "u":un,
                "m":email
            }   
            t=User.objects.get(username=user)    
            activeuser={
                "role":"onlystudent",
                "name":user.username
            }
            if CR.objects.filter(username=user):
                activeuser["role"]="cr"  
            if User.objects.filter(username=un).exists():
                if un == t.username: 
                    t=User.objects.get(username=user.username)                     
                    t.first_name=request.POST['fname'] 
                    t.last_name=request.POST['lname'] 
                    t.username=request.POST['uname']
                    t.email=request.POST['email'] 
                    t.save()                 
                    return redirect('profile')
                else:
                    messages.info(request,'Username Taken')          
                    return render(request, 'profile.html',context={'p':context,'activeuser':activeuser})          
                 
            elif  User.objects.filter(email=email).exists(): 
                if email == t.email: 
                    t=User.objects.get(username=user.username)                     
                    t.first_name=request.POST['fname'] 
                    t.last_name=request.POST['lname'] 
                    t.username=request.POST['uname']
                    t.email=request.POST['email'] 
                    t.save()                 
                    return redirect('profile')
                else:            
                    messages.info(request,'Email Taken')
                    return render(request, 'profile.html',context={'p':context,'activeuser':activeuser})          
            else:
                t=User.objects.get(username=user.username)                     
                t.first_name=request.POST['fname'] 
                t.last_name=request.POST['lname'] 
                t.username=request.POST['uname']
                t.email=request.POST['email'] 
                t.save()                 
                return redirect('profile') 
        else:
            return redirect('home')
    else:
        return redirect('account')
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        t=User.objects.get(username=user)    
        activeuser={
            "role":"onlystudent",
            "name":user.username
        }
        context={
                "f":t.first_name,
                "l":t.last_name,
                "u":t.username,
                "m":t.email,
            }
        if CR.objects.filter(username=user):
            activeuser["role"]="cr"              
        return render(request, 'profile.html',context={'p':context,'activeuser':activeuser})
      
    else:
        return redirect('account')
def search(request):
    if request.user.is_authenticated:
        try: 
            search = request.POST['search']
        except:
            search =""
        substring=search
        user = request.user
        activeuser={
            "role":"onlystudent",
            "name":user.username
        }
        user = request.user
        t=User.objects.get(username=user)
        if CR.objects.filter(username=user):
            activeuser["role"]="cr"
        incoming=[]
        complete=[]
        today = date.today()        
        r=str(today)
        year=""
        month=""
        date1=""
        j=0
        helper=""
        for i in r:
            if i != "-":
                helper+=i
            if i == "-":
                if j==4:
                    year=helper
                    helper=""
                elif j == 7:
                    month=helper
                    helper=""
                else:
                    date1=helper
            j+=1
        date1=helper       
        date_todos = TODO.objects.filter().order_by('end_date')
        completelen=0
        for k in date_todos:
            fullstring1= k.title
            fullstring2=k.course            
            fullstring1=fullstring1.lower()
            substring=substring.lower()
            if ((substring in fullstring1) or (substring in fullstring2)) and substring != "" :
                today2=str(k.end_date)
                year2=""
                month2=""
                date2=""
                j=0
                helper=""                
                for i in today2:
                    if i != "-":
                        helper+=i
                    if i == "-":
                        if j==4:
                            year2=helper
                            helper=""
                        elif j == 7:
                            month2=helper
                            helper=""
                        else:
                            date2=helper
                    j+=1
                date2=helper
                if year > year2 :
                    complete.append(k.id)
                elif year < year2:
                    incoming.append(k.id)                   
                else:
                    if month > month2:
                        complete.append(k.id)
                    elif month < month2:
                        incoming.append(k.id)                                                      
                    else:
                        if date1>date2:
                            complete.append(k.id)                   
                        else:
                            incoming.append(k.id)                
            else:
                pass            
        incominglen = len(incoming)
        completelen=len(complete)       
        return render(request, 'search.html', context={'search_word':search,'p':t,'todos': date_todos,'activeuser':activeuser, 'incoming':incoming,'complete':complete,'incominglen':incominglen,'completelen':completelen})