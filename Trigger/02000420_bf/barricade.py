""" trigger/02000420_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[99]):
            return None # Missing State: 카운트


