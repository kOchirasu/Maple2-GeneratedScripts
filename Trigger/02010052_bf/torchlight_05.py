""" trigger/02010052_bf/torchlight_05.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7542], visible=False) # 얼음이 어는 소리
        set_mesh(triggerIds=[6083,6084,6085,6086,6087,6088,6089,6090], visible=False, arg3=0, arg4=0, arg5=0) # 얼음!
        set_mesh(triggerIds=[6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082], visible=False, arg3=0, arg4=0, arg5=0) # 벽 해제
        set_effect(triggerIds=[7005], visible=False) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> state.State:
        if count_users(boxId=708, boxId=1):
            return freeze()


class freeze(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7542], visible=True) # 얼음이 어는 소리
        set_conversation(type=1, spawnId=994, script='$02010052_BF__TORCHLIGHT_05__0$', arg4=3) # 카나 말풍선 대사
        set_mesh(triggerIds=[6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082], visible=True, arg3=80, arg4=100, arg5=8) # 얼음!
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return idle_02()


class idle_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요
        create_monster(spawnIds=[105], arg2=False) # 횃불 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105]):
            return burn_state()


class burn_state(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7505], visible=True) # 얼음 녹는 소리
        set_mesh(triggerIds=[6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082], visible=False, arg3=800, arg4=100, arg5=8) # 벽 해제
        set_mesh(triggerIds=[600001], visible=False, arg3=0, arg4=0, arg5=0) # 벽 해제 (투명 벽)
        set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_05__1$', arg3='3000')
        set_effect(triggerIds=[7005], visible=True) # 횃불에 불이 붙는 이펙트
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return spawn_state()


class spawn_state(state.State):
    def on_enter(self):
        show_guide_summary(entityId=205, textId=20105202) # 카나를 쫓아가세요
        set_conversation(type=1, spawnId=994, script='$02010052_BF__TORCHLIGHT_05__2$', arg4=3) # 카나 말풍선 대사
        move_npc(spawnId=994, patrolName='MS2PatrolData_1007') # 카나의 분신 994 (이동)
        create_monster(spawnIds=[510,511,512,513,514,515], arg2=True) # 카나 정령 몬스터 등장
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return block_spawn()


class block_spawn(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6083,6084,6085,6086,6087,6088,6089,6090], visible=True, arg3=80, arg4=500, arg5=8) # 얼음!


