""" trigger/99999905/cannon.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 대포등장(self.ctx)


class 대포등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1001,1002,1003,1004], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[104]):
            return 소환해제(self.ctx)


class 소환해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1001,1002,1003,1004], arg2=False)


initial_state = 시작
