""" trigger/02000403_bf/buff.xml """
from common import *
import state


#  에디셔널 이펙트를 계속 걸어줌 
class idle(state.State):
    def on_enter(self):
        add_buff(boxIds=[720], skillId=71000009, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return buff_01()


class buff_01(state.State):
    def on_enter(self):
        add_buff(boxIds=[720], skillId=71000009, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


