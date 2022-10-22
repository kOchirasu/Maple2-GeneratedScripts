""" trigger/80000011_bonus/mainprocess_christmastree.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 이벤트대기중()


class 이벤트대기중(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[201], visible=False, animationEffect=False)
        set_ladder(triggerIds=[202], visible=False, animationEffect=False)
        set_ladder(triggerIds=[203], visible=False, animationEffect=False)
        set_ladder(triggerIds=[204], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 사다리나타남()


class 사다리나타남(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[201], visible=True, animationEffect=True)
        set_ladder(triggerIds=[202], visible=True, animationEffect=True)
        set_ladder(triggerIds=[203], visible=True, animationEffect=True)
        set_ladder(triggerIds=[204], visible=True, animationEffect=True)
        set_timer(timerId='2', seconds=30, clearAtZero=True, display=True, arg5=-90)
        show_guide_summary(entityId=26300385, textId=26300385)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 유저이동()


class 유저이동(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1):
            move_user(mapId=0, portalId=0)
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=26300385)


class 종료(state.State):
    pass


