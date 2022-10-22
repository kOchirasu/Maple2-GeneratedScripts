""" trigger/02000037_bf/trigger_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], visible=True, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2000]):
            return 발판()
        if monster_in_combat(boxIds=[2001]):
            return 발판()


class 발판(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], visible=False, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 포털등장()


class 포털등장(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000,2001]):
            return 발록죽음()


class 발록죽음(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], visible=True, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


