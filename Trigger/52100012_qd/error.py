""" trigger/52100012_qd/error.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Error', value=1):
            return end()
        if user_detected(boxIds=[702]):
            return error()


class error(state.State):
    def on_enter(self):
        move_random_user(mapId=52100012, portalId=5, triggerId=702, count=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class end(state.State):
    pass


