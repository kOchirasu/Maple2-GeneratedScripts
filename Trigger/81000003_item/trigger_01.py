""" trigger/81000003_item/trigger_01.xml """
import common


class 레버(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000223], state=1)
        self.set_interact_object(triggerIds=[10000214], state=1)
        self.set_mesh(triggerIds=[307,308,309,310,311,312,313,314,315,316,317,318,319], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000223], stateValue=0):
            return 다리01(self.ctx)


class 다리01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_mesh(triggerIds=[307,308], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 다리02(self.ctx)


class 다리02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=1)
        self.set_mesh(triggerIds=[309,310,311], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 다리03(self.ctx)


class 다리03(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=1)
        self.set_mesh(triggerIds=[312,313,314], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 다리04(self.ctx)


class 다리04(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=1)
        self.set_mesh(triggerIds=[315,316,317], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 다리05(self.ctx)


class 다리05(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=1)
        self.set_mesh(triggerIds=[318,319], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 다리06(self.ctx)


class 다리06(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='6'):
            return 레버(self.ctx)


initial_state = 레버
