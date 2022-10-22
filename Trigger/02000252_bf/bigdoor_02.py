""" trigger/02000252_bf/bigdoor_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[165,166,167,168], visible=True)
        set_interact_object(triggerIds=[10000406], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000406], arg2=0):
            return 열기()


class 열기(state.State):
    def on_enter(self):
        create_item(spawnIds=[9001], triggerId=998)
        set_mesh(triggerIds=[165,166,167,168], visible=False)


