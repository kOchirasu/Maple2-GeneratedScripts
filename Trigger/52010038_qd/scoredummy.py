""" trigger/52010038_qd/scoredummy.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001258], stateValue=0):
            return 점수(self.ctx)
        if self.object_interacted(interactIds=[10001259], stateValue=0):
            return 점수(self.ctx)
        if self.object_interacted(interactIds=[10001260], stateValue=0):
            return 점수(self.ctx)
        if self.object_interacted(interactIds=[10001261], stateValue=0):
            return 점수(self.ctx)
        if self.object_interacted(interactIds=[10001262], stateValue=0):
            return 점수(self.ctx)
        if self.object_interacted(interactIds=[10001263], stateValue=0):
            return 점수(self.ctx)
        if self.object_interacted(interactIds=[10001264], stateValue=0):
            return 점수(self.ctx)
        if self.object_interacted(interactIds=[10001265], stateValue=0):
            return 점수(self.ctx)


class 점수(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4030], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


initial_state = 대기
