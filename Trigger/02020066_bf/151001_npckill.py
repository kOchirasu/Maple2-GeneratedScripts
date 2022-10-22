""" trigger/02020066_bf/151001_npckill.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NPCKill', value=1):
            return NPCKillWait()


class NPCKillWait(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7500):
            return NPCKill()


class NPCKill(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[15401,15402,15501,15502])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KillEnd()


class KillEnd(state.State):
    def on_enter(self):
        set_user_value(triggerId=151001, key='NPCKill', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


