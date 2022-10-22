""" trigger/61000006_me/trigger_05.xml """
from common import *
import state


class 레버(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000214], state=1)
        set_mesh(triggerIds=[551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000214], arg2=0):
            return 바닥열기()


class 바닥열기(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=200)
        set_mesh(triggerIds=[551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 레버()


