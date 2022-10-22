""" trigger/02010051_bf/portal02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=30, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=31, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[836], visible=False) # light
        set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6001], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206], visible=True, arg3=0, arg4=0, arg5=0) # grating
        set_mesh(triggerIds=[12001,12002,12003,12004,12005,12006,12007,12008,12009,12010,12011,12012,12013,12014,12015,12016,12017,12018,12019,12020,12021,12022,12023,12024,12025,12026,12027,12028], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000836], state=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9011]):
            return 입장딜레이01()


class 입장딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 가이드준비01()


class 가이드준비01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20105101, textId=20105101, duration=4000) # 길 찾기

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000836], arg2=0):
            return 포털개방01()


class 포털개방01(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=1)
        set_effect(triggerIds=[836], visible=True) # light
        set_effect(triggerIds=[6002], visible=True) # vibrate
        set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206], visible=False, arg3=0, arg4=0, arg5=10) # grating
        set_mesh(triggerIds=[12001,12002,12003,12004,12005,12006,12007,12008,12009,12010,12011,12012,12013,12014,12015,12016,12017,12018,12019,12020,12021,12022,12023,12024,12025,12026,12027,12028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 포털개방02()


class 포털개방02(state.State):
    def on_enter(self):
        set_portal(portalId=30, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=31, visible=True, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000837], arg2=0):
            return 포털폐쇄()


class 포털폐쇄(state.State):
    def on_enter(self):
        set_portal(portalId=30, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=31, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206], visible=True, arg3=0, arg4=0, arg5=2) # grating
        set_effect(triggerIds=[6002], visible=False) # vibrate


