from django.urls import reverse
from django.shortcuts import render, redirect, reverse 
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    video_trailer = strip_tags(request.POST.get("video_trailer"))
    rating = strip_tags(request.POST.get("rating"))
    quantity = strip_tags(request.POST.get("quantity"))

    user = request.user
    new_product = ProductEntry(
        user=user,
        name=name,
        price=int(price),
        description=description,
        video_trailer=video_trailer,
        rating=float(rating),
        quantity=int(quantity)
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@login_required(login_url='/login')
def show_main(request):

    context = {
        'name': request.user.username,
        'class': 'PBP E',
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
            messages.error(request, "Invalid username or password. Please try again.")
      
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    mood = ProductEntry.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    mood = ProductEntry.objects.get(pk = id)
    mood.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def create_mood_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_product = ProductEntry.objects.create(
                user=request.user,
                name=data.get("name", ""),
                price=int(data.get("price", 0)),
                description=data.get("description", ""),
                video_trailer=data.get("video_trailer", ""),
                rating=float(data.get("rating", 0.0)),
                quantity=int(data.get("quantity", 0))
            )

            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
        except (ValueError, KeyError) as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error"}, status=401)