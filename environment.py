from utilities.environments.selector import select_environment


def before_all(context):
    select_environment(context).before_all(context)


def before_feature(context, feature):
    select_environment(context).before_feature(context, feature)


def before_scenario(context, scenario):
    select_environment(context).before_scenario(context, scenario)


def before_step(context, step):
    select_environment(context).before_step(context, step)


def after_scenario(context, scenario):
    select_environment(context).after_scenario(context, scenario)


def after_step(context, step):
    select_environment(context).after_step(context, step)


def after_all(context):
    select_environment(context).after_all(context)
