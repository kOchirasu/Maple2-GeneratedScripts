""" trigger/02010051_bf/portal03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6001], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        set_portal(portalId=50, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[837], visible=False) # light
        set_mesh(triggerIds=[2000,2001,2002,2003], visible=True, arg3=0, arg4=0, arg5=0) # invisible barrier
        set_mesh(triggerIds=[2100,2101,2102,2103,2104,2105], visible=True, arg3=0, arg4=0, arg5=0) # invisible barrier
        set_mesh(triggerIds=[2200], visible=True, arg3=0, arg4=0, arg5=0) # fence
        set_mesh(triggerIds=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009], visible=False, arg3=0, arg4=0, arg5=0) # stairs
        set_mesh(triggerIds=[13001,13002,13003,13004,13005,13006,13007,13008,13009,13010,13011,13012,13013,13014,13015,13016,13017,13018,13019,13020,13021,13022,13023,13024,13025,13026,13027,13028,13029,13030,13031,13032,13033,13034,13035,13036,13037,13038,13039], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000837], state=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9012]):
            return 입장딜레이01()


class 입장딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_mesh(triggerIds=[2000,2001,2002,2003], visible=False, arg3=0, arg4=0, arg5=0) # invisible barrier
        set_mesh(triggerIds=[2100,2101,2102,2103,2104,2105], visible=False, arg3=0, arg4=0, arg5=0) # invisible barrier

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 가이드준비01()


class 가이드준비01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20105101, textId=20105101, duration=4000) # 길 찾기

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000837], arg2=0):
            return 포털개방01()


class 포털개방01(state.State):
    def on_enter(self):
        set_user_value(triggerId=7, key='timercheck', value=1)
        set_timer(timerId='10', seconds=2)
        set_portal(portalId=50, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[6003], visible=True) # vibrate
        set_effect(triggerIds=[837], visible=True) # light
        set_random_mesh(triggerIds=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009], visible=True, meshCount=10, arg4=50, delay=50) # stairs
        set_mesh(triggerIds=[13001,13002,13003,13004,13005,13006,13007,13008,13009,13010,13011,13012,13013,13014,13015,13016,13017,13018,13019,13020,13021,13022,13023,13024,13025,13026,13027,13028,13029,13030,13031,13032,13033,13034,13035,13036,13037,13038,13039], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2200], visible=False, arg3=0, arg4=0, arg5=10) # fence

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 대화연출준비01()


class 대화연출준비01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if true():
            return 연출대화01()


class 연출대화01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=3)
        set_conversation(type=2, spawnId=11001319, script='$02010051_BF__PORTAL03__0$', arg4=3)
        set_skip(state=대화연출종료01)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 대화연출종료01()


class 대화연출종료01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=False) # vibrate


