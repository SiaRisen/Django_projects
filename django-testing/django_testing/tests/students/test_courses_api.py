import pytest
import random
from rest_framework.test import APIClient
from model_bakery import baker
from django.urls import reverse

from students.models import Student, Course
from students.serializers import CourseSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


def test_example():
    assert False, "Just test example"


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
class TestApp:

    def test_get_course_1(self, client, course_factory):

        courses = course_factory(_quantity=10)
        course_id = courses[0].id

        url = reverse('courses-detail', args=[course_id])
        response = client.get(url)
        data = response.json()

        assert response.status_code == HTTP_200_OK
        assert [item.id == data['id'] for item in courses]

    def test_get_list_courses(self, client, course_factory):

        courses = course_factory(_quantity=10)

        url = reverse('courses-list')
        response = client.get(url)
        data = response.json()

        assert response.status_code == HTTP_200_OK
        assert len(data) == len(courses)
        for index, course in enumerate(data):
            assert course['id'] == courses[index].id

    def test_created_course(self, client):

        count = Course.objects.count()
        url = reverse('courses-list')
        response = client.post(url, data={'name': 'Тестовый курс'})

        assert response.status_code == HTTP_201_CREATED
        assert Course.objects.count() == count + 1

    def test_update_course(self, client, course_factory):

        course = course_factory(_quantity=5)
        course_id = course[0].id

        url = reverse('courses-detail', args=[course_id])
        response = client.patch(url, data={'name': 'Обновленный курс'})
        data = response.json()

        assert response.status_code == HTTP_200_OK
        assert data['id'] == course_id
        assert data['name'] == 'Обновленный курс'

    def test_delete_course(self, client, course_factory):

        course = course_factory(_quantity=5)
        course_id = course[0].id
        count = Course.objects.count()

        url = reverse('courses-detail', args=[course_id])
        response = client.delete(url)

        assert response.status_code == HTTP_204_NO_CONTENT
        assert Course.objects.count() == count - 1


@pytest.mark.django_db
def test_filter_id(client, course_factory):

    courses = course_factory(_quantity=10)
    rand_course = random.choice(courses)

    url = reverse('courses-list')
    data = {'id': str(rand_course.id)}
    response = client.get(url, data=data)
    data = response.json()

    assert response.status_code == HTTP_200_OK
    assert len(data) == 1
    assert data[0]['id'] == rand_course.id
    assert data[0]['name'] == rand_course.name


@pytest.mark.django_db
def test_filter_name(client, course_factory):

    courses = course_factory(_quantity=10)
    rand_course = random.choice(courses)

    url = reverse('courses-list')
    data = {'name': str(rand_course.name)}
    response = client.get(url, {'name': rand_course.name})
    data = response.json()

    assert response.status_code == HTTP_200_OK
    assert len(data) == 1
    assert data[0]['id'] == rand_course.id
    assert data[0]['name'] == rand_course.name


@pytest.mark.parametrize('student_count, result', [
    (30, False),
    (21, False),
    (20, True),
    (5, True)
])
@pytest.mark.django_db
def test_max_students(student_count, result):

    student_list = [{'name': f'name {i}'} for i in range(student_count)]
    name = 'Тестовый курс'
    data = {'name': name, 'students': student_list}
    serializer = CourseSerializer()
    try:
        serializer.validate(data)
        result = True
    except serializers.ValidationError:
        result = False
    assert result == result
