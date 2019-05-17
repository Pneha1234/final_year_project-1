from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from .models import Food, Festival


# class BaseView(TemplateView):
#     template_name = 'base.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['active'] = 'base'
#
#         return context
#
#
# class HomeView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['active'] = 'home'
#
#         return context
#
#
# class FoodView(TemplateView):
#     template_name = 'food.html'
#
#     def get_context_data(self, **kwargs):
#         # get all food value
#         allFoods = Food.objects.all();
#
#         # get template
#         template = loader.get_template('food.html')
#
#         context = {
#             'foodData': allFoods,
#         }
#
#         return HttpResponse(template.render(context))
#
#         # context = super().get_context_data(**kwargs)
#         # context['active'] = 'food'
#         #
#         # return context
#
#     # def searchfood(selfrequest):
#     #  if request.method == 'POST':
#     #  if request.POST.get(location)
#
#
# class FestivalView(TemplateView):
#     template_name = 'festival.html']]
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['active'] = 'festival'
#
#         return context
#
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['active'] = 'contact'
#
#         return context

def foodView(request):
    food = Food.objects.all()
    return render(request, 'food.html', {'food':food})

def festivalView(request):
    festival = Festival.objects.all()
    return render(request, 'festival.html' , {'festival' : festival})