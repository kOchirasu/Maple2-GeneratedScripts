""" trigger/02100000_bf/monster.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
        set_mesh(triggerIds=[80001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[9500001,9500002,9500003,9500004,9500005,9500006,9500007,9500008,9500009,9500010], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[9600001,9600002,9600003,9600004,9600005,9600006,9600007,9600008,9600009,9600010,9600011,9600012,9600013,9600014], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if true():
            return 유저감지()


class 유저감지(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=True)
        set_portal(portalId=19, visible=False, enabled=False, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[80001], arg2=True)
        create_monster(spawnIds=[800011], arg2=True)
        create_monster(spawnIds=[81001], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 몬스터사망_1()


class 몬스터사망_1(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 몬스터등장_2()


class 몬스터등장_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[80002], arg2=True)
        create_monster(spawnIds=[800021], arg2=True)
        create_monster(spawnIds=[810021], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 몬스터사망_2()


class 몬스터사망_2(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 몬스터등장_3()


class 몬스터등장_3(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[81001])
        destroy_monster(spawnIds=[81002])
        destroy_monster(spawnIds=[810021])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 포탈생성()


class 포탈생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9500001,9500002,9500003,9500004,9500005,9500006,9500007,9500008,9500009,9500010], visible=True, arg3=0, arg4=90, arg5=1)
        set_mesh(triggerIds=[9600001,9600002,9600003,9600004,9600005,9600006,9600007,9600008,9600009,9600010,9600011,9600012,9600013,9600014], visible=True, arg3=0, arg4=90, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 길생성()


class 길생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[80001], visible=False, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return None


