from step.baseStep import BaseStep
from helper.properties import *

## step ##
step = BaseStep();

step.goToHomePage(get_settings()['DEFAULT-BASE-URL']);
step.login(
    get_settings()['USER-LOGIN'],
    get_settings()['USER-PASSWORD']);
step.update_testrail_from_excel();