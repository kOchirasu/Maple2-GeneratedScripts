""" trigger/02000421_bf/main.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6001], visible=False)
        set_mesh(triggerIds=[6002], visible=False)
        set_mesh(triggerIds=[6003], visible=False)
        set_mesh(triggerIds=[6004], visible=False)
        set_mesh(triggerIds=[6005], visible=False)
        set_mesh(triggerIds=[6006], visible=False)
        set_mesh(triggerIds=[6007], visible=False)
        set_mesh(triggerIds=[6008], visible=False)
        set_mesh(triggerIds=[6009], visible=False)
        set_mesh(triggerIds=[6010], visible=False)
        set_mesh(triggerIds=[6011], visible=False)
        set_mesh(triggerIds=[6012], visible=False)
        set_mesh(triggerIds=[6013], visible=False)
        set_mesh(triggerIds=[6014], visible=False)
        set_mesh(triggerIds=[6015], visible=False)
        set_mesh(triggerIds=[6016], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=700, boxId=1):
            return Ready_Idle()


class Ready_Idle(state.State):
    pass


