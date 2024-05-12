""" trigger/61000003_me_003/wait.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='60', seconds=60, startDelay=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[610], visible=True)
        self.show_guide_summary(entityId=26100001, textId=26100001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=100, minUsers='50'):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기2(self.ctx)
        if self.time_expired(timerId='60'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=26100001)


class 대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=26100002, textId=26100002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=100, minUsers='50'):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)
        if self.time_expired(timerId='60'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=26100002)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
