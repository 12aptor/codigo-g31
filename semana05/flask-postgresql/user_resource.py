from psycopg2.extras import DictConnection
import bcrypt
from db import get_db_connection
from typing import Dict, Any
from flask import jsonify

class UserResource:
    def list(self):
        conn = get_db_connection()

        try:
            users = []
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('SELECT * FROM users')
                    rows = cursor.fetchall()

                    for row in rows:
                        user = {
                            'id': row[0],
                            'name': row[1],
                            'email': row[2],
                            'created_at': str(row[4])
                        }
                        users.append(user)
            
            return jsonify(users), 200
        except Exception as e:
            return jsonify({
                'message': str(e)
            }), 400
        finally:
            conn.close()

    def create(self, data: Dict[str, Any]):
        conn = get_db_connection()

        try:
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            hashed_pwd = self._hash_password(password)

            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
                        (name, email, hashed_pwd)
                    )
            
            return jsonify({
                'message': 'User created successfully'
            }), 200
        except Exception as e:
            return jsonify({
                'message': str(e)
            }), 400
        finally:
            conn.close()

    def get_by_id(self, user_id: int):
        conn = get_db_connection()

        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
                    row = cursor.fetchone()

                    if row is None:
                        return {
                            'message': 'User not found'
                        }, 404
                    
                    user = {
                        'id': row[0],
                        'name': row[1],
                        'email': row[2],
                        'created_at': str(row[4])
                    }

                    return jsonify(user), 200
        except Exception as e:
            return {
                'message': str(e)
            }, 400
        finally:
            conn.close()

    def update(self, user_id: int, data: Dict[str, Any]):
        conn = get_db_connection()

        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.exuecute('SELECT * FROM users WHERE id = %s', (user_id,))
                    row = cursor.fetchone()

                    if row in None:
                        return {
                            'message': 'User not found'
                        }, 404
                    
                    name = data.get('name')
                    email = data.get('email')
                    
                    cursor.execute(
                        'UPDATE users SET name = %s, email = %s WHERE id = %s',
                        (name, email, user_id)
                    )

                    return {
                        'message': 'User updated successfully'
                    }, 200
        except Exception as e:
            return {
                'message': str(e)
            }, 400
        finally:
            conn.close()

    def delete(self, user_id: int):
        conn = get_db_connection()

        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
                    row = cursor.fetchone()

                    if row is None:
                        return {
                            'message': 'User not found'
                        }, 404
                    
                    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))

                    return {
                        'message': 'User deleted successfully'
                    }, 200
        except Exception as e:
            return {
                'message': str(e)
            }, 400
        finally:
            conn.close()

    def _hash_password(self, password: str) -> str:
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(pwd_bytes, salt)
        return hashed_pwd.decode('utf-8')