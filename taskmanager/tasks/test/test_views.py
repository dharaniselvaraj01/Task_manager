import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task

@pytest.mark.django_db
class TestTaskViews:
    @pytest.fixture(autouse=True)
    def setup_user_and_task(self, client):
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='12345')
        client.login(username='testuser', password='12345')

        # Create a sample task
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='A task for testing',
            completed=False
        )
        self.client = client

    def test_task_list_view(self):
        # Test the task list view
        response = self.client.get(reverse('task_list'))
        assert response.status_code == 200
        assert 'tasks/task_list.html' in [t.name for t in response.templates]
        assert 'Test Task' in response.content.decode()

    def test_task_create_view(self):
        # Test the task creation view
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'Description of new task',
        })
        assert response.status_code == 302  # Should redirect after successful creation
        assert Task.objects.filter(title='New Task').exists()  # Check if task was created

    def test_task_update_view(self):
        # Test the task update view
        response = self.client.post(reverse('task_update', args=[self.task.id]), {
            'title': 'Updated Task',
            'description': 'Updated description',
            'completed': True,
        })
        self.task.refresh_from_db()  # Refresh the task instance
        assert self.task.title == 'Updated Task'
        assert self.task.completed is True

    def test_task_delete_view(self):
        # Test the task delete view
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        assert response.status_code == 302  # Should redirect after successful deletion
        assert not Task.objects.filter(id=self.task.id).exists()  # Check if task was deleted
