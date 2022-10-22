""" trigger/84000006_wd/84000006_wd_wait.xml """
from common import *
import state


# ME공통 대기설정
# 대기 페이즈1&2 반복하다 시간 경과 or 인원 충족 시 게임 시작
# 대기 시작
class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=40, clearAtZero=True, display=False) # 테스트 수정 가능 지점

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 대기()


# 대기 페이즈1
class 대기(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='$84000006_WD__84000006_WD_WAIT__0$', duration=5000, delayTick=1000) # npc대사 : 애프터파티에 오신 것을 환영해요!
        show_guide_summary(entityId=28500001, textId=28500001, duration=5000) # 가이드 : 잠시만 기다리셈

    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=70):
            return 종료()
        if wait_tick(waitTick=5000):
            return 대기2()
        if time_expired(timerId='1'):
            return 종료()


# 대기 페이즈2
class 대기2(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='$84000006_WD__84000006_WD_WAIT__1$', duration=5000, delayTick=1000) # npc대사 : 애프터파티에 오신 것을 환영해요!
        show_guide_summary(entityId=28500002, textId=28500002, duration=5000) # 가이드 : 곧 시작함

    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=70):
            return 종료()
        if wait_tick(waitTick=5000):
            return 대기()
        if time_expired(timerId='1'):
            return 종료()


class 종료(state.State):
    pass


