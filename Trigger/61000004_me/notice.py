""" trigger/61000004_me/notice.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=15, startDelay=0)
        # action name="이벤트UI를설정한다" arg1="1" arg2="$61000004_ME__NOTICE__0$" arg3="4000" arg4="102" /

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 대기(self.ctx)


initial_state = 대기
