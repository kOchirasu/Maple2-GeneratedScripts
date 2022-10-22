""" trigger/02000207_bf/999102_lavaflow.xml """
from common import *
import state


class 전투체크(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='LavaflowHigh', value=1):
            set_user_value(triggerId=999102, key='LavaflowHigh', value=0)
            return 칸이동3()
        if user_value(key='LavaflowLow', value=1):
            set_user_value(triggerId=999102, key='LavaflowLow', value=0)
            return 칸이동2()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 칸이동3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        create_monster(spawnIds=[1001], arg2=False)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=28000):
            return 리턴()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 칸이동2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        create_monster(spawnIds=[1001], arg2=False)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 리턴()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 리턴(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            destroy_monster(spawnIds=[1001])
            return 대기()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])


