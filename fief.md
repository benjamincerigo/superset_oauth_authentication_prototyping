# Fief as the authentication

https://docs.fief.dev/self-hosting/quickstart/

## Docker command
```
docker run \
  --name fief-server-2 \
  -p 8000:8000 \
  -e "SECRET=ifcyDPw3ePikRZ2reoiqZbd1lQeBPv8rW8GVTiTUBQR57V3e5zV2X44BwjrN11XW9yHMtdjGZfG5MhfRJCbzSg" \
  -e "FIEF_CLIENT_ID=i6MmAfZueulaNHelc_2bdyXsKNtDhg5Ase8EnLzqK9Y" \
  -e "FIEF_CLIENT_SECRET=g-zyZFwLJIhfaREzAn3s2CsT7vbU7O2rpLJP2jyy8f4" \
  -e "ENCRYPTION_KEY=zsmv2Njm4glWZu8l3vZ7aaKmNBOKgkMd0ZHTZxcYYF0=" \
  -e "PORT=8000" \
  -e "ROOT_DOMAIN=localhost:8000" \
  -e "FIEF_DOMAIN=localhost:8000" \
  -e "FIEF_MAIN_USER_EMAIL=admin@admin.com" \
  -e "FIEF_MAIN_USER_PASSWORD=ifcyDPw3ePikRZ2" \
  -e "CSRF_COOKIE_SECURE=False" \
  -e "SESSION_DATA_COOKIE_SECURE=False" \
  -e "USER_LOCALE_COOKIE_SECURE=False" \
  -e "LOGIN_SESSION_COOKIE_SECURE=False" \
  -e "SESSION_COOKIE_SECURE=False" \
  -e "FIEF_ADMIN_SESSION_COOKIE_SECURE=False" \
  ghcr.io/fief-dev/fief:latest
```

You need to go in and add the redirect url for superset to the fief client:
- go to http://localhost:8000/admin
- login with `admin@admin.com` `ifcyDPw3ePikRZ2`
- go to "Clients" -> "Fief's clients" -> "Edit"
- add a redirect url: `http://localhost:8088/oauth-authorized/fief`


You can then go to `http://localhost:8088` and log in as the `admin@admin.com` oauth.


## Client
Try the fief client:https://docs.fief.dev/integrate/python/

Start a `python` console with the virtual env.
```
from fief_client import Fief

fief = Fief(
    "http://localhost:8000",  
    "i6MmAfZueulaNHelc_2bdyXsKNtDhg5Ase8EnLzqK9Y",
    "g-zyZFwLJIhfaREzAn3s2CsT7vbU7O2rpLJP2jyy8f4",
)

redirect_url = "http://localhost:8000/docs/oauth2-redirect"

auth_url = fief.auth_url(redirect_url, scope=["openid", "permissions"])
print(f"Open this URL in your browser: {auth_url}")
# Code in the URL

code = input("Paste the callback code: ")

tokens, userinfo = fief.auth_callback(code, redirect_url)
print(f"Tokens: {tokens}")
print(f"Userinfo: {userinfo}")
```

## General Evaluation
Fief is interesting as it would be possible to move this into a fastapi project with the use of
fastapi-users: https://fastapi-users.github.io/fastapi-users/latest/
This way if wee need implement something ourselves then it would be easy to move from fief into our
own oauth.

There are some issues with the getting matching of roles in fief with roles in superset and it
might be that we would have to match permissions in fief to roles in superset as it is not
possible/simple
to get roles from the api for a fief user.

It is possible to create and configure users from the api using a client key. 

Currently they don't have a user invite flow.
