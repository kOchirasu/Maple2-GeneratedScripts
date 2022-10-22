""" trigger/02010086_bf/train_open_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000897], state=0)
        set_effect(triggerIds=[7003], visible=False) # 전원 붙는 소리
        set_effect(triggerIds=[7004], visible=False) # 전원 붙는 소리
        set_mesh(triggerIds=[1161,1162,1163], visible=False) # 파랑 안보이는 상태

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000897], arg2=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=113, textId=20003363) # [b:레버]를 조작하여 드럼통을 폭파시키세요.

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000897], arg2=0):
            return 작동_01()

    def on_exit(self):
        hide_guide_summary(entityId=113)


class 작동_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7003], visible=True) # 전원 붙는 소리
        set_effect(triggerIds=[7004], visible=True) # 전원 붙는 소리
        set_mesh(triggerIds=[1171,1172,1173], visible=False, arg4=300, arg5=10) # 빨간 선이
        set_mesh(triggerIds=[1161,1162,1163], visible=True, arg4=300, arg5=10) # 파란 선으로
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 작동_02()


class 작동_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2111], visible=False, arg4=30, arg5=0) # 드럼통 폭발
        set_mesh(triggerIds=[1161,1162,1163], visible=False, arg4=0, arg5=10) # 파란 선도 마저 삭제
        set_mesh(triggerIds=[2101], visible=False, arg4=50, arg5=1) # 유리창 해제
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 벽제거()


class 벽제거(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (켬)


