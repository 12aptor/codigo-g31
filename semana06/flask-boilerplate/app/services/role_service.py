from app.models.role_model import Role
from app.schemas.role_schema import RoleSchema
from db import db

class RoleService:
    def get_by_id(self, role_id: int) -> Role | None:
        role = Role.query.get(role_id)
        return role
    
    def get_all(self) -> list[Role]:
        roles = Role.query.all()
        return roles
    
    def create(self, data: RoleSchema) -> Role:
        role = Role(
            name=data.name
        )
        db.session.add(role)
        db.session.commit()
        return role
    
    def update(self, role: Role, data: RoleSchema) -> Role:
        role.name = data.name
        db.session.commit()
        return role
    
    def delete(self, role: Role) -> None:
        db.session.delete(role)
        db.session.commit()
        return None
    
role_service = RoleService()