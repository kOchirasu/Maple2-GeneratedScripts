""" trigger/02000066_bf/q10003067.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[103], questIds=[50001642], questStates=[2]):
            return 포털활성화(self.ctx)


class 포털활성화(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='woodsoflife', value=1):
            return None # Missing State: 포털비활성화


class 가이드활성화(common.Trigger):
    def on_enter(self):
        self.guide_event(eventId=10003067)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
