""" trigger/02010052_bf/torchlight_06.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[6100,6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122], visible=False, arg3=0, arg4=0, arg5=0) # 벽 해제
        set_effect(triggerIds=[7006], visible=False) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> state.State:
        if count_users(boxId=709, boxId=1):
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7543], visible=True) # 얼음이 어는 소리
        set_mesh(triggerIds=[6100,6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122], visible=True, arg3=80, arg4=70, arg5=8) # 얼음!
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return Event_05_01()


class Event_05_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[994]) # 카나 사라짐
        create_monster(spawnIds=[106], arg2=False) # 화롯불 생성
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106]):
            return burn_state()


class burn_state(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=200)
        set_effect(triggerIds=[7506], visible=True) # 얼음 녹는 소리
        set_mesh(triggerIds=[6100,6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_mesh(triggerIds=[600002], visible=False, arg3=0, arg4=0, arg5=0) # 벽 해제 (투명 벽)
        set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_06__0$', arg3='3000')
        set_effect(triggerIds=[7006], visible=True) # 횃불에 불이 붙는 이펙트
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return spawn_state()


class spawn_state(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


