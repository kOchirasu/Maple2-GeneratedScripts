""" trigger/02000066_bf/mob04.xml """
import common


# 디펜스 모드 :  원거리
class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[900]):
            return 차타이머1(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[902]): # 33레벨
            return 차타이머3(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[904]):
            return 차타이머4(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[906]): # 35레벨
            return 차타이머6(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[908]):
            return 차타이머7(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[910]): # 35레벨 하드
            return 차타이머9(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[912]):
            return 차타이머10(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[914]):
            return 차타이머12(self.ctx)


class 차타이머1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='25', seconds=25)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[900]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='25'):
            return 생성랜덤(self.ctx)


class 차타이머3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='23', seconds=23)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='23'):
            return 생성랜덤(self.ctx)


class 차타이머4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='21', seconds=21)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[904]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='21'):
            return 생성랜덤(self.ctx)


class 차타이머6(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='19', seconds=19)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='19'):
            return 생성랜덤(self.ctx)


class 차타이머7(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='20'):
            return 생성랜덤(self.ctx)


class 차타이머9(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='18', seconds=18)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='18'):
            return 생성랜덤(self.ctx)


class 차타이머10(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='16', seconds=16)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='16'):
            return 생성랜덤(self.ctx)


class 차타이머12(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='14', seconds=14)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='14'):
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
        self.create_monster(spawnIds=[1301], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1302], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1303], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성4(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1304], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성5(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1305], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성6(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1306], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성7(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1307], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성8(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1308], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1301])
        self.destroy_monster(spawnIds=[1302])
        self.destroy_monster(spawnIds=[1303])
        self.destroy_monster(spawnIds=[1304])
        self.destroy_monster(spawnIds=[1305])
        self.destroy_monster(spawnIds=[1306])
        self.destroy_monster(spawnIds=[1307])
        self.destroy_monster(spawnIds=[1308])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


initial_state = 대기시간
