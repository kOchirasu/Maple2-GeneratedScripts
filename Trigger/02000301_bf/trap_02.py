""" trigger/02000301_bf/trap_02.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[610], visible=False)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1101], arg2=False)
        set_mesh(triggerIds=[3021,3022,3023,3024,3025,3026], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3027,3028], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 경보()
        if user_detected(boxIds=[10201]):
            return 경보()
        if user_detected(boxIds=[10202]):
            return 경보()
        if monster_dead(boxIds=[1101]):
            return 경보()
        if monster_dead(boxIds=[1001]):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[605], visible=True)
        set_effect(triggerIds=[610], visible=True)
        create_monster(spawnIds=[1002], arg2=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002')
        create_monster(spawnIds=[2003], arg2=False)
        show_guide_summary(entityId=20003002, textId=20003002)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_conversation(type=1, spawnId=1001, script='$02000301_BF__TRAP_02__1$', arg4=2)
        set_mesh(triggerIds=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3027,3028], visible=False, arg3=0, arg4=0, arg5=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2003]):
            hide_guide_summary(entityId=20003002)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2003]):
            set_mesh(triggerIds=[3021,3022,3023,3024,3025,3026], visible=False, arg3=0, arg4=0, arg5=5)
            set_mesh(triggerIds=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], visible=False, arg3=0, arg4=0, arg5=5)
            return 해제()


