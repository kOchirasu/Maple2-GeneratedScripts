""" trigger/02100001_bf/11_guidenpcspawn.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9903]):
            return NpcSpawn()


class NpcSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[109], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return CheckUser()


class CheckUser(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9903]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109])


