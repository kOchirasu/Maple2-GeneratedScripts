""" trigger/02000213_bf/regenmob02.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 소환몹등장(self.ctx)


class 소환몹등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000259], stateValue=1):
            # arg2="0" 을 넣으면 몬스터가  등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음
            self.create_monster(spawnIds=[1002], animationEffect=False)
            return 소멸체크(self.ctx)


class 소멸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000259], stateValue=0):
            return 소멸(self.ctx)
        if self.object_interacted(interactIds=[10000259], stateValue=2):
            return 소멸(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 소환몹등장(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='1')


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1002])
        self.set_timer(timerId='1', seconds=1200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='1')


initial_state = 시작대기중
