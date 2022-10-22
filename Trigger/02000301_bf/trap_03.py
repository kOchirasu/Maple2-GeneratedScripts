""" trigger/02000301_bf/trap_03.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_interact_object(triggerIds=[10000512], state=1)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_mesh(triggerIds=[3031,3032,3033,3034,3035,3036], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4301,4302,4303,4304,4305,4306], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 경보()
        if user_detected(boxIds=[10301]):
            return 경보()
        if user_detected(boxIds=[10302]):
            return 경보()
        if user_detected(boxIds=[10303]):
            return 경보()
        if user_detected(boxIds=[10304]):
            return 경보()
        if user_detected(boxIds=[10305]):
            return 경보()
        if object_interacted(interactIds=[10000512], arg2=0):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        set_interact_object(triggerIds=[10000512], state=0)
        create_monster(spawnIds=[2004], arg2=False)
        set_effect(triggerIds=[605], visible=True)
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[610], visible=True)
        show_guide_summary(entityId=20003001, textId=20003001)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_mesh(triggerIds=[3031,3032,3033,3034,3035,3036], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4301,4302,4303,4304,4305,4306], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2004]):
            hide_guide_summary(entityId=20003001)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2004])
        set_mesh(triggerIds=[3031,3032,3033,3034,3035,3036], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[4301,4302,4303,4304,4305,4306], visible=False, arg3=0, arg4=0, arg5=5)


