""" trigger/02000301_bf/trap_09.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=218, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=219, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_interact_object(triggerIds=[10000516], state=1)
        set_effect(triggerIds=[609], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_mesh(triggerIds=[3091,3092,3093,3094,3095,3096], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[109]):
            return 경보()
        if user_detected(boxIds=[10901]):
            return 경보()
        if user_detected(boxIds=[10902]):
            return 경보()
        if user_detected(boxIds=[10903]):
            return 경보()
        if user_detected(boxIds=[10904]):
            return 경보()
        if user_detected(boxIds=[10905]):
            return 경보()
        if user_detected(boxIds=[10906]):
            return 경보()
        if user_detected(boxIds=[10907]):
            return 경보()
        if object_interacted(interactIds=[10000516], arg2=0):
            return 해제()


class 경보(state.State):
    def on_enter(self):
        set_actor(triggerId=218, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=219, visible=True, initialSequence='sf_quest_light_A01_On')
        set_interact_object(triggerIds=[10000516], state=0)
        create_monster(spawnIds=[2010], arg2=False)
        set_effect(triggerIds=[609], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[610], visible=True)
        show_guide_summary(entityId=20003001, textId=20003001)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_mesh(triggerIds=[3091,3092,3093,3094,3095,3096], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2010]):
            set_effect(triggerIds=[610], visible=False)
            hide_guide_summary(entityId=20003001)
            set_actor(triggerId=218, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=219, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제()


class 해제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2010])
        set_mesh(triggerIds=[3091,3092,3093,3094,3095,3096], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929], visible=False, arg3=0, arg4=0, arg5=5)


