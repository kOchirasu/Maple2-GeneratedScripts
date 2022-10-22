""" trigger/02020201_bf/altar3.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 전투시작체크()


class 전투시작체크(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[101]):
            return 생성대기()


class 생성대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='gogo', value=1):
            return 생성대기2()


class 생성대기2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 전투체크()


class 전투체크(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[101]):
            return 제단생성()


class 제단생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제단파괴체크()


class 제단파괴체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[203]):
            return 제단재생성시간()


class 제단재생성시간(state.State):
    def on_enter(self):
        set_ai_extra_data(key='Sidephase', value=1, isModify=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=40000):
            set_ai_extra_data(key='Sidephase', value=-1, isModify=True)
            return 전투체크()


class 종료(state.State):
    pass


