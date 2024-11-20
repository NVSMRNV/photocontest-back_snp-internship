
from drf_yasg import openapi


REQUEST_PARAMETERS = openapi.Schema(
    title='request_body',
    type=openapi.TYPE_OBJECT,
    properties=dict(
        username=openapi.Schema(title='username', description='Имя пользователя', type=openapi.TYPE_STRING),
        password=openapi.Schema(title='password', description='Пароль пользователя', type=openapi.TYPE_STRING),
        bio=openapi.Schema(title='bio', description='Дополнительная информация о пользователе', type=openapi.TYPE_STRING),
        email=openapi.Schema(title='email', description='Почта пользователя', type=openapi.TYPE_STRING),
        avatar=openapi.Schema(title='avatar', description='Фото пользователя', type=openapi.TYPE_FILE)
    ),
    required=['username', 'password']
)


RESPONSES = {
    201: openapi.Response(
        description='Success.',
        examples={
            'application/json': {
                'user': {
                    "id": 65,
                    "username": "jerry",
                    "email": "jerry@mail.com",
                    "bio": "Junior python dev.",
                    "updated": "2024-11-20T12:02:31.466753Z",
                    "created": "2024-11-20T12:02:31.466763Z",
                    "avatar": "/media/defaultuser.png"
                }
            }
        }
    ),
    400: openapi.Response(
        description='Bad request.',
    ),
}


REGISTER_PARAMETERS = {
    'tags': ['users'],
    'request_body': REQUEST_PARAMETERS,
    'responses': RESPONSES,
    'operation_description': 'Регистрирует пользователя в системе по имени пользователя и паролю.'
}