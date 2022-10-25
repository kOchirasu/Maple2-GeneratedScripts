""" trigger/02000329_bf/03_object.xml """
import common


class 오브젝트_03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1103,1104]):
            return 오브젝트_03_작동(self.ctx)


class 오브젝트_03_작동(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 오브젝트_03_작동_메세지(self.ctx)


class 오브젝트_03_작동_메세지(common.Trigger):
    pass


initial_state = 오브젝트_03
