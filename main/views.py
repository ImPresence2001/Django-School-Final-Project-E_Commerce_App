from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Part, Software, Prebuild
# Create your views here.

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def parts(request):
  myparts = Part.objects.all().values()
  template = loader.get_template('all_parts.html')
  context = {
    'myparts': myparts,
  }
  return HttpResponse(template.render(context, request))

def parts_details(request, id):
  myparts = Part.objects.get(id=id)
  template = loader.get_template('parts_details.html')
  context = {
    'myparts': myparts,
  }
  return HttpResponse(template.render(context, request))

def softwares(request):
  mysoftwares = Software.objects.all().values()
  template = loader.get_template('all_softwares.html')
  context = {
    'mysoftwares': mysoftwares,
  }
  return HttpResponse(template.render(context, request))

def softwares_details(request, id):
  mysoftwares = Software.objects.get(id=id)
  template = loader.get_template('softwares_details.html')
  context = {
    'mysoftwares': mysoftwares,
  }
  return HttpResponse(template.render(context, request))

def prebuilds(request):
  myprebuilds = Prebuild.objects.all().values()
  template = loader.get_template('all_prebuilds.html')
  context = {
    'myprebuilds': myprebuilds,
  }
  return HttpResponse(template.render(context, request))

def prebuilds_details(request, id):
  myprebuilds = Prebuild.objects.get(id=id)
  template = loader.get_template('prebuilds_details.html')
  context = {
    'myprebuilds': myprebuilds,
  }
  return HttpResponse(template.render(context, request))