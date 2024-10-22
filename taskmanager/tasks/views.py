from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView
from .models import Task
from .forms import TaskForm 

class HomeView(TemplateView):
    template_name = 'tasks/home.html'

# List view for displaying user-specific tasks
class TaskListView(LoginRequiredMixin, ListView):
    """
    Displays a list of tasks that are specific to the currently logged-in user.

    Inherits:
        LoginRequiredMixin: Ensures that the user is logged in before accessing this view.
        ListView: A built-in Django generic view to display a list of objects.

    Attributes:
        model (Task): The model that this view will use.
        template_name (str): The template used to render the task list.

    Methods:
        get_queryset(): Filters the tasks to show only those belonging to the logged-in user.
    """
    model = Task
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)  # Show tasks of the logged-in user

# Create new task
class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Allows the logged-in user to create a new task.

    Inherits:
        LoginRequiredMixin: Ensures the user is authenticated before creating a task.
        CreateView: A built-in Django view for handling object creation.

    Attributes:
        model (Task): The model that this view will create.
        form_class (TaskForm): The form class used to handle task creation.
        success_url (str): The URL to redirect to after successful task creation.
        template_name (str): The template used to render the task creation form.

    Methods:
        form_valid(form): Assigns the current user to the task before saving it.
    """

    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    template_name = 'tasks/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user for the task
        return super().form_valid(form)

# Update existing task
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allows the logged-in user to update an existing task.

    Inherits:
        LoginRequiredMixin: Ensures the user is authenticated before updating a task.
        UpdateView: A built-in Django view for handling object updates.

    Attributes:
        model (Task): The model that this view will update.
        fields (list): A list of fields that can be updated by the user.
        success_url (str): The URL to redirect to after a successful update.
        template_name (str): The template used to render the task update form.
    """
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task_list')
    template_name = 'tasks/task_form.html'

# Delete a task
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Allows the logged-in user to delete an existing task.

    Inherits:
        LoginRequiredMixin: Ensures the user is authenticated before deleting a task.
        DeleteView: A built-in Django view for handling object deletion.

    Attributes:
        model (Task): The model that this view will delete.
        success_url (str): The URL to redirect to after a successful deletion.
        template_name (str): The template used to render the task deletion confirmation page.
    """
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'tasks/task_confirm_delete.html'

# Toggle task completion status
class TaskToggleView(LoginRequiredMixin, UpdateView):
    """
    Toggles the completion status of a task.

    Inherits:
        LoginRequiredMixin: Ensures the user is authenticated before toggling task status.
        UpdateView: A built-in Django view for handling object updates.

    Attributes:
        model (Task): The model that this view will toggle.
        fields (list): The 'completed' field is the only field updated.
        success_url (str): The URL to redirect to after toggling the task status.

    Methods:
        post(request, *args, **kwargs): Handles POST requests to toggle the task completion status.
    """
    model = Task
    fields = ['completed']
    success_url = reverse_lazy('task_list')
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.completed = not task.completed  # Toggle the completed status
        task.save()
        return redirect('task_list')
