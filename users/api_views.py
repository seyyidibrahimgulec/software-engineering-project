from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Teacher
from users.serializers import TeacherSerializer


class TeachersAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get("department") and request.GET.get("language"):
            try:
                r = TeacherSerializer(
                    Teacher.objects.filter(
                        department=request.GET.get("department"),
                        known_langs=request.GET.get("language"),
                    ),
                    many=True,
                ).data
            except Teacher.DoesNotExist:
                r = {[]}

        return Response(r)
