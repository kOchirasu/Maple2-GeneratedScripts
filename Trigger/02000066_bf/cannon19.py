""" trigger/02000066_bf/cannon19.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[8019])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[8019], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[8019]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            return 시작(self.ctx)


initial_state = 시작
