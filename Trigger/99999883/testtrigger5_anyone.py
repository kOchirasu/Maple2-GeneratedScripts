""" trigger/99999883/testtrigger5_anyone.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[901])

    def on_tick(self) -> state.State:
        if check_user():
            return StartDelay()


class StartDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return CheckAnyOne()


class CheckAnyOne(state.State):
    def on_tick(self) -> state.State:
        if any_one():
            return QuitDelay()


class QuitDelay(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[901])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait()


