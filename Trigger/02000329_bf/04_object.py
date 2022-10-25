""" trigger/02000329_bf/04_object.xml """
import common


class 오브젝트_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1105,1106,1107,1108]):
            return 오브젝트_04_작동(self.ctx)


class 오브젝트_04_작동(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return 오브젝트_04_작동_메세지(self.ctx)


class 오브젝트_04_작동_메세지(common.Trigger):
    pass


initial_state = 오브젝트_04
