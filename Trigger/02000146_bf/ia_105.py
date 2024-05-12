""" trigger/02000146_bf/ia_105.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000180], state=1)
        self.set_actor(triggerId=205, visible=True, initialSequence='Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000180], stateValue=0):
            return NPC등장(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(triggerId=205, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[405])


class NPC등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=405, script='$02000146_BF__IA_105__0$', arg4=3)
        self.set_timer(timerId='1', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[405]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
