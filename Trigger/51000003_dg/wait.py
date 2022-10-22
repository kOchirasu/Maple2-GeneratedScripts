""" trigger/51000003_dg/wait.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000018], state=2)
        set_interact_object(triggerIds=[11000019], state=2)
        set_interact_object(triggerIds=[11000020], state=2)
        set_interact_object(triggerIds=[11000021], state=2)


