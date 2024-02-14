SECRET_KEY='j48ZSBLZbP8h7kmsVokj8DtbK2Kzr54+IZV5xwp0O20bEww2j4pn71OT'
ENABLE_PROXY_FIX=True
SESSION_COOKIE_SAMESITE=None
SESSION_COOKIE_SECURE=False
SESSION_COOKIE_HTTPONLY=False
WTF_CSRF_ENABLED=False
TALISMAN_ENABLED=False

from flask_appbuilder.security.manager import (
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
    AUTH_OID,
    AUTH_REMOTE_USER
)
AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True  # allow users who are not already in the FAB DB
AUTH_USER_REGISTRATION_ROLE = "Gamma"  # this role will be given in addition to any AUTH_ROLES_MAPPING
OAUTH_PROVIDERS = [
    { 
        'name':'fief',
        'token_key':'access_token', # Name of the token in the response of access_token_url
        'icon':'fa-address-card',   # Icon for the provider
        'remote_app': {
            'client_id':'i6MmAfZueulaNHelc_2bdyXsKNtDhg5Ase8EnLzqK9Y',  # Client Id (Identify Superset application)
            'client_secret':'g-zyZFwLJIhfaREzAn3s2CsT7vbU7O2rpLJP2jyy8f4', # Secret for this Client Id (Identify Superset application)
            'client_kwargs':{
                'scope': 'openid permissions roles'               # Scope for the Authorization
            },
            'server_metadata_url': 'http://localhost:8000/.well-known/openid-configuration', # URL to get the metadata
            'api_base_url':'http://localhost:8000/', # Base URL for the API

        }
    },
   {
        "name": "keycloak",
        "icon": "fa-key",
        "token_key": "access_token",
        "remote_app": {
            "client_id": "superset",
            "client_secret": "OgnR0vEWQXZZcKx9hKGss6r6fadM24uk",
            # Needed for the userinfo get to work
            'api_base_url':'http://localhost:8080/realms/master/protocol/',
            "client_kwargs": {
                "scope": "openid email profile"
            },
            'server_metadata_url': 'http://localhost:8080/realms/master/.well-known/openid-configuration',

        },
    },
]

AUTH_ROLES_MAPPING = {
    "SUPERSET_ADMIN": ["Admin"],
    "SUPERSET_GAMMA": ["Gamma"],
}

# if we should replace ALL the user's roles each login, or only on registration
AUTH_ROLES_SYNC_AT_LOGIN = True
#  import os.path
#  import sys
#  sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
import custom_sso_security_manager

CUSTOM_SECURITY_MANAGER = custom_sso_security_manager.CustomSsoSecurityManager


FAB_ADD_SECURITY_API = True

PREVENT_UNSAFE_DB_CONNECTIONS = False

