""" trigger/02000328_bf/qcomplete.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(key='clearafter', value=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[999999], questIds=[10003061], questStates=[2]):
            return 완료npc리젠()


class 완료npc리젠(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002])

    def on_tick(self) -> state.State:
        if user_value(key='clearafter', value=1):
            return 완료npc킬()


class 완료npc킬(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002])


