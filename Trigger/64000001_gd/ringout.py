""" trigger/64000001_gd/ringout.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return 링아웃(self.ctx)


class 링아웃(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.move_user(mapId=64000001, portalId=2, boxId=105)
            return 대기(self.ctx)


initial_state = 대기
