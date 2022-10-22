""" trigger/99999841/debuffactive.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if dungeon_variable(varID='801', value=1):
            return 이동속도감소()
        if dungeon_variable(varID='802', value=1):
            return 공격력감소()
        if dungeon_variable(varID='803', value=1):
            return 체력감소()


class 이동속도감소(state.State):
    def on_enter(self):
        dungeon_variable(varId=801, value=0)
        set_event_ui(type=1, arg2='이동속도 감소 디버프에 걸립니다.', arg3='5000')
        add_buff(boxIds=[9001], skillId=70002581, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if true():
            return None # Missing State: 종료


class 공격력감소(state.State):
    def on_enter(self):
        dungeon_variable(varId=802, value=0)
        set_event_ui(type=1, arg2='공격력 감소 디버프에 걸립니다.', arg3='5000')
        add_buff(boxIds=[9001], skillId=70002591, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if true():
            return None # Missing State: 종료


class 체력감소(state.State):
    def on_enter(self):
        dungeon_variable(varId=803, value=0)
        set_event_ui(type=1, arg2='체력 감소 디버프에 걸립니다.', arg3='5000')
        add_buff(boxIds=[9001], skillId=70002601, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if true():
            return None # Missing State: 종료


