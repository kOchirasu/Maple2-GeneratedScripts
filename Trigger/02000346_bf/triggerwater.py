""" trigger/02000346_bf/triggerwater.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if count_users(boxId=60001, boxId=1):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=True, arg3=0, arg4=0, arg5=5)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 발판랜덤()


class 발판랜덤(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)
        set_random_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=False, meshCount=8, arg4=0, delay=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 유저체크()
        if monster_dead(boxIds=[101]):
            return None # Missing State: 종료


class 유저체크(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[60002]):
            set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=True, arg3=0, arg4=0, arg5=0)
            return 대기시간()
        if monster_dead(boxIds=[101]):
            return None # Missing State: 종료


