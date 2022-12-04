""" trigger/02000298_bf/mob_08.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[109]):
            self.create_monster(spawnIds=[1008], animationEffect=False)
            return 종료(self.ctx)
        if self.user_detected(boxIds=[110]):
            self.create_monster(spawnIds=[1008], animationEffect=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
