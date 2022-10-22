""" trigger/02000301_bf/trap_05.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=210, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_interact_object(triggerIds=[10000513], state=1)
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_mesh(triggerIds=[3051,3052,3053,3054,3055,3056], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 경보()
        if user_detected(boxIds=[10501]):
            return 경보()
        if user_detected(boxIds=[10502]):
            return 경보()
        if user_detected(boxIds=[10503]):
            return 경보()
        if user_detected(boxIds=[10504]):
            return 경보()
        if user_detected(boxIds=[10505]):
            return 경보()
        if object_interacted(interactIds=[10000513], arg2=0):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=210, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_On')
        set_interact_object(triggerIds=[10000513], state=0)
        create_monster(spawnIds=[2006], arg2=False)
        set_effect(triggerIds=[606], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[610], visible=True)
        show_guide_summary(entityId=20003001, textId=20003001)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_mesh(triggerIds=[3051,3052,3053,3054,3055,3056], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2006]):
            hide_guide_summary(entityId=20003001)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=210, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2006])
        set_mesh(triggerIds=[3051,3052,3053,3054,3055,3056], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519], visible=False, arg3=0, arg4=0, arg5=5)


