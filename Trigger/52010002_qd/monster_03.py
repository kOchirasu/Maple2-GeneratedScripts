""" trigger/52010002_qd/monster_03.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=701, spawnIds=[103]):
            return Event_01()


class Event_01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103]):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113], arg2=False)
        set_conversation(type=1, spawnId=113, script='$52010002_QD__MONSTER_03__0$', arg4=2, arg5=1)


class End(state.State):
    pass


