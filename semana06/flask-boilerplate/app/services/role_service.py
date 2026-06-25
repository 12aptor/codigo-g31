from app.models.role_model import Role
from typing import Union

class RoleService:
    def get_by_id(self, role_id: int) -> Union[Role, None]:
        role = Role.query.get(role_id)
        return role
    
role_service = RoleService()