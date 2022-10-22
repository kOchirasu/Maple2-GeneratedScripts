""" trigger/02000349_bf/wall_16.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623,31624,31625], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[116]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623,31624,31625], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[116]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


