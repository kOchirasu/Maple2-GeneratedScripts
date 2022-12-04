""" trigger/02000066_bf/mob02.xml """
import trigger_api


# 디펜스 모드 :  해골A
class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class 차타이머1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='12', seconds=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[900]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='12'):
            return 생성랜덤(self.ctx)


class 차타이머2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='10'):
            return 생성랜덤(self.ctx)


class 차타이머3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='9'):
            return 생성랜덤(self.ctx)


class 차타이머4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='8', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[904]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='8'):
            return 생성랜덤(self.ctx)


class 차타이머5(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[905]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='7'):
            return 생성랜덤(self.ctx)


class 차타이머6(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='6'):
            return 생성랜덤(self.ctx)


class 차타이머7(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='3'):
            return 생성랜덤(self.ctx)


class 차타이머8(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[909]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='3'):
            return 생성랜덤(self.ctx)


class 차타이머9(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='3'):
            return 생성랜덤(self.ctx)


class 차타이머10(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='3'):
            return 생성랜덤(self.ctx)


class 차타이머11(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[913]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='3'):
            return 생성랜덤(self.ctx)


class 차타이머12(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='3'):
            return 생성랜덤(self.ctx)


class 생성랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class 번생성1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1104], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성5(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1105], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성6(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1106], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성7(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1107], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성8(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1101])
        self.destroy_monster(spawnIds=[1102])
        self.destroy_monster(spawnIds=[1103])
        self.destroy_monster(spawnIds=[1104])
        self.destroy_monster(spawnIds=[1105])
        self.destroy_monster(spawnIds=[1106])
        self.destroy_monster(spawnIds=[1107])
        self.destroy_monster(spawnIds=[1108])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


initial_state = 대기시간
