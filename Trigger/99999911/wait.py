""" trigger/99999911/wait.xml """
import trigger_api


class 최초(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=701, boxId=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10, startDelay=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100001, textId=26100001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=701, boxId=20):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기2(self.ctx)
        if self.time_expired(timerId='10'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=26100001)


class 대기2(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100002, textId=26100002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=701, boxId=20):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)
        if self.time_expired(timerId='60'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=26100002)


class 종료(trigger_api.Trigger):
    pass


initial_state = 최초
