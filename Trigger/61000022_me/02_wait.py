""" trigger/61000022_me/02_wait.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=60, startDelay=1, interval=0) # 테스트 수정 가능 지점

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100001, textId=26100001, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9001, boxId=50):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기2(self.ctx)
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100002, textId=26100002, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9001, boxId=50):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
