# General research into security management for superset

It is important that we are able to configure a user in the phoenix plaform that has access to the
datasets and dashboards for an instance. Here is some initial reseach in to how we might do this
and how this would relate to spesific oauth providers.


## General
Superset uses fab security: https://flask-appbuilder.readthedocs.io/en/latest/security.html#responsible-disclosure

## Roles

docs: https://superset.apache.org/docs/security/
There are three main role set up in superset:
- Admin: does everything
- User: everything apart from user management
- Gamma: only has access to things that data soures they have been given access to.


It would seem that we need to use:
- Admin for admin users
- Gamma for all other users
- Add a role for each instance into superset that gives permissions to read datasets for the
  instance.


## Oauth and roles
It is possibles to customise the additions of roles for an oauth user. 

Currenlty this mapping is hard coded into the superset_config and there is a bit of documentation
[here](https://flask-appbuilder.readthedocs.io/en/latest/security.html#authentication-oauth)
and docs for superset here: https://superset.apache.org/docs/installation/configuring-superset/#mapping-ldap-or-oauth-groups-to-superset-roles

This is the moment in the code here the auth_user_oauth is configured and the user is registered or
the roles are updated: https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/security/manager.py#L1339

We would need to find a way to produce the list of roles based on the userinfo. For each oauth
provider it is going to be different how this is done. 

In this example I was able to override `_oauth_claculate_user_roles` to produce the correct roles.

It might also be possible using AUTH_USER_REGISTRATION_ROLE_JMESPATH: https://github.com/dpgaspar/Flask-AppBuilder/blob/6f00efcce7d6d88a3e957910581c3ac1de19a301/docs/config.rst#using-jmespath-to-map-user-registration-role

### Fief
With fief it would be possible to have the perissions be mapped to the roles in superset. 
