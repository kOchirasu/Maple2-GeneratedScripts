""" trigger/02000242_bf/trigger_03_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[705,706], visible=False)
        self.destroy_monster(spawnIds=[622,623,624,625,626,627,628,629,630])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[203]):
            return 몹생성(self.ctx)


class 몹생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[622,623,624,625,626,627,628,629,630], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[622,623,624,625,626,627,628,629,630]):
            return 통과(self.ctx)


class 통과(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
