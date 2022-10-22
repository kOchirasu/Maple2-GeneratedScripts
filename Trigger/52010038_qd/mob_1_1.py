""" trigger/52010038_qd/mob_1_1.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='WaveStart', value=1):
            return 생성()

    def on_exit(self):
        spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True)
        spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True)
        spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True)
        create_monster(spawnIds=[2011], arg2=True)


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2011], arg2=True)
        spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True, randomPickCount=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 생성()
        if user_value(key='WaveSlowDown', value=1):
            return 생성2()
        if user_value(key='WaveEnd', value=1):
            return 종료()


class 생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2011], arg2=True)
        spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True, randomPickCount=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return 생성2()
        if user_value(key='WaveEnd', value=1):
            return 종료()


class 종료(state.State):
    pass


