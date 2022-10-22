""" trigger/84000004_wd/main.xml """
from common import *
import state


class 시작_타이머설정(state.State):
    def on_enter(self):
        set_timer(timerId='4000', seconds=300, clearAtZero=True, display=False) # 5분 타이머. 기념촬영장은 맥시멈 5분만 돌아가도록 한다. 포털을 사용할 수 없기 때문에 시간에 제한을 둔다.
        set_portal(portalId=10001, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if true():
            return 카메라세팅()


class 카메라세팅(state.State):
    def on_enter(self):
        set_photo_studio(isEnable=True) # 자유각도변환 UI ON
        set_portal(portalId=10001, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if true():
            return 강제퇴장대기()


class 강제퇴장대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='exitstudio', value=1):
            return 강제퇴장준비()
        if time_expired(timerId='4000'):
            return 강퇴안내()


class 강퇴안내(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400138) # 가이드 메시지 : 잠시 후, 기념 촬영장이 폐쇄됩니다. 모두 퇴장해 주세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 강제퇴장준비()


class 강제퇴장준비(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=28400138) # 가이드 메시지 : 잠시 후, 기념 촬영장이 폐쇄됩니다. 모두 퇴장해 주세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 강제퇴장()


class 강제퇴장(state.State):
    def on_enter(self):
        room_expire() # 방을 완전 폐쇄해버리는 명령어. 룸스테이지에서 제한시간이 다 되었을때의 처리와 같은 로직


