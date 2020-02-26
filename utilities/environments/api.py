import os

from utilities.environments.common import CommonEnvironment


class ApiEnvironment(CommonEnvironment):
    def before_scenario(self, context, scenario):
        super().before_scenario(context, scenario)
        context.base_api_url = os.getenv('API_URL')
        context.logger.info(f'Base API URL is: {context.base_api_url}')
