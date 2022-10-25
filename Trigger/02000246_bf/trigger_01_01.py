""" trigger/02000246_bf/trigger_01_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[601,602,603,604,605,606,607,608,609])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[201]):
            return 몹생성(self.ctx)


class 몹생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[601,602,603,604,605,606,607,608,609], animationEffect=False)
        self.set_timer(timerId='1', seconds=120)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[601,602,603,604,605,606,607,608,609]):
            return 통과(self.ctx)


class 통과(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=180)


initial_state = 대기
