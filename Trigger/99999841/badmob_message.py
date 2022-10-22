""" trigger/99999841/badmob_message.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if dungeon_variable(varID='901', value=1):
            return 쫄몹1()
        if dungeon_variable(varID='902', value=1):
            return 쫄몹2()
        if dungeon_variable(varID='903', value=1):
            return 쫄몹3()


class 쫄몹1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='방해쫄몹1이 생성되었습니다.\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if wait_tick(waitTick=6000):
            return 대기()


class 쫄몹2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='방해쫄몹2가 생성되었습니다.\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if wait_tick(waitTick=6000):
            return 대기()


class 쫄몹3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='방해쫄몹3이 생성되었습니다.\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if wait_tick(waitTick=6000):
            return 대기()


class 종료(state.State):
    pass


