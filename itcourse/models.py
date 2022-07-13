from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    imgpath = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.PROTECT, null=True)
    logo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.description}'


class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.address}, {self.latitude}, {self.longitude}'

class Contact(models.Model):

    class Type(models.IntegerChoices):
        PHONE = 1
        FACEBOOK = 2
        EMAIL = 3

    type = models.IntegerField(choices=Type.choices)
    value = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.value}'


