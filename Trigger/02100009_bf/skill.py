""" trigger/02100009_bf/skill.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='Fencebreak', value=0)
        set_mesh(triggerIds=[10001,10002,10003,10004,10005,10006,10007,10008], visible=True, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[1000001], isEnable=True)
        set_skill(triggerIds=[1000002], isEnable=True)
        set_skill(triggerIds=[1000003], isEnable=True)
        set_skill(triggerIds=[1000004], isEnable=True)
        set_skill(triggerIds=[1000005], isEnable=True)
        set_skill(triggerIds=[1000006], isEnable=True)
        set_skill(triggerIds=[1000007], isEnable=True)
        set_skill(triggerIds=[1000008], isEnable=True)
        set_skill(triggerIds=[1000008], isEnable=True)
        set_skill(triggerIds=[1000008], isEnable=True)
        set_skill(triggerIds=[1000008], isEnable=True)
        set_skill(triggerIds=[1000008], isEnable=True)
        set_skill(triggerIds=[1000009], isEnable=True)
        set_skill(triggerIds=[1000010], isEnable=True)
        set_skill(triggerIds=[1000011], isEnable=True)
        set_skill(triggerIds=[1000012], isEnable=True)
        set_skill(triggerIds=[1000013], isEnable=True)
        set_skill(triggerIds=[1000014], isEnable=True)
        set_skill(triggerIds=[1000015], isEnable=True)
        set_skill(triggerIds=[1000016], isEnable=True)
        set_skill(triggerIds=[1000017], isEnable=True)
        set_skill(triggerIds=[1000018], isEnable=True)
        set_skill(triggerIds=[1000019], isEnable=True)
        set_skill(triggerIds=[1000020], isEnable=True)
        set_skill(triggerIds=[1000021], isEnable=True)
        set_skill(triggerIds=[1000022], isEnable=True)
        set_skill(triggerIds=[1000023], isEnable=True)
        set_skill(triggerIds=[1000024], isEnable=True)
        set_skill(triggerIds=[1000025], isEnable=True)
        set_skill(triggerIds=[1000026], isEnable=True)
        set_skill(triggerIds=[1000027], isEnable=True)
        set_skill(triggerIds=[1000028], isEnable=True)
        set_skill(triggerIds=[1000029], isEnable=True)
        set_skill(triggerIds=[1000030], isEnable=True)
        set_skill(triggerIds=[1000031], isEnable=True)
        set_skill(triggerIds=[1000032], isEnable=True)
        set_skill(triggerIds=[1000033], isEnable=True)
        set_skill(triggerIds=[1000034], isEnable=True)
        set_skill(triggerIds=[1000035], isEnable=True)
        set_skill(triggerIds=[1000036], isEnable=True)
        set_skill(triggerIds=[1000037], isEnable=True)
        set_skill(triggerIds=[1000038], isEnable=True)
        set_skill(triggerIds=[1000039], isEnable=True)
        set_skill(triggerIds=[1000040], isEnable=True)
        set_skill(triggerIds=[1000041], isEnable=True)
        set_skill(triggerIds=[1000042], isEnable=True)
        set_skill(triggerIds=[1000043], isEnable=True)
        set_skill(triggerIds=[1000044], isEnable=True)
        set_skill(triggerIds=[1000045], isEnable=True)
        set_skill(triggerIds=[1000046], isEnable=True)
        set_skill(triggerIds=[1000047], isEnable=True)
        set_skill(triggerIds=[1000048], isEnable=True)

    def on_tick(self) -> state.State:
        if true():
            return 유저감지()


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 스킬사용()


class 스킬사용(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='FenceBreak', value=1):
            return 길막삭제()


class 길막삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10001,10002,10003,10004,10005,10006,10007,10008], visible=False, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[1000001], isEnable=False)
        set_skill(triggerIds=[1000002], isEnable=False)
        set_skill(triggerIds=[1000003], isEnable=False)
        set_skill(triggerIds=[1000004], isEnable=False)
        set_skill(triggerIds=[1000005], isEnable=False)
        set_skill(triggerIds=[1000006], isEnable=False)
        set_skill(triggerIds=[1000007], isEnable=False)
        set_skill(triggerIds=[1000008], isEnable=False)
        set_skill(triggerIds=[1000008], isEnable=False)
        set_skill(triggerIds=[1000008], isEnable=False)
        set_skill(triggerIds=[1000008], isEnable=False)
        set_skill(triggerIds=[1000008], isEnable=False)
        set_skill(triggerIds=[1000009], isEnable=False)
        set_skill(triggerIds=[1000010], isEnable=False)
        set_skill(triggerIds=[1000011], isEnable=False)
        set_skill(triggerIds=[1000012], isEnable=False)
        set_skill(triggerIds=[1000013], isEnable=False)
        set_skill(triggerIds=[1000014], isEnable=False)
        set_skill(triggerIds=[1000015], isEnable=False)
        set_skill(triggerIds=[1000016], isEnable=False)
        set_skill(triggerIds=[1000017], isEnable=False)
        set_skill(triggerIds=[1000018], isEnable=False)
        set_skill(triggerIds=[1000019], isEnable=False)
        set_skill(triggerIds=[1000020], isEnable=False)
        set_skill(triggerIds=[1000021], isEnable=False)
        set_skill(triggerIds=[1000022], isEnable=False)
        set_skill(triggerIds=[1000023], isEnable=False)
        set_skill(triggerIds=[1000024], isEnable=False)
        set_skill(triggerIds=[1000025], isEnable=False)
        set_skill(triggerIds=[1000026], isEnable=False)
        set_skill(triggerIds=[1000027], isEnable=False)
        set_skill(triggerIds=[1000028], isEnable=False)
        set_skill(triggerIds=[1000029], isEnable=False)
        set_skill(triggerIds=[1000030], isEnable=False)
        set_skill(triggerIds=[1000031], isEnable=False)
        set_skill(triggerIds=[1000032], isEnable=False)
        set_skill(triggerIds=[1000033], isEnable=False)
        set_skill(triggerIds=[1000034], isEnable=False)
        set_skill(triggerIds=[1000035], isEnable=False)
        set_skill(triggerIds=[1000036], isEnable=False)
        set_skill(triggerIds=[1000037], isEnable=False)
        set_skill(triggerIds=[1000038], isEnable=False)
        set_skill(triggerIds=[1000039], isEnable=False)
        set_skill(triggerIds=[1000040], isEnable=False)
        set_skill(triggerIds=[1000041], isEnable=False)
        set_skill(triggerIds=[1000042], isEnable=False)
        set_skill(triggerIds=[1000043], isEnable=False)
        set_skill(triggerIds=[1000044], isEnable=False)
        set_skill(triggerIds=[1000045], isEnable=False)
        set_skill(triggerIds=[1000046], isEnable=False)
        set_skill(triggerIds=[1000047], isEnable=False)
        set_skill(triggerIds=[1000048], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return None # Missing State: 끝1


