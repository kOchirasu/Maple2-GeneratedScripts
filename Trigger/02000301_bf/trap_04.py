""" trigger/02000301_bf/trap_04.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=209, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[610], visible=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1102], arg2=False)
        set_mesh(triggerIds=[3041,3042,3043,3044,3045,3046], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3047,3048], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 경보()
        if user_detected(boxIds=[10401]):
            return 경보()
        if user_detected(boxIds=[10402]):
            return 경보()
        if monster_dead(boxIds=[1102]):
            return 경보()
        if monster_dead(boxIds=[1003]):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=209, visible=True, initialSequence='sf_quest_light_A01_On')
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[610], visible=True)
        create_monster(spawnIds=[1004], arg2=False)
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004')
        create_monster(spawnIds=[2005], arg2=False)
        show_guide_summary(entityId=20003002, textId=20003002)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_conversation(type=1, spawnId=1003, script='$02000301_BF__TRAP_04__1$', arg4=2)
        set_mesh(triggerIds=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3047,3048], visible=False, arg3=0, arg4=0, arg5=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2005]):
            hide_guide_summary(entityId=20003002)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=209, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2005]):
            set_mesh(triggerIds=[3041,3042,3043,3044,3045,3046], visible=False, arg3=0, arg4=0, arg5=5)
            set_mesh(triggerIds=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], visible=False, arg3=0, arg4=0, arg5=5)
            return 해제()


