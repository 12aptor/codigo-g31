from rest_framework import generics, mixins
from .models import (
    Project,
    Issue,
    Tag
)
from .serializers import (
    ProjectSerializer,
    IssueSerializer,
    TagSerializer,
    IssueStatusSerializer,
)
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response

@extend_schema(tags=['Project'])
@extend_schema_view(
    post=extend_schema(
        summary='Registrar un nuevo Project para un Workspace',
        description='Crea un nuevo Project.'
    )
)
class ProjectView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@extend_schema(tags=['Project'])
@extend_schema_view(
    get=extend_schema(
        summary='Obtener un Project',
        description='Obtiene un Project activo por su ID'
    ),
    put=extend_schema(
        summary='Actualizar un Project',
        description='Actualiza un Projeect activo por su ID'
    ),
    delete=extend_schema(
        summary='Eliminar logicamente un Project',
        description='Elimina logicamente un Project activo por su ID'
    ),
)
class ManageProjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_destroy(self, instance: Project):
        instance.soft_delete()

@extend_schema(tags=['Issue'])
class IssueView(generics.CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

@extend_schema(tags=['Issue'])
class IssueStatusView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueStatusSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

@extend_schema(tags=['Project'])
class ProjectIssuesView(generics.ListAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return Issue.objects.filter(project_id=project_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        grouped_data = {
            status[0]: [] for status in Issue.Status.choices
        }

        for issue in serializer.data:
            grouped_data[issue['status']].append(issue)

        return Response(grouped_data)

@extend_schema(tags=["Tag"])
class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

@extend_schema(tags=["Tag"])
class ManageTagView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer