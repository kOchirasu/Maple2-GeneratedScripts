""" trigger/99999922/event2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[999910]):
            return 진행1(self.ctx)


class 진행1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='300', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1001]):
            return 진행2(self.ctx)


class 진행2(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[999910], skillId=49179111, level=1, isSkillSet=True)
        self.set_timer(timerId='300', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 시작10(self.ctx)


class 시작10(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='400', seconds=60)


initial_state = 대기
