""" trigger/02000146_bf/ia_103.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000178], state=1)
        self.set_actor(triggerId=203, visible=True, initialSequence='Attack_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000178], stateValue=0):
            return NPC등장(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=203, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[403])


class NPC등장(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=403, script='$02000146_BF__IA_103__0$', arg4=3)
        self.set_timer(timerId='1', seconds=15)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[403]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=8)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
