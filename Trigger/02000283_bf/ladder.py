""" trigger/02000283_bf/ladder.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[511], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[512], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[513], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[514], visible=False, animationEffect=False)
        self.set_interact_object(triggerIds=[10000429], state=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[2001]):
            return 반응대기(self.ctx)


class 반응대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000429], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000429], stateValue=0):
            return 사다리생성(self.ctx)


class 사다리생성(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[514], visible=True, animationEffect=True)
        self.set_timer(timerId='10', seconds=10, startDelay=0, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
