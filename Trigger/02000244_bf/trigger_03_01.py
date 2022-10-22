""" trigger/02000244_bf/trigger_03_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[705,706], visible=False)


