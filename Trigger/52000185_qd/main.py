""" trigger/52000185_qd/main.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        add_buff(boxIds=[2001], skillId=99910280, level=1, arg4=False, arg5=True) # 벨라 변신
        add_buff(boxIds=[2001], skillId=99910280, level=1, arg4=False, arg5=False) # 벨라 변신

    def on_tick(self) -> state.State:
        if true():
            return Ready()


class Ready(state.State):
    def on_enter(self):
        add_buff(boxIds=[2001], skillId=99910280, level=1, arg4=False, arg5=True) # 벨라 변신
        add_buff(boxIds=[2001], skillId=99910280, level=1, arg4=False, arg5=False) # 벨라 변신

    def on_tick(self) -> state.State:
        if true():
            return Idle()


