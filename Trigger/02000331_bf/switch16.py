""" trigger/02000331_bf/switch16.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000802], state=2) # 첫번째 다리 재생성레버 감춤
        set_effect(triggerIds=[4100], visible=False) # 아랫방향 화살표
        set_user_value(key='FirstBridgeOff', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 첫번째전투종료()


class 첫번째전투종료(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='FirstBridgeOff', value=1):
            return 딜레이01()


class 딜레이01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 유저재시작()


class 유저재시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 딜레이02()


class 딜레이02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이동안내()


class 이동안내(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        set_interact_object(triggerIds=[10000802], state=0) # 첫번째 다리 재생성레버 나타남
        set_interact_object(triggerIds=[10000802], state=1) # 첫번째 다리 재생성레버 활성화
        set_effect(triggerIds=[4100], visible=True) # 아랫방향 화살표

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 스위치켜기()


class 스위치켜기(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000802]):
            return 다리재생성()


class 다리재생성(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016], visible=True, meshCount=16, arg4=100, delay=100) # 없어졌던 다리 재생성
        set_effect(triggerIds=[777701], visible=True) # 길 나타남01 사운드 / 첫 번째 다리
        set_mesh(triggerIds=[90000], visible=False, arg3=0, arg4=0, arg5=0) # 1st barrier OFF
        set_mesh(triggerIds=[90001], visible=False, arg3=0, arg4=0, arg5=0) # 2nd barrier OFF
        set_effect(triggerIds=[4100], visible=False) # 아랫방향 화살표

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


