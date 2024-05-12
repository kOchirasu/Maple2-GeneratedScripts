""" trigger/02000244_bf/trigger_02_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[703,704], visible=True)
        self.destroy_monster(spawnIds=[622,623,624,625,626,627,628,629,630])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[202]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[622,623,624,625,626,627,628,629,630], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[622,623,624,625,626,627,628,629,630]):
            return 통과(self.ctx)
        if self.object_interacted(interactIds=[10000302], stateValue=0):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[703,704], visible=False)
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
