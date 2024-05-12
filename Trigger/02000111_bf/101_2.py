""" trigger/02000111_bf/101_2.xml """
import trigger_api


class 시작대기중1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000165], state=1)
        self.set_mesh(triggerIds=[302], visible=False)
        self.set_effect(triggerIds=[402], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000165], stateValue=0):
            return 열기1(self.ctx)


class 시작대기중2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000165], state=1)
        self.set_mesh(triggerIds=[302], visible=False)
        self.set_effect(triggerIds=[402], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000165], stateValue=0):
            return 열기1(self.ctx)


class 열기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[302], visible=True)
        self.set_effect(triggerIds=[402], visible=True)
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=202, spawnIds=[103]):
            return 아이템1(self.ctx)
        if self.npc_detected(boxId=202, spawnIds=[104]):
            return 아이템2(self.ctx)
        if self.npc_detected(boxId=202, spawnIds=[105]):
            return 아이템3(self.ctx)
        if self.time_expired(timerId='1'):
            return 시작대기중2(self.ctx)


class 아이템1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawnIds=[502], triggerId=0, itemId=10000165)
        self.set_mesh(triggerIds=[302], visible=False)
        self.set_interact_object(triggerIds=[10000165], state=1)
        self.set_effect(triggerIds=[402], visible=True)
        self.destroy_monster(spawnIds=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 빠지기1(self.ctx)


class 아이템2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawnIds=[502], triggerId=0, itemId=10000165)
        self.set_mesh(triggerIds=[302], visible=False)
        self.set_interact_object(triggerIds=[10000165], state=1)
        self.set_effect(triggerIds=[402], visible=True)
        self.destroy_monster(spawnIds=[104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 빠지기2(self.ctx)


class 아이템3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawnIds=[502], triggerId=0, itemId=10000165)
        self.set_mesh(triggerIds=[302], visible=False)
        self.set_interact_object(triggerIds=[10000165], state=1)
        self.set_effect(triggerIds=[402], visible=True)
        self.destroy_monster(spawnIds=[105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 빠지기3(self.ctx)


class 빠지기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작대기중2(self.ctx)


class 빠지기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작대기중2(self.ctx)


class 빠지기3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작대기중2(self.ctx)


initial_state = 시작대기중1
