from drf_yasg import openapi


REQUEST_PARAMETERS = openapi.Schema(
    title='request_body',
    type=openapi.TYPE_OBJECT,
    properties=dict(
        username=openapi.Schema(title='username', description='Имя пользователя', type=openapi.TYPE_STRING),
        password=openapi.Schema(title='password', description='Пароль пользователя', type=openapi.TYPE_STRING),
    ),
    required=['username', 'password']
)


RESPONSES = {
    200: openapi.Response(
        description='Success.',
        examples={
            'application/json': {
                'token': 'user_token_string',
            }
        }
    ),
    400: 'Bad request',
}


LOGIN_PARAMETERS = {
    'tags': ['users'],
    'request_body': REQUEST_PARAMETERS,
    'responses': RESPONSES,
    'operation_description': 'Авторизует пользователя в системе по имени пользователя и паролю.'
}