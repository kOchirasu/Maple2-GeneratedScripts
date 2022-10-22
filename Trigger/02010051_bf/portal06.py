""" trigger/02010051_bf/portal06.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[900], visible=False)
        set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506], visible=True, arg3=0, arg4=0, arg5=0) # Gate Close grating
        set_mesh(triggerIds=[1511,1512,1513], visible=False, arg3=0, arg4=0, arg5=0) # Gate Open grating
        set_effect(triggerIds=[914], visible=False) # light
        set_interact_object(triggerIds=[10000914], state=0)
        set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606], visible=True, arg3=0, arg4=0, arg5=0) # grating
        set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6001], visible=False) # vibrate
        set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6005], visible=False) # MainGateOpen vibrate
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 입장딜레이01()


class 입장딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
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
        set_timer(timerId='2', seconds=3)
        set_conversation(type=2, spawnId=11001319, script='$02010051_BF__PORTAL06__0$', arg4=3)
        set_skip(state=연출대화02대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 연출대화02대기()


class 연출대화02대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 연출대화02()


class 연출대화02(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=4)
        set_conversation(type=2, spawnId=11001319, script='$02010051_BF__PORTAL06__1$', arg4=3)
        set_skip(state=대화연출종료01)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대화연출종료01()


class 대화연출종료01(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 문열기01()


class 문열기01(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[6005], visible=True) # MainGateOpen vibrate
        set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506], visible=False, arg3=0, arg4=0, arg5=10) # Gate Close grating
        set_mesh(triggerIds=[1511,1512,1513], visible=True, arg3=1, arg4=0, arg5=0) # Gate Open grating

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 유저입장01()


class 유저입장01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 가이드준비()


class 가이드준비(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=7) # VoicePlay

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 가이드시작()


class 가이드시작(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20105101, textId=20105101, duration=4000) # 길 찾기
        set_interact_object(triggerIds=[10000914], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000914], arg2=0):
            return 포털개방01()


class 포털개방01(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=1)
        set_effect(triggerIds=[914], visible=True) # light
        set_effect(triggerIds=[6000], visible=True) # DoorOpen vibrate
        set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606], visible=False, arg3=0, arg4=0, arg5=10) # grating

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 포털개방02()


class 포털개방02(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=11, visible=True, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000835], arg2=0):
            return 포털폐쇄()


class 포털폐쇄(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606], visible=True, arg3=0, arg4=0, arg5=2) # grating
        set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6005], visible=False) # MainGateOpen vibrate


