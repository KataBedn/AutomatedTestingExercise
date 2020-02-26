from dotenv import load_dotenv

from utilities.logger import Logger


class CommonEnvironment(object):
    def before_all(self, context):
        context.logger = Logger(context)
        load_dotenv('.env')

    def before_feature(self, context, feature):
        pass

    def before_scenario(self, context, scenario):
        pass

    def before_step(self, context, step):
        context.step = step

    def after_scenario(self, context, scenario):
        pass

    def after_step(self, context, step):
        pass

    def after_all(self, context):
        context.logger.shutdown()
