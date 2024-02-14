#!/usr/bin/env python3

import logging
from superset.security import SupersetSecurityManager
from fief_client import Fief

class CustomSsoSecurityManager(SupersetSecurityManager):

    def oauth_user_info(self, provider, response=None):
        logging.debug("Oauth2 provider: {0}.".format(provider))
        if provider == 'fief':
            oauth_conf = self.appbuilder.sm.oauth_remotes[provider].__dict__
            fief = Fief(
                oauth_conf["api_base_url"],
                oauth_conf["client_id"],
                oauth_conf["client_secret"],
            )
            userinfo = fief.userinfo(response["access_token"])
            logging.info("Userinfo: {0}.".format(userinfo))
            if userinfo.get("email") == "admin@admin.com":
                userinfo["role_keys"] = ["SUPERSET_ADMIN"]
            else:
                userinfo["role_keys"] = ["SUPERSET_GAMMA"]
            access_token = fief.validate_access_token(response["access_token"])
            logging.info("permissions: {0}.".format(access_token.get("permissions")))
            userinfo["permissions"] = access_token.get("permissions")
            return userinfo
        else:
            # Irritaitng that this is not oauth_user_info :(
            return self.get_oauth_user_info(provider, response)

    #  def _oauth_calculate_user_roles(self, userinfo) -> list[str]:

        #  fab_role = self.find_role("console_created_role")
        #  return [fab_role] if fab_role else []

