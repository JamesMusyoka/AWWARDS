from django.test import TestCase

from .models import Project, Profile, Rate

class ProjectTestClass(TestCase):
    def setUp(self):
        self.james= Project(title = 'James', project_image = 'Muito')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Project))

    def test_save_method(self):
        self.james.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.james.save_project()
        projects = Project.objects.all()
        self.assertFalse(len(projects) == 0)

    def test_get_project(self):
        projects = Project.objects.all()
        self.assertFalse(len(projects)>0)

    def tearDown(self):
        Project.objects.all().delete()
        Rate.objects.all().delete()
        Profile.objects.all().delete()

    
class ProfileTestClass(TestCase):
    def setUp(self):
        self.james = Profile(first_name = 'James', email = 'jamesmu475@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james, Profile))

    def test_save_method(self):
        self.james.save_profile()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles) > 0)

    def test_delete_method(self):
        self.james.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    
class RateTestClass(TestCase):
    def setUp(self):
        self.james = Rate(rate = 'James')

    def test_instance(self):
        self.assertTrue(isinstance(self.james, Rate))



    
