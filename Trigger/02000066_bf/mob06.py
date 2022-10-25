""" trigger/02000066_bf/mob06.xml """
import common


# 파토스
class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[902]): # 33레벨
            return 차타이머3(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[906]): # 35레벨
            return 차타이머6(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[910]): # 35레벨 하드
            return 차타이머9(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[914]):
            return 차타이머12(self.ctx)


class 차타이머3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='5'):
            return 차생성3(self.ctx)


class 차타이머6(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='5'):
            return 차생성6(self.ctx)


class 차타이머9(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='40', seconds=40)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='40'):
            return 차생성9(self.ctx)


class 차타이머12(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='20'):
            return 차생성12(self.ctx)


class 차생성3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1299], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[902]):
            return 소멸(self.ctx)


class 차생성6(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1299], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[906]):
            return 소멸(self.ctx)


class 차생성9(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1299], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[910]):
            return 소멸(self.ctx)


class 차생성12(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1299], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[914]):
            return 소멸(self.ctx)


class 소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1299])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


initial_state = 대기시간
