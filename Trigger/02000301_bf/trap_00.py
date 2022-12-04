""" trigger/02000301_bf/trap_00.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=200, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_interact_object(triggerIds=[10000510], state=1)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4001,4002,4003], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return 경보(self.ctx)
        if self.object_interacted(interactIds=[10000510], stateValue=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=200, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_interact_object(triggerIds=[10000510], state=0)
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[605], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.show_guide_summary(entityId=20003001, textId=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4001,4002,4003], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            self.hide_guide_summary(entityId=20003001)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=200, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2001])
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[4001,4002,4003], visible=False, arg3=0, delay=0, scale=5)


initial_state = 시작
