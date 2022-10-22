""" trigger/02020101_bf/dummysummon.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Dummy', value=1):
            create_monster(spawnIds=[401], arg2=False)
            return 더미소환()


class 더미소환(state.State):
    def on_enter(self):
        set_user_value(triggerId=900008, key='Dummy', value=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 대기()
        if user_value(key='Dummy', value=0):
            return 대기()


