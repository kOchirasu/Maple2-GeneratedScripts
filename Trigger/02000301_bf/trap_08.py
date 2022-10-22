""" trigger/02000301_bf/trap_08.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=216, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=217, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_interact_object(triggerIds=[10000515], state=1)
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_mesh(triggerIds=[3081,3082,3083,3084,3085,3086], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[108]):
            return 경보()
        if user_detected(boxIds=[10801]):
            return 경보()
        if user_detected(boxIds=[10802]):
            return 경보()
        if user_detected(boxIds=[10803]):
            return 경보()
        if user_detected(boxIds=[10804]):
            return 경보()
        if user_detected(boxIds=[10805]):
            return 경보()
        if user_detected(boxIds=[10806]):
            return 경보()
        if object_interacted(interactIds=[10000515], arg2=0):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=216, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=217, visible=True, initialSequence='sf_quest_light_A01_On')
        set_interact_object(triggerIds=[10000515], state=0)
        create_monster(spawnIds=[2009], arg2=False)
        set_effect(triggerIds=[608], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[610], visible=True)
        show_guide_summary(entityId=20003001, textId=20003001)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_mesh(triggerIds=[3081,3082,3083,3084,3085,3086], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2009]):
            hide_guide_summary(entityId=20003001)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=216, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=217, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2009])
        set_mesh(triggerIds=[3081,3082,3083,3084,3085,3086], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818], visible=False, arg3=0, arg4=0, arg5=5)


