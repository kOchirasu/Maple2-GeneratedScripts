""" trigger/02000301_bf/trap_06.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=213, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_interact_object(triggerIds=[10000514], state=1)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_mesh(triggerIds=[3061,3062,3063,3064,3065,3066], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 경보()
        if user_detected(boxIds=[10601]):
            return 경보()
        if user_detected(boxIds=[10602]):
            return 경보()
        if user_detected(boxIds=[10603]):
            return 경보()
        if user_detected(boxIds=[10604]):
            return 경보()
        if user_detected(boxIds=[10605]):
            return 경보()
        if object_interacted(interactIds=[10000514], arg2=0):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=213, visible=True, initialSequence='sf_quest_light_A01_On')
        set_interact_object(triggerIds=[10000514], state=0)
        create_monster(spawnIds=[2007], arg2=False)
        set_effect(triggerIds=[607], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[610], visible=True)
        show_guide_summary(entityId=20003001, textId=20003001)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_mesh(triggerIds=[3061,3062,3063,3064,3065,3066], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2007]):
            hide_guide_summary(entityId=20003001)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=213, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2007])
        set_mesh(triggerIds=[3061,3062,3063,3064,3065,3066], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614], visible=False, arg3=0, arg4=0, arg5=5)


