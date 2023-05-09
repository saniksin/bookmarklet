from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreatedForm
from django.shortcuts import get_list_or_404
from .models import Image

# Create your views here.

@login_required
def image_create(request):
    if request.method == 'POST':
        #форма отправлена
        form = ImageCreatedForm(data=request.POST)
        if form.is_valid():
            # данные в форме вилидны
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # назначить текущего пользователя элементу
            new_image.user = request.user
            new_image.save()
            messages.success(request,
                             'Изображение успешно добавлено!')
            # перенарпавить к представулению детальной информации
            return redirect(new_image.get_absolute_url())
    else:
        # скомпоновать форму с данными, предоставленными 
        # букмарклером методом GET
        form = ImageCreatedForm(data=request.GET)
        return render(request,
                      'images/image/create.html',
                      {'section': 'images',
                       'form': form})


def image_detail(request, id, slug):
    image = get_list_or_404(Image, id=id, slug=slug)
    return render(request,
                  'images/image/detail.html',
                  {'section':'images',
                   'image':image})