import json

import telebot
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from main_app.forms import ManagerForm, ContactForm
from main_app.models import *


def home_page(request):
    context = {
        'news': News.objects.order_by('-pk')[:3],
        'categories': Category.objects.filter(parent=None),
        'Form': ContactForm(),
    }
    return render(request, 'main_app/index.html', context)


class NewsDetail(DetailView):
    model = News
    template_name = 'main_app/news_single.html'
    context_object_name = 'news'
    extra_context = {
        'another_news': News.objects.order_by('-pk')[:3],
    }


def product_detail(request, pk):
    template_name = 'main_app/product_single.html'
    # category_name = Category.objects.get(name=category)
    product = Product.objects.get(pk=pk)
    context = {
        # 'category': category_name,
        'product': product,
        'another_products': Product.objects.filter(sub_category_id=product.sub_category_id).exclude(pk=pk)[:4],
        'Form': ManagerForm(),
        # initial = {'product': product}
    }
    return render(request, template_name, context)


def products_page(request):
    context = {
        'Categories': Category.objects.filter(parent=None),
        'Subcategories': Category.objects.filter(parent__isnull=False),
        'Products': Product.objects.all(),
    }
    return render(request, 'main_app/products.html', context)


def about_page(request):
    return render(request, 'main_app/about_us.html')


class NewsList(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'main_app/news_all.html'
    paginate_by = 3


def contacts_page(request):
    context = {
        'Form': ContactForm(),
    }
    return render(request, 'main_app/contact.html', context)


def send_message(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            bot_token = '1256450138:AAHTUj9_gP4QHkBaAeyIvz5Q6yVU5VJeg1E'
            chat_id = '267010404'
            txt_dict = {
                'Имя: ': request.POST['username'],
                'Телефон: ': request.POST['phone'],
                'Email: ': request.POST['email'],
                'Тема: ': product.name,
            }
            bot_txt = 'Новая <b>заявка</b>! Нужно отреагировать\n\n'
            for txt_arr in txt_dict.items():
                bot_txt += '<b>' + txt_arr[0] + '</b>' + txt_arr[1] + '\n'
            bot = telebot.TeleBot(bot_token)
            bot.send_message(
                chat_id=chat_id,
                text=bot_txt,
                parse_mode='HTML'
            )
            return render(request, 'main_app/form_response.html', context={'response': 'ok'})
    else:
        form = ManagerForm()
    return render(request, 'main_app/form_response.html', context={'response': 'error'})


def contact_message(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            bot_token = '1256450138:AAHTUj9_gP4QHkBaAeyIvz5Q6yVU5VJeg1E'
            chat_id = '267010404'
            txt_dict = {
                'Имя: ': request.POST['username'],
                'Телефон: ': request.POST['phone'],
                'Email: ': request.POST['email'],
                'Текст: ': request.POST['message'],
            }
            bot_txt = 'Новая <b>заявка</b>! Нужно отреагировать\n\n'
            for txt_arr in txt_dict.items():
                bot_txt += '<b>' + txt_arr[0] + '</b>' + txt_arr[1] + '\n'
            bot = telebot.TeleBot(bot_token)
            bot.send_message(
                chat_id=chat_id,
                text=bot_txt,
                parse_mode='HTML'
            )
            return render(request, 'main_app/form_response.html', context={'response': 'ok'})
    else:
        form = ManagerForm()
    return render(request, 'main_app/form_response.html', context={'response': 'error'})


def search(request):
    if request.method == 'POST':
        search_text = request.POST['search']

        response_data = Product.objects.filter(name__icontains=search_text).values('name', 'sub_category', 'pk')

        # return HttpResponse(
        #     json.dumps(response_data),
        #     content_type="application/json"
        # )
        return JsonResponse({'results': list(response_data)})
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
