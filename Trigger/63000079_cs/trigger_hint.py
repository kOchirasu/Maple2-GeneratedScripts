""" trigger/63000079_cs/trigger_hint.xml """
import trigger_api


class 힌트(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818], visible=True, meshCount=2, arg4=0, delay=1000)
        self.set_timer(timerId='99', seconds=3, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='99'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818], visible=False)
        self.set_timer(timerId='41', seconds=30, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='41'):
            return 힌트(self.ctx)


initial_state = 힌트
