""" trigger/02010051_bf/portal01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[835], visible=False) # light
        set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6001], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106], visible=True, arg3=0, arg4=0, arg5=0) # grating
        set_mesh(triggerIds=[11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014,11015,11016,11017,11018,11019,11020,11021,11022,11023,11024,11025,11026,11027,11028], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000835], state=1)
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9010]):
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
        if object_interacted(interactIds=[10000835], arg2=0):
            return 포털개방01()


class 포털개방01(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=1)
        set_effect(triggerIds=[835], visible=True) # light
        set_effect(triggerIds=[6001], visible=True) # vibrate
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106], visible=False, arg3=0, arg4=0, arg5=10) # grating
        set_mesh(triggerIds=[11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014,11015,11016,11017,11018,11019,11020,11021,11022,11023,11024,11025,11026,11027,11028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 포털개방02()


class 포털개방02(state.State):
    def on_enter(self):
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=21, visible=True, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000836], arg2=0):
            return 포털폐쇄()


class 포털폐쇄(state.State):
    def on_enter(self):
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106], visible=True, arg3=0, arg4=0, arg5=2) # grating
        set_effect(triggerIds=[6001], visible=False) # vibrate


