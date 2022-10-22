""" trigger/02010086_bf/train_open.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False) # 전원 붙는 소리
        set_effect(triggerIds=[7002], visible=False) # 전원 붙는 소리
        set_mesh(triggerIds=[1061,1062,1063], visible=False) # 안보이는 상태
        set_mesh(triggerIds=[2011,2012,2013], visible=False) # 안보이는 상태
        set_interact_object(triggerIds=[10000896], state=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000896], arg2=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=113, textId=20003363) # [b:레버]를 조작하여 드럼통을 폭파시키세요.

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000896], arg2=0):
            return 작동_01()

    def on_exit(self):
        hide_guide_summary(entityId=113)


class 작동_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=True) # 전원 붙는 소리
        set_effect(triggerIds=[7002], visible=True) # 전원 붙는 소리
        set_mesh(triggerIds=[1071,1072,1073], visible=False, arg4=300, arg5=10) # 빨간 선이
        set_mesh(triggerIds=[1061,1062,1063], visible=True, arg4=300, arg5=10) # 파란 선으로
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 작동_02()


class 작동_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1055], visible=False, arg4=30, arg5=0) # 드럼통 폭발
        set_mesh(triggerIds=[1061,1062,1063], visible=False, arg4=0, arg5=10) # 파란 선도 마저 삭제
        set_mesh(triggerIds=[1005], visible=False, arg4=50, arg5=1) # 유리창 해제
        set_actor(triggerId=1022, visible=True, initialSequence='Opened') # 문 열림
        set_mesh(triggerIds=[1021], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='1', seconds=1)


