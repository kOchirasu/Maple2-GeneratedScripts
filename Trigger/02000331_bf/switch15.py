""" trigger/02000331_bf/switch15.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000801], state=2) # 외다리 재생성레버 감춤
        set_effect(triggerIds=[4200], visible=False) # 아랫방향 화살표
        set_user_value(key='SecondBridgeOff', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[99993]):
            return 전투체크()


class 전투체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SecondBridgeOff', value=1):
            return 스위치준비()


class 스위치준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[777703], visible=False) # 길 나타남02 사운드 / 외다리
        set_effect(triggerIds=[777804], visible=False) # 길 없어짐02 사운드 /  외다리

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[99995]):
            return 스위치켜기()


class 스위치켜기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        set_interact_object(triggerIds=[10000801], state=0) # 외다리 생성하는 레버01 나타남
        set_interact_object(triggerIds=[10000801], state=1) # 외다리 생성하는 레버01 나타남
        set_effect(triggerIds=[4200], visible=True) # 아랫방향 화살표

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000801]):
            return 외다리재생성()

    def on_exit(self):
        set_effect(triggerIds=[7775], visible=True) # 레버 작동 사운드


class 외다리재생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[90008], visible=False, arg3=0, arg4=0, arg5=0) # 9th barrier OFF
        set_random_mesh(triggerIds=[10040,10041,10042,10043,10044], visible=True, meshCount=5, arg4=100, delay=100)
        set_effect(triggerIds=[777703], visible=True) # 길 나타남02 사운드 / 외다리
        set_effect(triggerIds=[4200], visible=False) # 아랫방향 화살표

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[99992]):
            return 이동안내()


class 이동안내(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        set_mesh(triggerIds=[90008], visible=False, arg3=0, arg4=0, arg5=0) # 9th barrier OFF
        set_random_mesh(triggerIds=[10040,10041,10042,10043,10044], visible=True, meshCount=5, arg4=150, delay=150) # 3rd bridge ON

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


