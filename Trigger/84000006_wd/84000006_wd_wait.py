""" trigger/84000006_wd/84000006_wd_wait.xml """
import trigger_api


# ME공통 대기설정
# 대기 페이즈1&2 반복하다 시간 경과 or 인원 충족 시 게임 시작
# 대기 시작
class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=40, startDelay=1, interval=0) # 테스트 수정 가능 지점

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 대기(self.ctx)


# 대기 페이즈1
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # npc대사 : 애프터파티에 오신 것을 환영해요!
        self.add_balloon_talk(spawnId=102, msg='$84000006_WD__84000006_WD_WAIT__0$', duration=5000, delayTick=1000)
        self.show_guide_summary(entityId=28500001, textId=28500001, duration=5000) # 가이드 : 잠시만 기다리셈

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, minUsers='70'):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기2(self.ctx)
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


# 대기 페이즈2
class 대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # npc대사 : 애프터파티에 오신 것을 환영해요!
        self.add_balloon_talk(spawnId=102, msg='$84000006_WD__84000006_WD_WAIT__1$', duration=5000, delayTick=1000)
        self.show_guide_summary(entityId=28500002, textId=28500002, duration=5000) # 가이드 : 곧 시작함

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, minUsers='70'):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
