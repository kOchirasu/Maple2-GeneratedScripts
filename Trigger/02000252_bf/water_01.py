""" trigger/02000252_bf/water_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108], visible=False, arg3=0, delay=100)
        self.set_interact_object(triggerIds=[10000409], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000409], stateValue=0):
            return 물(self.ctx)


class 물(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108], visible=True, arg3=0, delay=250)


initial_state = 대기
