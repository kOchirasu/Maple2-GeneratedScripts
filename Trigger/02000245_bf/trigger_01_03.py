""" trigger/02000245_bf/trigger_01_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[601,602,603])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[201]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[601,602,603], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601,602,603]):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)


initial_state = 대기
