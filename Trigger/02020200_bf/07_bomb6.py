""" trigger/02020200_bf/07_bomb6.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BombOn', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[213], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BombOn', value=2):
            return 종료()
        if monster_dead(boxIds=[213]):
            return 폭탄_터짐()


class 폭탄_터짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2006], visible=False, arg3=1500, arg5=3)

    def on_tick(self) -> state.State:
        if user_value(key='BombOn', value=2):
            return 종료()
        if true():
            return 대기시간()


class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BombOn', value=2):
            return 종료()
        if wait_tick(waitTick=40000):
            set_mesh(triggerIds=[2006], visible=True, arg5=3)
            return 시작()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[213])
        set_mesh(triggerIds=[2006], visible=False, arg3=1500, arg5=3)


