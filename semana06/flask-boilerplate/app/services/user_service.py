from app.models.user_model import User

class UserService:
    def find_by_email(self, email: str) -> User | None:
        user = User.query.filter_by(email=email).first()
        return user
    

user_service = UserService()