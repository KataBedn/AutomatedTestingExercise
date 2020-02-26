from utilities.environments.api import ApiEnvironment
from utilities.environments.common import CommonEnvironment
from utilities.environments.mobile import MobileEnvironment
from utilities.environments.web import WebEnvironment

web = WebEnvironment()
api = ApiEnvironment()
mobile = MobileEnvironment()
common = CommonEnvironment()


def select_environment(context):
    tags = getattr(context, 'tags', [])

    if 'mobile' in tags:
        return mobile

    if 'api' in tags:
        return api

    if 'web' in tags:
        return web

    return common
