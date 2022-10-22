""" trigger/99999931/endlever.xml """
from common import *
import state


class 게임종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[211,212], visible=True) # 닫힌 문이 보인다 (arg2=1)
        set_mesh(triggerIds=[551,552], visible=False) # 열린 문을 가린다 (arg2=0)
        set_interact_object(triggerIds=[10000216], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000216], arg2=0):
            return 종료안내()


class 종료안내(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        set_event_ui(type=5, arg3='3000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 문열기()


class 문열기(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=7)
        set_mesh(triggerIds=[211,212], visible=False) # 닫힌 문을 가린다
        set_mesh(triggerIds=[551,552], visible=True) # 열린 문을 보인다

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문닫기()


class 문닫기(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_mesh(triggerIds=[211,212], visible=True) # 닫힌 문을 가린다
        set_mesh(triggerIds=[551,552], visible=False) # 열린 문을 보인다
        set_mesh(triggerIds=[201,202,203,204,205,206,207,208], visible=True) # 순간 이동 발판이 보인다 (arg2=1)
        set_portal(portalId=101, visible=False, enabled=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        set_portal(portalId=102, visible=False, enabled=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        set_portal(portalId=103, visible=False, enabled=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        set_portal(portalId=104, visible=False, enabled=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        set_portal(portalId=115, visible=False, enabled=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        set_portal(portalId=116, visible=False, enabled=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        set_portal(portalId=117, visible=False, enabled=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        set_portal(portalId=118, visible=False, enabled=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 게임종료()


