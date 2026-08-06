from faker import Faker

faker = Faker()

def test_dummy():
    sum = 1 + 1
    assert sum == 2, 'Hubo un error al sumar'

def test_dummy2():
    prod = 2 * 2
    assert prod == 6, 'Hubo un error al multiplicar'

def test_json():
    user = {
        'id': faker.random_int(),
        'name': faker.name(),
        'email': faker.email(),
    }
    assert isinstance(user, dict)
    assert isinstance(user['id'], int)