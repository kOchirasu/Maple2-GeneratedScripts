""" trigger/65000002_bd/bush_06.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        remove_buff(boxId=1001006, skillId=70000075)

    def on_tick(self) -> state.State:
        if count_users(boxId=1001006, boxId=1, operator='Equal'):
            return 버프발동()


class 버프발동(state.State):
    def on_enter(self):
        add_buff(boxIds=[1001006], skillId=70000075, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 버프발동()
        if count_users(boxId=1001006, boxId=1, operator='Greater'):
            return 대기()
        if not user_detected(boxIds=[1001006]):
            return 대기()


class 종료(state.State):
    pass


