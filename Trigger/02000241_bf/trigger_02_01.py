""" trigger/02000241_bf/trigger_02_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[703,704], visible=False)
        self.destroy_monster(spawnIds=[613,614,615,616,617,618,619,620,621])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[202]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[613,614,615,616,617,618,619,620,621], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[613,614,615,616,617,618,619,620,621]):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
