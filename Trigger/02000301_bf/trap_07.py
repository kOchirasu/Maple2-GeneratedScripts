""" trigger/02000301_bf/trap_07.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=214, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=215, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[610], visible=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1103], arg2=False)
        set_mesh(triggerIds=[3071,3072,3073,3074,3075,3076], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3077,3078], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return 경보()
        if user_detected(boxIds=[10701]):
            return 경보()
        if user_detected(boxIds=[10702]):
            return 경보()
        if user_detected(boxIds=[10703]):
            return 경보()
        if monster_dead(boxIds=[1103]):
            return 경보()
        if monster_dead(boxIds=[1005]):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=214, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=215, visible=True, initialSequence='sf_quest_light_A01_On')
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[610], visible=True)
        create_monster(spawnIds=[1006], arg2=False)
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1006')
        create_monster(spawnIds=[2008], arg2=False)
        show_guide_summary(entityId=20003002, textId=20003002)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_conversation(type=1, spawnId=1005, script='$02000301_BF__TRAP_07__1$', arg4=2)
        set_mesh(triggerIds=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3077,3078], visible=False, arg3=0, arg4=0, arg5=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2008]):
            hide_guide_summary(entityId=20003002)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=214, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=215, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2008]):
            set_mesh(triggerIds=[3071,3072,3073,3074,3075,3076], visible=False, arg3=0, arg4=0, arg5=5)
            set_mesh(triggerIds=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], visible=False, arg3=0, arg4=0, arg5=5)
            return 해제()


