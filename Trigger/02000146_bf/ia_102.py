""" trigger/02000146_bf/ia_102.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000177], state=1)
        self.set_actor(triggerId=202, visible=True, initialSequence='Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000177], stateValue=0):
            return NPC등장(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=202, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[402])


class NPC등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=402, script='$02000146_BF__IA_102__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[402]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
