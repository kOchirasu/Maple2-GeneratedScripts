""" trigger/02000336_bf/train_lever_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8161,8162,8163,8164], visible=False) # 안보이는 상태
        set_interact_object(triggerIds=[10000898], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000898], arg2=0):
            return 작동_01()
        if count_users(boxId=709, boxId=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=113, textId=20003363, duration=3000)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000898], arg2=0):
            return 작동_01()


class 작동_01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8161,8162,8163,8164], visible=True, arg4=300, arg5=10) # 파란 선으로
        set_mesh(triggerIds=[8261,8262,8263,8264], visible=False, arg4=300, arg5=10) # 빨간 선이
        set_effect(triggerIds=[7012], visible=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 작동_02()


class 작동_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        set_mesh(triggerIds=[8064,8065,8066,8067,8068], visible=False, arg4=0, arg5=10) # 벽은 사라지고
        set_skill(triggerIds=[5808], isEnable=True) # 벽 날리는 스킬
        set_mesh(triggerIds=[8069], visible=False, arg4=30, arg5=0) # 드럼통 폭발
        set_mesh(triggerIds=[8161,8162,8163,8164], visible=False, arg4=0, arg5=10) # 파란 선도 마저 삭제


