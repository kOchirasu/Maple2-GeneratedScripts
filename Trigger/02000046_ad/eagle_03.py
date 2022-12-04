""" trigger/02000046_ad/eagle_03.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000295], state=1)
        self.set_actor(triggerId=203, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000295], stateValue=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=203, visible=False, initialSequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[303], animationEffect=False)
        self.move_npc(spawnId=303, patrolName='MS2PatrolData_203')
        self.set_conversation(type=1, spawnId=303, script='$02000046_AD__EAGLE_03__0$', arg4=2)
        self.set_timer(timerId='1', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[303])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작대기중(self.ctx)


initial_state = 시작대기중
