""" trigger/02000348_bf/heal01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000803], state=0)
        set_skill(triggerIds=[701], isEnable=False)


