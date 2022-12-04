""" trigger/02020098_bf/message.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[11]):
            return 크리스탈활용안내메시지출력(self.ctx)


class 크리스탈활용안내메시지출력(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=29200002, textId=29200002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6300):
            return 트리거종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=29200002)


class 트리거종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
