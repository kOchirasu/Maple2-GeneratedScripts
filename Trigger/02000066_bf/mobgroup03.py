""" trigger/02000066_bf/mobgroup03.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1501])
        self.destroy_monster(spawnIds=[1502])
        self.destroy_monster(spawnIds=[1503])
        self.destroy_monster(spawnIds=[1504])
        self.destroy_monster(spawnIds=[1505])
        self.destroy_monster(spawnIds=[1506])
        self.destroy_monster(spawnIds=[1507])
        self.destroy_monster(spawnIds=[1508])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 대기시간(self.ctx)


# 디펜스 모드 :  해골 자코 모둠
class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[900]):
            return 차타이머1(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[901]):
            return 차타이머2(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[902]): # 33레벨
            return 차타이머3(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[904]):
            return 차타이머4(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[905]):
            return 차타이머5(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[906]): # 35레벨
            return 차타이머6(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[908]):
            return 차타이머7(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[909]):
            return 차타이머8(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[910]): # 35레벨 하드
            return 차타이머9(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[912]):
            return 차타이머10(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[913]):
            return 차타이머11(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[914]):
            return 차타이머12(self.ctx)


class 차타이머1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='14', seconds=14)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[900]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='14'):
            return 대기시간(self.ctx)


class 차타이머2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=6)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[901]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='6'):
            return 대기시간(self.ctx)


class 차타이머3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=11)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='11'):
            return 대기시간(self.ctx)


class 차타이머4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=11)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[904]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='11'):
            return 대기시간(self.ctx)


class 차타이머5(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[905]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='5'):
            return 대기시간(self.ctx)


class 차타이머6(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='10'):
            return 대기시간(self.ctx)


class 차타이머7(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=11)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='11'):
            return 대기시간(self.ctx)


class 차타이머8(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[909]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='5'):
            return 대기시간(self.ctx)


class 차타이머9(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='10'):
            return 대기시간(self.ctx)


class 차타이머10(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='14', seconds=14)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='14'):
            return 대기시간(self.ctx)


class 차타이머11(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='7', seconds=7)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[913]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='7'):
            return 대기시간(self.ctx)


class 차타이머12(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='13', seconds=13)
        self.create_monster(spawnIds=[1501], animationEffect=False)
        self.create_monster(spawnIds=[1502], animationEffect=False)
        self.create_monster(spawnIds=[1503], animationEffect=False)
        self.create_monster(spawnIds=[1504], animationEffect=False)
        self.create_monster(spawnIds=[1505], animationEffect=False)
        self.create_monster(spawnIds=[1506], animationEffect=False)
        self.create_monster(spawnIds=[1507], animationEffect=False)
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='13'):
            return 대기시간(self.ctx)


class 소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1501])
        self.destroy_monster(spawnIds=[1502])
        self.destroy_monster(spawnIds=[1503])
        self.destroy_monster(spawnIds=[1504])
        self.destroy_monster(spawnIds=[1505])
        self.destroy_monster(spawnIds=[1506])
        self.destroy_monster(spawnIds=[1507])
        self.destroy_monster(spawnIds=[1508])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


initial_state = 시작
