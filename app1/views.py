from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Gallery
from .forms import Gallery_form



# Start application Here 
# Used django Modelform 

def image_upload_view(request):
     #comments = Comment.objects.latest('datetime')
    obj=Gallery.objects.order_by('-datetime')
    if request.method == 'POST':
        form = Gallery_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'app1/upload.html', {'form': form, 'img_obj': img_obj,'images':obj})
    else:
        form = Gallery_form()
    return render(request, 'app1/upload.html', {'form': form,'images':obj })  