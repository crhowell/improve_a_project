from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils import timezone
from operator import attrgetter
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *


def menu_list(request):
    all_menus = Menu.objects.all().prefetch_related('items')
    exp_menus = []
    no_exp_menus = []
    for menu in all_menus:
        if menu.expiration_date is None:
            no_exp_menus.append(menu)
            continue
        if menu.expiration_date >= timezone.now().date():
            exp_menus.append(menu)

    exp_menus = sorted(exp_menus, key=attrgetter('expiration_date'), reverse=True)

    # This doesn't work in Python 3 when None is a value in the list.
    # menus = sorted(menus, key=attrgetter('expiration_date'))
    menus = exp_menus + no_exp_menus
    return render(request, 'menu/list_all_current_menus.html', {'menus': menus})


def menu_detail(request, pk):
    menu = Menu.objects.prefetch_related('items').get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    try: 
        item = Item.objects.select_related('chef').get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'menu/detail_item.html', {'item': item})


def create_new_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'menu/menu_edit.html', {'form': form})


def edit_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    items = Item.objects.all()

    if request.method == "POST":
        print(menu.created_date)
        form = MenuForm(instance=menu, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('menu_list'))

    return render(request, 'menu/change_menu.html', {
        'menu': menu,
        'items': items,
        })
