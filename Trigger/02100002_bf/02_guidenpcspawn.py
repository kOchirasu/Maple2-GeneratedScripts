""" trigger/02100002_bf/02_guidenpcspawn.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='GuideNpcSpawn', value=0)
        destroy_monster(spawnIds=[109])

    def on_tick(self) -> state.State:
        if user_value(key='GuideNpcSpawn', value=1):
            return NpcSpawn()


class NpcSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[109], arg2=False)
        move_npc(spawnId=109, patrolName='MS2PatrolData_GuideNpc')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return CheckUser()


class CheckUser(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109])


