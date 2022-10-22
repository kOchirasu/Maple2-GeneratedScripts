""" trigger/80000013_bonus/mob_04.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return start()


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104]):
            return wait()


class wait(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[701]):
            return start()
        if wait_tick(waitTick=1500):
            return idle()


class end(state.State):
    pass


