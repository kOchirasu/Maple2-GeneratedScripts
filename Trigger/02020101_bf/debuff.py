""" trigger/02020101_bf/debuff.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Debuff', value=1):
            return 디버프시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 디버프시작(state.State):
    def on_enter(self):
        set_user_value(triggerId=900002, key='Debuff', value=0)
        add_buff(boxIds=[1004], skillId=70002122, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='Debuff', value=0):
            return 대기()
        if monster_dead(boxIds=[101]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=900002, key='Debuff', value=0)
        remove_buff(boxId=1004, skillId=70002122, arg3=True)
        add_buff(boxIds=[1004], skillId=70002123, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='Debuff', value=0):
            return 대기()


