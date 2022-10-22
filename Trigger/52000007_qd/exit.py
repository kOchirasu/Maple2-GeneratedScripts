""" trigger/52000007_qd/exit.xml """
from common import *
import state


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 초5()


class 초5(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            create_item(spawnIds=[9001,9002,9003,9004,9005], triggerId=101)
            add_buff(boxIds=[101], skillId=70000019, level=1)
            return 초30()


class 초30(state.State):
    def on_enter(self):
        set_timer(timerId='300', seconds=300, clearAtZero=False)
        set_event_ui(type=1, arg2='$52000007_QD__EXIT__0$', arg3='4000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 유저이동()


class 유저이동(state.State):
    def on_tick(self) -> state.State:
        if true():
            move_user(mapId=2000064, portalId=800, boxId=0)
            return 유저감지()


