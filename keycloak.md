# Keycloak testing


## Set up
```
docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:23.0.6 start-dev
```

Go to admin:
http://localhost:8080/admin/master/console/#/master/clients/add-client

`Name`: superset
`Client Authentication`: check
`Oauth 2.0 ...`: check
Add the valid redirect url: http://localhost:8088/oauth-authorized/keycloak

You need to copy the secret into supereset_config.py

You should now be able to loging with keycloak

Beaware that if you stop the keycloak docker instance it will lose the data

## Keycloak
This seems to work well and is has a resonable comminity.

It would also seem that it is possible to user invitiations:
- https://stackoverflow.com/questions/63778740/keycloak-user-invitation-email

It is also easy to get the roles that have been assigned to a users using the roles scope.
