import pytest
from django.contrib.auth.models import User
from tasks.models import Task

@pytest.mark.django_db
class TestTaskModel:
    @pytest.fixture(autouse=True)
    def setup_user_and_task(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Create a task
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='A task for testing',
            completed=False
        )

    def test_task_creation(self):
        # Test that the task was created correctly
        assert self.task.title == 'Test Task'
        assert self.task.user.username == 'testuser'
        assert not self.task.completed

    def test_str_method(self):
        # Test the string representation of the task
        assert str(self.task) == 'Test Task'
