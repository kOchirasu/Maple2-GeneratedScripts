""" trigger/02000213_bf/regenmob09.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 소환몹등장(self.ctx)


class 소환몹등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000259], stateValue=1):
            self.create_monster(spawnIds=[1009], animationEffect=False)
            return 소멸체크(self.ctx)


class 소멸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000259], stateValue=0):
            return 소멸(self.ctx)
        if self.object_interacted(interactIds=[10000259], stateValue=2):
            return 소멸(self.ctx)
        if self.monster_dead(boxIds=[1009]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 소환몹등장(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1009])
        self.set_timer(timerId='1', seconds=1200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


initial_state = 시작대기중
