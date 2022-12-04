""" trigger/02000313_bf/regenmob05.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=13, spawnIds=[91]):
            return 소환몹등장(self.ctx)


class 소환몹등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103,104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103,104]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


initial_state = 시작대기중
