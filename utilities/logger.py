import logging
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d-%H%M')
logging.basicConfig(
    filename=f'logs/logs-{now}.txt',
    level=logging.INFO,
    format='[%(levelname)-8s %(asctime)s] %(message)s'
)


class Logger:

    def __init__(self, context):
        self.logger = logging.getLogger('automated-tests-logger')
        self.context = context

    def _with_metadata(self, log):
        scenario_name = self.context.scenario.name if hasattr(self.context, 'scenario') else ''
        step_name = self.context.step.name if hasattr(self.context, 'step') else ''
        return f'[{scenario_name}][{step_name}] {log}'

    def debug(self, log):
        log = self._with_metadata(log)
        self.logger.debug(log)

    def info(self, log):
        log = self._with_metadata(log)
        self.logger.info(log)

    def warning(self, log):
        log = self._with_metadata(log)
        self.logger.warning(log)

    def error(self, log):
        log = self._with_metadata(log)
        self.logger.error(log)

    def exception(self, log):
        log = self._with_metadata(log)
        self.logger.exception(log)

    def shutdown(self):
        logging.shutdown()
