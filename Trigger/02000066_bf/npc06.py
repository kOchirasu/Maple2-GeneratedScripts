""" trigger/02000066_bf/npc06.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[605], visible=False)
        self.set_actor(triggerId=206, visible=False, initialSequence='Dead_A')
        self.set_interact_object(triggerIds=[10000374], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return NPC생성(self.ctx)


class NPC생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.create_monster(spawnIds=[2006], animationEffect=False)
        self.set_interact_object(triggerIds=[10000374], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return NPC생성조건(self.ctx)


class NPC생성조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2006]):
            self.set_effect(triggerIds=[605], visible=True)
            self.show_guide_summary(entityId=20000663, textId=20000663)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.destroy_monster(spawnIds=[2006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20000663)
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=206, visible=True, initialSequence='Dead_A')
        self.set_interact_object(triggerIds=[10000374], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000374], stateValue=0):
            return 부활(self.ctx)


class 부활(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.create_monster(spawnIds=[2006], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return NPC대사(self.ctx)


class NPC대사(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=206, visible=False, initialSequence='Dead_A')
        self.set_conversation(type=1, spawnId=2006, script='$02000066_BF__NPC06__1$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2006]):
            return NPC생성조건(self.ctx)


initial_state = 시작
