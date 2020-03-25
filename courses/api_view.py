import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import Classroom, Language, Lesson
from courses.serializers import ClassroomSerializer
from timeslots.models import ClassroomUnavailableSlot, TeacherUnavailableSlot
from users.models import Teacher, User


class ClassRoomAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get("department"):
            try:
                r = ClassroomSerializer(
                    Classroom.objects.filter(department=request.GET.get("department")),
                    many=True,
                ).data
            except Classroom.DoesNotExist:
                r = {[]}

        return Response(r)


class CreateLessonAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # TODO: make post
        name = request.GET.get("name")
        teacher = Teacher.objects.get(pk=request.GET.get("teacher"))
        classroom = Classroom.objects.get(id=request.GET.get("classroom"))
        start_hour = int(request.GET.get("start_hour"))
        end_hour = int(request.GET.get("end_hour"))
        language = request.GET.get("language")
        day = datetime.datetime.strptime(request.GET.get("day"), "%Y-%m-%dT%H:%M:%S.%f")
        day = datetime.datetime(year=day.year, month=day.month, day=day.day)

        lesson = Lesson.objects.create(
            name=name,
            classroom=classroom,
            teacher=teacher,
            language=Language.objects.get(id=language),
            degree=1,
        )

        TeacherUnavailableSlot.objects.create(
            start_datetime=day + datetime.timedelta(hours=start_hour),
            end_datetime=day + datetime.timedelta(hours=end_hour),
            teacher=teacher,
            lesson=lesson,
        )

        ClassroomUnavailableSlot.objects.create(
            start_datetime=day + datetime.timedelta(hours=start_hour),
            end_datetime=day + datetime.timedelta(hours=end_hour),
            classroom=classroom,
            lesson=lesson,
        )

        return Response("mk")
