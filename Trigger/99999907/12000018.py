""" trigger/99999907/12000018.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000018], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000018], arg2=0):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 종료(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


