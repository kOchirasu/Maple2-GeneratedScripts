""" trigger/02000301_bf/trap_03.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_interact_object(triggerIds=[10000512], state=1)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_mesh(triggerIds=[3031,3032,3033,3034,3035,3036], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4301,4302,4303,4304,4305,4306], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10301]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10302]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10303]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10304]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10305]):
            return 경보(self.ctx)
        if self.object_interacted(interactIds=[10000512], stateValue=0):
            return 해제(self.ctx)


class 경보(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_interact_object(triggerIds=[10000512], state=0)
        self.create_monster(spawnIds=[2004], animationEffect=False)
        self.set_effect(triggerIds=[605], visible=True)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.show_guide_summary(entityId=20003001, textId=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(triggerIds=[3031,3032,3033,3034,3035,3036], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4301,4302,4303,4304,4305,4306], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2004]):
            self.hide_guide_summary(entityId=20003001)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2004])
        self.set_mesh(triggerIds=[3031,3032,3033,3034,3035,3036], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[4301,4302,4303,4304,4305,4306], visible=False, arg3=0, delay=0, scale=5)


initial_state = 시작
