from django.shortcuts import render,redirect
from .models import Entry,Blog,Author
from .form import Entryform

# Create your views here
def base(request):
    context={"entry_list":Entry.objects.all()}
    return render(request,"show.html",context)

def showout(request):
    if request.method=="GET":
         form=Entryform()
         return render(request,"showout.html",{"form":form})
    else:
        form =Entryform(request.POST)
        if form.is_valid:
            form.save()
        return redirect("/list")
