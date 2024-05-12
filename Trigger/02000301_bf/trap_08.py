""" trigger/02000301_bf/trap_08.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=216, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=217, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_interact_object(triggerIds=[10000515], state=1)
        self.set_effect(triggerIds=[608], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_mesh(triggerIds=[3081,3082,3083,3084,3085,3086], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[108]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10801]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10802]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10803]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10804]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10805]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10806]):
            return 경보(self.ctx)
        if self.object_interacted(interactIds=[10000515], stateValue=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=216, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=217, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_interact_object(triggerIds=[10000515], state=0)
        self.create_monster(spawnIds=[2009], animationEffect=False)
        self.set_effect(triggerIds=[608], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.show_guide_summary(entityId=20003001, textId=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(triggerIds=[3081,3082,3083,3084,3085,3086], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2009]):
            self.hide_guide_summary(entityId=20003001)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=216, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=217, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2009])
        self.set_mesh(triggerIds=[3081,3082,3083,3084,3085,3086], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818], visible=False, arg3=0, delay=0, scale=5)


initial_state = 시작
