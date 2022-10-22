""" trigger/99999911/fail.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        move_user(mapId=99999911, portalId=1, boxId=702)

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return fail_random()


class fail_random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return fail_01()
        if random_condition(rate=1):
            return fail_02()
        if random_condition(rate=1):
            return fail_03()
        if random_condition(rate=1):
            return fail_04()
        if random_condition(rate=5):
            return fail_04()


class fail_01(state.State):
    def on_enter(self):
        move_user(mapId=99999911, portalId=1, boxId=702)

    def on_tick(self) -> state.State:
        if true():
            return idle()


class fail_02(state.State):
    def on_enter(self):
        move_user(mapId=99999911, portalId=2, boxId=702)

    def on_tick(self) -> state.State:
        if true():
            return idle()


class fail_03(state.State):
    def on_enter(self):
        move_user(mapId=99999911, portalId=3, boxId=702)

    def on_tick(self) -> state.State:
        if true():
            return idle()


class fail_04(state.State):
    def on_enter(self):
        move_user(mapId=99999911, portalId=4, boxId=702)

    def on_tick(self) -> state.State:
        if true():
            return idle()


class fail_05(state.State):
    def on_enter(self):
        move_user(mapId=99999911, portalId=5, boxId=702)

    def on_tick(self) -> state.State:
        if true():
            return idle()


