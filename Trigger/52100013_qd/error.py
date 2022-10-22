""" trigger/52100013_qd/error.xml """
from common import *
import state


#  플레이어 감지 
#  슈팅전 체크 에디셔널 이펙트를 계속 걸어줌 
class ready(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return idle()
        if not is_dungeon_room():
            return quest_idle()


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Error', value=1):
            return end()
        if user_detected(boxIds=[702]):
            return error()


class error(state.State):
    def on_enter(self):
        move_random_user(mapId=52100013, portalId=2, triggerId=702, count=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class quest_idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Error', value=1):
            return end()
        if user_detected(boxIds=[702]):
            return quest_error()
        if quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[1]):
            return end()
        if quest_user_detected(boxIds=[701], questIds=[50100080], questStates=[2]):
            return end()


class quest_error(state.State):
    def on_enter(self):
        move_random_user(mapId=52100013, portalId=2, triggerId=702, count=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return quest_idle()
        if quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[1]):
            return end()
        if quest_user_detected(boxIds=[701], questIds=[50100080], questStates=[2]):
            return end()


class end(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001,1002], visible=False)


