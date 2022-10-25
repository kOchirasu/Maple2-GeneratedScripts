""" trigger/02000245_bf/trigger_02_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[703,704], visible=False)
        self.destroy_monster(spawnIds=[604,605,606,607,608,609,610,611,612])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[202]):
            return 몹생성(self.ctx)


class 몹생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[604,605,606,607,608,609,610,611,612], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[604,605,606,607,608,609,610,611,612]):
            return 통과(self.ctx)


class 통과(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[703,704], visible=False)
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
