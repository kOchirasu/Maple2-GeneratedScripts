""" trigger/02000294_bf/main2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[10001])
        destroy_monster(spawnIds=[10002])
        destroy_monster(spawnIds=[10003])
        destroy_monster(spawnIds=[10004])

    def on_tick(self) -> state.State:
        if user_value(key='Battle_01', value=1):
            return 트리거01진행()


class 트리거01진행(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10001], arg2=False)
        create_monster(spawnIds=[10002], arg2=False)
        create_monster(spawnIds=[10003], arg2=False)
        create_monster(spawnIds=[10004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트리거02시작()


class 트리거02시작(state.State):
    def on_enter(self):
        move_npc(spawnId=10001, patrolName='MS2PatrolData0')
        move_npc(spawnId=10002, patrolName='MS2PatrolData1')
        move_npc(spawnId=10003, patrolName='MS2PatrolData2')
        move_npc(spawnId=10004, patrolName='MS2PatrolData3')


