""" trigger/02000254_bf/pillar_02.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000441], state=0)
        self.set_skill(triggerIds=[702], enable=False)
        self.set_effect(triggerIds=[444], visible=False)
        self.set_effect(triggerIds=[445], visible=False)
        self.set_effect(triggerIds=[461], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=906, spawnIds=[104]):
            return 반응대기(self.ctx)


class 반응대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000441], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000441], stateValue=0):
            return 스턴(self.ctx)
        if not self.npc_detected(boxId=906, spawnIds=[104]):
            return 시작대기중(self.ctx)


class 스턴(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[444], visible=True)
        self.set_effect(triggerIds=[445], visible=True)
        self.set_effect(triggerIds=[461], visible=True)
        self.set_skill(triggerIds=[702], enable=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스턴2(self.ctx)


class 스턴2(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[702], enable=False)
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
