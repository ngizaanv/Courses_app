from django.test import TestCase

from itcourse.models import *

class CoursesModelTestStr(TestCase):
    @classmethod
    def setUpTestData(cls):
        Course.objects.create(name='Destination', description='))((')
        Category.objects.create(name='Language courses', imgpath='jdfihfsdj')
        Branch.objects.create(latitude='41656515', longitude='564661', address='Amsterdam')
        Contact.objects.create(type=1, value='jhdskhf')


    def test_course_str(self):
        course = Course.objects.get(id=1)
        expected_name = f'{course.name}, {course.description}'
        self.assertEqual(expected_name, str(course))


    def test_category_str(self):
        category = Category.objects.get(id=1)
        expected_name = category.name
        self.assertEqual(expected_name, str(category))

    def test_branch_str(self):
        branch = Branch.objects.get(id=1)
        expected_name = f'{branch.address}, {branch.latitude}, {branch.longitude}'
        self.assertEqual(expected_name, str(branch))

    def test_contact_str(self):
        contact = Contact.objects.get(id=1)
        expected_name = contact.value
        self.assertEqual(expected_name, str(contact))


