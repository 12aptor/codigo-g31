from rest_framework import generics
from .models import Workspace
from .serializers import WorkspaceSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

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