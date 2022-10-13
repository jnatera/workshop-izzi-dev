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

from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

from polls.views import QuestionViewset,ChoiceViewset

schema_view = get_schema_view(
    openapi.Info(
        title="api-zzi",
        default_version="v1",
        description="Documentación API IZZI Spanner",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="johann188@gmail.com"),
        license=openapi.License(name="S/L"),
    ),
    public=True,
)
router = routers.DefaultRouter()
router.trailing_slash = ''
router.register("questions", QuestionViewset,basename="questions")
router.register("choice", ChoiceViewset)


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
