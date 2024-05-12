""" trigger/02000301_bf/trap_06.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=213, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_interact_object(triggerIds=[10000514], state=1)
        self.set_effect(triggerIds=[607], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_mesh(triggerIds=[3061,3062,3063,3064,3065,3066], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[106]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10601]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10602]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10603]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10604]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10605]):
            return 경보(self.ctx)
        if self.object_interacted(interactIds=[10000514], stateValue=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=213, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_interact_object(triggerIds=[10000514], state=0)
        self.create_monster(spawnIds=[2007], animationEffect=False)
        self.set_effect(triggerIds=[607], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.show_guide_summary(entityId=20003001, textId=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(triggerIds=[3061,3062,3063,3064,3065,3066], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2007]):
            self.hide_guide_summary(entityId=20003001)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=213, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2007])
        self.set_mesh(triggerIds=[3061,3062,3063,3064,3065,3066], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614], visible=False, arg3=0, delay=0, scale=5)


initial_state = 시작
