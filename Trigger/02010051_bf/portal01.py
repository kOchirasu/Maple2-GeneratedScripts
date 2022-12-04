""" trigger/02010051_bf/portal01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[835], visible=False) # light
        self.set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6001], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106], visible=True, arg3=0, delay=0, scale=0) # grating
        self.set_mesh(triggerIds=[11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014,11015,11016,11017,11018,11019,11020,11021,11022,11023,11024,11025,11026,11027,11028], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000835], state=1)
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9010]):
            return 입장딜레이01(self.ctx)


class 입장딜레이01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 가이드준비01(self.ctx)


class 가이드준비01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20105101, textId=20105101, duration=4000) # 길 찾기

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000835], stateValue=0):
            return 포털개방01(self.ctx)


class 포털개방01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=1)
        self.set_effect(triggerIds=[835], visible=True) # light
        self.set_effect(triggerIds=[6001], visible=True) # vibrate
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106], visible=False, arg3=0, delay=0, scale=10) # grating
        self.set_mesh(triggerIds=[11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014,11015,11016,11017,11018,11019,11020,11021,11022,11023,11024,11025,11026,11027,11028], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 포털개방02(self.ctx)


class 포털개방02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=21, visible=True, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000836], stateValue=0):
            return 포털폐쇄(self.ctx)


class 포털폐쇄(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106], visible=True, arg3=0, delay=0, scale=2) # grating
        self.set_effect(triggerIds=[6001], visible=False) # vibrate


initial_state = 대기
