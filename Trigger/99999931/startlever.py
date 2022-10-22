""" trigger/99999931/startlever.xml """
from common import *
import state


class 시작레버(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[211,212], visible=True) # 닫힌 문이 보인다 (arg2=1)
        set_mesh(triggerIds=[551,552], visible=False) # 열린 문을 가린다 (arg2=0)
        set_portal(portalId=500, visible=False, enabled=True) # 탈락자용 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)
        set_interact_object(triggerIds=[10000215], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000215], arg2=0):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[201,202,203,204,205,206,207,208], visible=False) # 순간 이동 발판이 사라진다
        set_portal(portalId=101, visible=False, enabled=False) # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        set_portal(portalId=102, visible=False, enabled=False) # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        set_portal(portalId=103, visible=False, enabled=False) # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        set_portal(portalId=104, visible=False, enabled=False) # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        set_portal(portalId=115, visible=False, enabled=False) # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        set_portal(portalId=116, visible=False, enabled=False) # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        set_portal(portalId=117, visible=False, enabled=False) # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        set_portal(portalId=118, visible=False, enabled=False) # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다

    def on_tick(self) -> state.State:
        if true():
            return 게임준비()


class 게임준비(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=3)
        set_event_ui(type=1, arg2='$99999931__STARTLEVER__0$', arg3='4000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 시작레버()


