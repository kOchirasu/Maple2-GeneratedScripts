""" trigger/02000253_bf/wall_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9001], visible=True)
        set_agent(triggerIds=[9002], visible=True)
        set_mesh(triggerIds=[501,502], visible=True)
        set_mesh(triggerIds=[601,602,603], visible=True)
        set_interact_object(triggerIds=[10000437], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000437], arg2=0):
            return 열기()


class 열기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_mesh(triggerIds=[501,502], visible=False)
        set_mesh(triggerIds=[601,602,603], visible=False)


