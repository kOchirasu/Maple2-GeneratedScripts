""" trigger/02100004_bf/npc13.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 소환대기()


class 소환대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=999992, key='NpcSpawned13', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawn13', value=1):
            return 소환()


class 소환(state.State):
    def on_enter(self):
        set_user_value(triggerId=999992, key='NpcSpawned13', value=1)
        create_monster(spawnIds=[2013], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 종료(state.State):
    pass


