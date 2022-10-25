""" trigger/02000246_bf/trigger_02_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[611,612,613,614,615,616,617,618,619])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[202]):
            return 몹생성(self.ctx)


class 몹생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[611,612,613,614,615,616,617,618,619], animationEffect=False)
        self.set_timer(timerId='1', seconds=120)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[611,612,613,614,615,616,617,618,619]):
            return 통과(self.ctx)


class 통과(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=180)


initial_state = 대기
