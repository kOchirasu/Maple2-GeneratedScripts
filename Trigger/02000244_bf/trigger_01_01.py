""" trigger/02000244_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[701,702], visible=True)
        self.set_mesh(triggerIds=[709,710], visible=True)
        self.destroy_monster(spawnIds=[631,632,633,634,635,636,637,638,639])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[201]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[631,632,633,634,635,636,637,638,639], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[631,632,633,634,635,636,637,638,639]):
            return 통과(self.ctx)
        if self.object_interacted(interactIds=[10000303], stateValue=0):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[701,702], visible=False)
        self.set_mesh(triggerIds=[709,710], visible=False)
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
