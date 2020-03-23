import datetime
import itertools

from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import Classroom
from timeslots.models import ClassroomUnavailableSlot, TeacherUnavailableSlot
from users.models import Teacher


class TimeAvailableAPIView(APIView):
    def get(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(pk=request.GET.get("teacher"))
        classroom = Classroom.objects.get(pk=request.GET.get("classroom"))
        day = datetime.datetime.strptime(request.GET.get("day"), "%Y-%m-%dT%H:%M:%S.%f")
        day = datetime.datetime(year=day.year, month=day.month, day=day.day)
        end_of_day = day + datetime.timedelta(days=1)

        # get unaviable slots
        unable_from_teach = TeacherUnavailableSlot.objects.filter(
            teacher=teacher, start_datetime__gt=day, end_datetime__lt=end_of_day
        )
        unable_from_class = ClassroomUnavailableSlot.objects.filter(
            classroom=classroom, start_datetime__gt=day, end_datetime__lt=end_of_day
        )

        all_availbles = [x for x in range(24)]

        for unable_item in itertools.chain(unable_from_class, unable_from_teach):
            start_hour = unable_item.start_datetime.hour
            end_hour = unable_item.end_datetime.hour

            try:
                start_index = all_availbles.index(start_hour)
                end_index = all_availbles.index(end_hour)
                del all_availbles[start_index:end_index]

            except ValueError:
                pass

        return Response(all_availbles)
