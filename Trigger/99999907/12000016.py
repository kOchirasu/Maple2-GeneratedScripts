""" trigger/99999907/12000016.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000016], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000016], stateValue=0):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=11)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


initial_state = 대기
