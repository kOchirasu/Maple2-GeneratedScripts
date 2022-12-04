""" trigger/02000187_bf/trigger_01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[101], questIds=[20001281], questStates=[2]):
            return 몹리젠(self.ctx)


class 몹리젠(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,202,203,204,205,206])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205,206]):
            return 쿨타임(self.ctx)


class 쿨타임(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
