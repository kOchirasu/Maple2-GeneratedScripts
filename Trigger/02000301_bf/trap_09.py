""" trigger/02000301_bf/trap_09.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=218, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=219, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_interact_object(triggerIds=[10000516], state=1)
        self.set_effect(triggerIds=[609], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_mesh(triggerIds=[3091,3092,3093,3094,3095,3096], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[109]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10901]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10902]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10903]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10904]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10905]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10906]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10907]):
            return 경보(self.ctx)
        if self.object_interacted(interactIds=[10000516], stateValue=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=218, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=219, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_interact_object(triggerIds=[10000516], state=0)
        self.create_monster(spawnIds=[2010], animationEffect=False)
        self.set_effect(triggerIds=[609], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.show_guide_summary(entityId=20003001, textId=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(triggerIds=[3091,3092,3093,3094,3095,3096], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2010]):
            self.set_effect(triggerIds=[610], visible=False)
            self.hide_guide_summary(entityId=20003001)
            self.set_actor(triggerId=218, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=219, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2010])
        self.set_mesh(triggerIds=[3091,3092,3093,3094,3095,3096], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929], visible=False, arg3=0, delay=0, scale=5)


initial_state = 시작
