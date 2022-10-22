""" trigger/52000094_qd/52000094_trigger.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3003,3004], visible=False)
        destroy_monster(spawnIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9100], questIds=[50100500], questStates=[1]):
            return 진행중일때20002275()
        if quest_user_detected(boxIds=[9100], questIds=[20002275], questStates=[1]):
            return 진행중일때20002275()


class 진행중일때20002275(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009], arg2=False) # ,90537,90539

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]):
            return 진행중일때20002275()


