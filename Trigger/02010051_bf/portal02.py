""" trigger/02010051_bf/portal02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=30, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=31, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[836], visible=False) # light
        self.set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6001], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        self.set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206], visible=True, arg3=0, delay=0, scale=0) # grating
        self.set_mesh(triggerIds=[12001,12002,12003,12004,12005,12006,12007,12008,12009,12010,12011,12012,12013,12014,12015,12016,12017,12018,12019,12020,12021,12022,12023,12024,12025,12026,12027,12028], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000836], state=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9011]):
            return 입장딜레이01(self.ctx)


class 입장딜레이01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 가이드준비01(self.ctx)


class 가이드준비01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20105101, textId=20105101, duration=4000) # 길 찾기

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000836], stateValue=0):
            return 포털개방01(self.ctx)


class 포털개방01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=1)
        self.set_effect(triggerIds=[836], visible=True) # light
        self.set_effect(triggerIds=[6002], visible=True) # vibrate
        self.set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206], visible=False, arg3=0, delay=0, scale=10) # grating
        self.set_mesh(triggerIds=[12001,12002,12003,12004,12005,12006,12007,12008,12009,12010,12011,12012,12013,12014,12015,12016,12017,12018,12019,12020,12021,12022,12023,12024,12025,12026,12027,12028], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 포털개방02(self.ctx)


class 포털개방02(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=30, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=31, visible=True, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000837], stateValue=0):
            return 포털폐쇄(self.ctx)


class 포털폐쇄(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=30, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=31, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206], visible=True, arg3=0, delay=0, scale=2) # grating
        self.set_effect(triggerIds=[6002], visible=False) # vibrate


initial_state = 대기
