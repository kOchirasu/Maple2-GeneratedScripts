""" trigger/81000003_item/trigger_02.xml """
import common


class 레버(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000225], state=1)
        self.set_mesh(triggerIds=[530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000225], stateValue=0):
            return 바닥열기(self.ctx)


class 바닥열기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='8', seconds=200)
        self.set_mesh(triggerIds=[530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='8'):
            return 레버(self.ctx)


initial_state = 레버
