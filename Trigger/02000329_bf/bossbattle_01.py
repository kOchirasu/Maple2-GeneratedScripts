""" trigger/02000329_bf/bossbattle_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[611], visible=False)
        set_interact_object(triggerIds=[10000759], state=2)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_actor(triggerId=211, visible=True, initialSequence='Closed')
        create_monster(spawnIds=[1011,1012,1013,1014,1015,1016,1017,1018], arg2=False)
        set_effect(triggerIds=[6811], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[5001]):
            return 보스소환()
        if monster_dead(boxIds=[5001,5002]):
            return 닭장열기()


class 보스소환(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=109, textId=20000070) # 보스를 처치하세요!
        set_skip(state=보스전투시작)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[5001,5002]):
            return 닭장열기()
        if time_expired(timerId='3'):
            return 보스전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 보스전투시작(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[5001,5002]):
            return 닭장열기()

    def on_exit(self):
        hide_guide_summary(entityId=109)


class 닭장열기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[611], visible=True)
        set_interact_object(triggerIds=[10000759], state=1)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=103, textId=20000050) # 닭장을 여세요
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000759], arg2=0):
            return 보스전투끝()

    def on_exit(self):
        hide_guide_summary(entityId=103)


class 보스전투끝(state.State):
    def on_enter(self):
        set_effect(triggerIds=[611], visible=False)
        set_effect(triggerIds=[6811], visible=True)
        set_timer(timerId='6', seconds=6)
        set_timer(timerId='2', seconds=2)
        set_actor(triggerId=211, visible=True, initialSequence='Opened')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 닭장오픈()

    def on_exit(self):
        set_achievement(triggerId=106, type='trigger', achieve='ClearSavetheChicken') # ClearSavetheChicken 퀘스트


class 닭장오픈(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        dungeon_clear()
        move_npc(spawnId=1011, patrolName='MS2PatrolData_1010')
        move_npc(spawnId=1012, patrolName='MS2PatrolData_1009')
        move_npc(spawnId=1013, patrolName='MS2PatrolData_1008')
        move_npc(spawnId=1014, patrolName='MS2PatrolData_1007')
        move_npc(spawnId=1015, patrolName='MS2PatrolData_1006')
        move_npc(spawnId=1016, patrolName='MS2PatrolData_1005')
        move_npc(spawnId=1017, patrolName='MS2PatrolData_1004')
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


