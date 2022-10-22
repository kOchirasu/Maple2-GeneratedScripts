""" trigger/02000253_bf/wall_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9003], visible=True)
        set_agent(triggerIds=[9004], visible=True)
        set_mesh(triggerIds=[503,504], visible=True)
        set_mesh(triggerIds=[604,605,606], visible=True)
        set_interact_object(triggerIds=[10000438], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000438], arg2=0):
            return 열기()


class 열기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_mesh(triggerIds=[503,504], visible=False)
        set_mesh(triggerIds=[604,605,606], visible=False)


