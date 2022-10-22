""" trigger/02000336_bf/train_open.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[16014,16015,16016], visible=False) # 안보이는 상태
        set_interact_object(triggerIds=[10000805], state=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=706, boxId=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=113, textId=20003363)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000805], arg2=0):
            return 작동_01()

    def on_exit(self):
        hide_guide_summary(entityId=113)


class 작동_01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[16011,16012,16013], visible=False, arg4=300, arg5=10) # 빨간 선이
        set_mesh(triggerIds=[16014,16015,16016], visible=True, arg4=300, arg5=10) # 파란 선으로
        set_effect(triggerIds=[7013], visible=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 작동_02()


class 작동_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        set_skill(triggerIds=[5802], isEnable=True) # 벽 날리는 스킬
        set_mesh(triggerIds=[16001], visible=False, arg4=30, arg5=0) # 드럼통 폭발
        set_mesh(triggerIds=[16014,16015,16016], visible=False, arg4=0, arg5=10) # 파란 선도 마저 삭제
        set_mesh(triggerIds=[16000], visible=False, arg4=50, arg5=1) # 유리창 해제
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return 작동_03()


class 작동_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[305,306,307,308], arg2=False) # 기본 배치 될 몬스터 등장


