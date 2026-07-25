from rest_framework import generics
from .models import (
    Workspace,
    WorkspaceMember,
)
from .serializers import (
    WorkspaceSerializer,
    WorkspaceMemberSerializer,
)
from projects.models import Project
from projects.serializers import ProjectSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated

@extend_schema(tags=['Workspace'])
@extend_schema_view(
    get=extend_schema(
        summary='Listar todos los Workspaces',
        description='Obtiene una lista paginada de todos los Workspaces activos en el sistema.'
    ),
    post=extend_schema(
        summary='Registrar un nuevo Workspace',
        description='Crea un nuevo Workspace. Asegúrate de enviar los campos requeridos. Solo accesible para usuarios autenticados.'
    )
)
class WorkspaceView(generics.ListCreateAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        workspace = serializer.save()
        WorkspaceMember.objects.create(
            workspace=workspace,
            user=user,
            role='OWNER'
        )

@extend_schema(tags=['Workspace'])
@extend_schema_view(
    get=extend_schema(
        summary='Obtener un Workspace',
        description='Obtiene un Workspace activo por su ID.'
    ),
    put=extend_schema(
        summary='Actualizar un Workspace',
        description='Actualizar un Workspace activo por su ID.'
    ),
    delete=extend_schema(
        summary='Eliminar logicamente un Workspace',
        description='Eliminar logicamente un Workspace activo por su ID.'
    )
)
class ManageWorkspaceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def perform_destroy(self, instance: Workspace):
        instance.soft_delete()

@extend_schema(tags=["Workspace"])
@extend_schema_view(
    get=extend_schema(
        summary='Listar todos los Miembros del Workspace',
        description='Obtiene una lista paginada de todos los usuarios activos Miembros del Workspace'
    ),
    post=extend_schema(
        summary='Registrar un Miembro en un Workspace',
        description='Añade un Usuario como Miembro de un Workspace. Solo accesible para usuarios autenticados.'
    )
)
class WorkspaceMemberView(generics.CreateAPIView):
    queryset = WorkspaceMember.objects.all()
    serializer_class = WorkspaceMemberSerializer

@extend_schema(tags=['Workspace'])
@extend_schema_view(
    get=extend_schema(
        summary='Listar todos los Projects',
        description='Obtiene una lista paginada de todos los Projects activos de un Workspace'
    )
)
class WorkspaceProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_id')
        return Project.objects.filter(workspace_id=workspace_id)