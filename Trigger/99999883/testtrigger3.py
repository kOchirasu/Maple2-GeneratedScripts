""" trigger/99999883/testtrigger3.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001010], state=0) # FlyingCloud
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9900]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001010], state=1) # FlyingCloud

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001010], stateValue=0):
            return TakeOffFlyingCloud01(self.ctx)


class TakeOffFlyingCloud01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_interact_object(triggerIds=[10001010], state=2) # FlyingCloud
        self.set_visible_breakable_object(triggerIds=[4000], visible=True)
        self.set_breakable(triggerIds=[4000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return TakeOffFlyingCloud02(self.ctx)


class TakeOffFlyingCloud02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=99999883, portalId=100, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TakeOffFlyingCloud03(self.ctx)


class TakeOffFlyingCloud03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return TakeOffFlyingCloud04(self.ctx)


class TakeOffFlyingCloud04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=99999883, portalId=101, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)


initial_state = Wait
