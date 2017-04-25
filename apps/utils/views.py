from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages


generic_template = 'pages/form_models.html'

class GenericCreate(LoginRequiredMixin, CreateView):
  title = ''
  dependencies = []

  def get_context_data(self, **kwargs):
    context = super(GenericCreate, self).get_context_data(**kwargs)
    context['title']         = self.title
    context['dependencies']  = self.dependencies
    context['template_name'] = self.template_name
    return context

  def form_valid(self, form):
    messages.success(self.request, _('Contenido creado con éxito'))
    return super(CreateView, self).form_valid(form)


class GenericUpdate(LoginRequiredMixin, UpdateView):
  title = ''
  dependencies = []

  def get_context_data(self, **kwargs):
    context = super(GenericUpdate, self).get_context_data(**kwargs)
    context['title']        = self.title
    context['dependencies'] = self.dependencies
    context['template_name'] = self.template_name
    return context

  def form_valid(self, form):
    messages.success(self.request, _('Contenido editado con éxito'))
    return super(UpdateView, self).form_valid(form)

  def get_initial(self):
    super(GenericUpdate, self).get_initial()
    if not self.object.edit_permissions(self.request.user):
      raise PermissionDenied
    return self.initial


class GenericDelete(LoginRequiredMixin, DeleteView):
  title = ''
  template_name = generic_template

  def get_context_data(self, **kwargs):
    context = super(GenericDelete, self).get_context_data(**kwargs)
    context['title'] = self.title
    context['template_name'] = self.template_name
    return context

  def form_valid(self, form):
    messages.success(self.request, _('Contenido borrado con éxito'))
    return super(DeleteView, self).form_valid(form)

  def get_initial(self):
    super(GenericUpdate, self).get_initial()
    if not self.object.edit_permissions(self.request.user):
      raise PermissionDenied
    return self.initial