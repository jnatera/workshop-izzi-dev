# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from rest_framework import serializers
from django.http import HttpRequest, HttpResponse
from polls.models import Question
from rest_framework import viewsets

from polls.models import Choice


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Segundo webservice en django -  IZZI.")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionViewset(viewsets.ModelViewSet):
    """
    Question Views
    """
    serializer_class = QuestionSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"


class ChoiceViewset(viewsets.ModelViewSet):
    """

    """
    serializer_class = ChoiceSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
