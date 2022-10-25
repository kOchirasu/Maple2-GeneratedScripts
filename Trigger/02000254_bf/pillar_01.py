""" trigger/02000254_bf/pillar_01.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000440], state=0)
        self.set_skill(triggerIds=[701], enable=False)
        self.set_effect(triggerIds=[440], visible=False)
        self.set_effect(triggerIds=[441], visible=False)
        self.set_effect(triggerIds=[442], visible=False)
        self.set_effect(triggerIds=[443], visible=False)
        self.set_effect(triggerIds=[460], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=905, spawnIds=[103]):
            return 반응대기(self.ctx)


class 반응대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000440], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000440], stateValue=0):
            return 스턴(self.ctx)
        if not self.npc_detected(boxId=905, spawnIds=[103]):
            return 시작대기중(self.ctx)


class 스턴(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[440], visible=True)
        self.set_effect(triggerIds=[441], visible=True)
        self.set_effect(triggerIds=[442], visible=True)
        self.set_effect(triggerIds=[443], visible=True)
        self.set_effect(triggerIds=[460], visible=True)
        self.set_skill(triggerIds=[701], enable=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스턴2(self.ctx)


class 스턴2(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[701], enable=False)
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
