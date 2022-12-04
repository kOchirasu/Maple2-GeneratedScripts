""" trigger/02000066_bf/mobgroup02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
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
        if self.user_detected(boxIds=[103]):
            return 대기시간(self.ctx)


# 디펜스 모드 :  해골모둠
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
        self.set_timer(timerId='45', seconds=45)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[900]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='45'):
            return 대기시간(self.ctx)


class 차타이머2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='22', seconds=22)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='22'):
            return 대기시간(self.ctx)


class 차타이머3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='40', seconds=40)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[902]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='40'):
            return 대기시간(self.ctx)


class 차타이머4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='33', seconds=33)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[904]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='33'):
            return 대기시간(self.ctx)


class 차타이머5(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='16', seconds=16)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[905]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='16'):
            return 대기시간(self.ctx)


class 차타이머6(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='28', seconds=28)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[906]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='28'):
            return 대기시간(self.ctx)


class 차타이머7(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='25', seconds=25)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[908]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='25'):
            return 대기시간(self.ctx)


class 차타이머8(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='13', seconds=13)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[909]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='13'):
            return 대기시간(self.ctx)


class 차타이머9(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='22', seconds=22)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[910]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='22'):
            return 대기시간(self.ctx)


class 차타이머10(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=20)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[912]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='20'):
            return 대기시간(self.ctx)


class 차타이머11(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[913]):
            return 대기시간(self.ctx)
        if self.time_expired(timerId='10'):
            return 대기시간(self.ctx)


class 차타이머12(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='16', seconds=16)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1104], animationEffect=False)
        self.create_monster(spawnIds=[1105], animationEffect=False)
        self.create_monster(spawnIds=[1106], animationEffect=False)
        self.create_monster(spawnIds=[1107], animationEffect=False)
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[914]):
            return 소멸(self.ctx)
        if self.time_expired(timerId='16'):
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


initial_state = 시작
