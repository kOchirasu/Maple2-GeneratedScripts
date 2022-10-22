""" trigger/02000301_bf/trap_01.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_interact_object(triggerIds=[10000511], state=1)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_mesh(triggerIds=[3011,3012,3013,3014,3015,3016], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4101,4102,4103,4104], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 경보()
        if object_interacted(interactIds=[10000511], arg2=0):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        set_interact_object(triggerIds=[10000511], state=0)
        create_monster(spawnIds=[2002], arg2=False)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[605], visible=True)
        set_effect(triggerIds=[610], visible=True)
        show_guide_summary(entityId=20003001, textId=20003001)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_mesh(triggerIds=[3011,3012,3013,3014,3015,3016], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4101,4102,4103,4104], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            hide_guide_summary(entityId=20003001)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002])
        set_mesh(triggerIds=[3011,3012,3013,3014,3015,3016], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[4101,4102,4103,4104], visible=False, arg3=0, arg4=0, arg5=5)


