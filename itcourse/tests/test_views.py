import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from itcourse.serializers import *
from itcourse.models import *

client = Client()

class CourseListViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='cooking courses', imgpath='777777')
        self.branche = Branch.objects.create(latitude='848445', longitude='88884', address='Kant')
        self.contact = Contact.objects.create(type=2, value='jkhdfkljshdfkh')
        self.course = Course.objects.create(name='Cooking', description='delicious', logo='@@@@',
                                            category=self.category)

        self.valid_payload = {
            'name': "Cooking",
            'description': "delicious",
            'category': {
                "name": "cooking courses",
                "imgpath": "777777"
            },
            'logo': "@@@@",
            'contacts': [
                {
                    "type": 2,
                    "value": "jkhdfkljshdfkh"
                }
            ],
            'branches': [
                {
                    "latitude": "848445",
                    "longitude": "88884",
                    "address": "Kant"
                }
            ],
        }

        self.invalid_payload = {
            'name': " ",
            'description': "delicious",
            'category': {
                "name": "cooking courses",
                "imgpath": "777777"
            },
            'logo': "@@@@",
            'contacts': [
                {
                    "type": 2,
                    "value": "jkhdfkljshdfkh"
                }
            ],
            'branches': [
                {
                    "latitude": "848445",
                    "longitude": "88884",
                    "address": "Kant"
                }
            ],
        }

    def test_view_get(self):
        response = client.get(reverse('get_post_course'))
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_create_valid_course(self):
        response = client.post(reverse('get_post_course'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_course(self):
        response = client.post(reverse('get_post_course'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CourseDetailViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='cooking courses', imgpath='777777')
        self.branche = Branch.objects.create(latitude='848445', longitude='88884', address= 'Kant')
        self.contact = Contact.objects.create(type=2, value='jkhdfkljshdfkh')
        self.course= Course.objects.create(name='Cooking', description='delicious', logo='@@@@',
                                           category=self.category)

        self.valid_payload= {
                'name': "Cooking",
                'description': "test_description",
                'category': {
                    "name": "cooking courses",
                    "imgpath": "777777"
                },
                'logo': "@@@@",
                'contacts': [
                    {
                        "type": 2,
                        "value": "jkhdfkljshdfkh"
                    }
                ],
                'branches': [
                    {
                        "latitude": "848445",
                        "longitude": "88884",
                        "address": "Kant"
                    }
                ],
            }

        self.invalid_payload = {
            'name': " ",
            'description': "delicious",
            'category': {
                "name": "cooking courses",
                "imgpath": "777777"
            },
            'logo': "@@@@",
            'contacts': [
                {
                    "type": 2,
                    "value": "jkhdfkljshdfkh"
                }
            ],
            'branches': [
                {
                    "latitude": "848445",
                    "longitude": "88884",
                    "address": "Kant"
                }
            ],
        }

    def test_get_valid_course_detail(self):
        response = client.get(reverse('get_delete_course', kwargs={'pk': self.course.pk}))
        course = Course.objects.get(pk=self.course.pk)
        serializer = CourseSerializer(course)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_course_detail(self):
        response = client.get(reverse('get_delete_course', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_delete_course(self):
        response = client.delete(
            reverse('get_delete_course', kwargs={'pk': self.course.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_course', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)







