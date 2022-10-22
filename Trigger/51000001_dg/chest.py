""" trigger/51000001_dg/chest.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000013,11000014,11000015,11000016,11000017], state=2)


