""" trigger/02000335_bf/train_open.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6920], visible=False) # Train_bomb_03
        set_mesh(triggerIds=[6091,6092,6093], visible=False) # 안보이는 상태
        set_interact_object(triggerIds=[10000786], state=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=709, boxId=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=113, textId=20003363) # [b:레버]를 조작하여 드럼통을 폭파시키세요.

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000786], arg2=0):
            return 작동_01()

    def on_exit(self):
        hide_guide_summary(entityId=113)


class 작동_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6922], visible=True) # Train_bomb_03
        set_mesh(triggerIds=[6081,6082,6083], visible=False, arg4=300, arg5=10) # 빨간 선이
        set_mesh(triggerIds=[6091,6092,6093], visible=True, arg4=300, arg5=10) # 파란 선으로
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 작동_02()


class 작동_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6099,6076], visible=False, arg4=30, arg5=0) # 드럼통 폭발
        set_mesh(triggerIds=[6091,6092,6093], visible=False, arg4=0, arg5=10) # 파란 선도 마저 삭제
        set_mesh(triggerIds=[6000], visible=False, arg4=50, arg5=1) # 유리창 해제
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽제거()


class 벽제거(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6920], visible=True) # Train_bomb_03
        set_skill(triggerIds=[5807], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[5808], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[5809], isEnable=True) # 벽 날리는 스킬
        set_mesh(triggerIds=[7071,7072,7073,7074], visible=False, arg4=15, arg5=8) # 벽 해제
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113], arg2=True) # 추가 이벤트 스폰 몬스터
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_01_조건()


class 관문_01_조건(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.
        create_monster(spawnIds=[115,116,137,139], arg2=True) # 추가 이벤트 스폰 몬스터

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[113]):
            return 관문_01_개방()

    def on_exit(self):
        hide_guide_summary(entityId=105)


class 관문_01_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20003362) # 다음 구역으로 이동할 수 있습니다.
        set_mesh(triggerIds=[6211,6212,6213,6214,6215,6216,6217,6218], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 관문_01_개방_02()

    def on_exit(self):
        hide_guide_summary(entityId=106)


class 관문_01_개방_02(state.State):
    pass


