""" trigger/02000246_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[601,602,603,604,605,606,607,608,609])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[201]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[601,602,603,604,605,606,607,608,609], animationEffect=False)
        self.set_timer(timerId='1', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601,602,603,604,605,606,607,608,609]):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=180)


initial_state = 대기
