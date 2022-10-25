""" trigger/02000304_bf/minion_04.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[114]):
            self.create_monster(spawnIds=[1007,1008], animationEffect=False)
            return 종료체크(self.ctx)
        if self.monster_dead(boxIds=[2001]):
            return 종료체크(self.ctx)


class 종료체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1007,1008]):
            return 대기시간(self.ctx)
        if self.monster_dead(boxIds=[2001]):
            self.destroy_monster(spawnIds=[1007,1008])
            return 대기시간(self.ctx)


class 대기시간(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            self.move_user(mapId=2000304, portalId=10, boxId=114)
            return 대기(self.ctx)


initial_state = 대기
