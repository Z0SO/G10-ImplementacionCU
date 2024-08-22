Uso y Prueba

    Registro:

    Para registrar un nuevo usuario, usa la ruta /api/register/:

    http

POST /accounts/api/register/
Content-Type: application/json

{
    "username": "nuevo_usuario",
    "password": "nueva_contraseña"
}

Inicio de Sesión:

Para obtener un token, usa la ruta /api/token/:

http

POST /accounts/api/token/
Content-Type: application/json

{
    "username": "tu_usuario",
    "password": "tu_contraseña"
}

Refrescar Token:

Para obtener un nuevo access_token, usa la ruta /api/token/refresh/:

http

    POST /accounts/api/token/refresh/
    Content-Type: application/json

    {
        "refresh": "refresh_token_value"
    }

Resumen

    Registro: Permite a los nuevos usuarios crear cuentas.
    Inicio de Sesión: Usa TokenObtainPairView para autenticar a los usuarios y proporcionar tokens JWT.
    Refrescar Token: Usa TokenRefreshView para obtener un nuevo access_token cuando el original expire.

