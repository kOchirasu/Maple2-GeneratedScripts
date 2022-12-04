""" trigger/02000304_bf/minion_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[112]):
            self.create_monster(spawnIds=[1003,1004], animationEffect=False)
            return 종료체크(self.ctx)
        if self.monster_dead(boxIds=[2001]):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1003,1004]):
            return 대기시간(self.ctx)
        if self.monster_dead(boxIds=[2001]):
            self.destroy_monster(spawnIds=[1003,1004])
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.move_user(mapId=2000304, portalId=10, boxId=112)
            return 대기(self.ctx)


initial_state = 대기
