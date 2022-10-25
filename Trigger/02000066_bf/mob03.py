""" trigger/02000066_bf/mob03.xml """
import common


# 디펜스 모드 :  엘리트
class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
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


class 차타이머2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='80', seconds=80)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[901]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='80'):
            return 생성랜덤(self.ctx)


class 차타이머3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='75', seconds=75)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='75'):
            return 생성랜덤(self.ctx)


class 차타이머4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='68', seconds=68)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[904]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='68'):
            return 생성랜덤(self.ctx)


class 차타이머5(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='63', seconds=63)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[905]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='63'):
            return 생성랜덤(self.ctx)


class 차타이머6(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='58', seconds=58)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='58'):
            return 생성랜덤(self.ctx)


class 차타이머7(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='68', seconds=68)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='68'):
            return 생성랜덤(self.ctx)


class 차타이머8(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='62', seconds=62)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[909]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='62'):
            return 생성랜덤(self.ctx)


class 차타이머9(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='60'):
            return 생성랜덤(self.ctx)


class 차타이머10(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='55', seconds=55)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='55'):
            return 생성랜덤(self.ctx)


class 차타이머11(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='52', seconds=52)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[913]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='52'):
            return 생성랜덤(self.ctx)


class 차타이머12(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='49', seconds=49)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='49'):
            return 생성랜덤(self.ctx)


class 생성랜덤(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=12):
            return 번생성1(self.ctx)
        if self.random_condition(rate=13):
            return 번생성2(self.ctx)
        if self.random_condition(rate=12):
            return 번생성3(self.ctx)
        if self.random_condition(rate=13):
            return 번생성4(self.ctx)
        if self.random_condition(rate=12):
            return 번생성5(self.ctx)
        if self.random_condition(rate=13):
            return 번생성6(self.ctx)
        if self.random_condition(rate=12):
            return 번생성7(self.ctx)
        if self.random_condition(rate=13):
            return 번생성8(self.ctx)


class 번생성1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1201], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성4(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1204], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성5(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1205], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성6(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1206], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성7(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1207], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성8(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1208], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1201])
        self.destroy_monster(spawnIds=[1202])
        self.destroy_monster(spawnIds=[1203])
        self.destroy_monster(spawnIds=[1204])
        self.destroy_monster(spawnIds=[1205])
        self.destroy_monster(spawnIds=[1206])
        self.destroy_monster(spawnIds=[1207])
        self.destroy_monster(spawnIds=[1208])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


initial_state = 대기시간
