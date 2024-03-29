""" trigger/02000334_bf/guide.xml """
import trigger_api


# 플레이어 감지
class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=90099, spawnIds=[150]):
            return 차타이머1(self.ctx)


class 차타이머1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 가이드_01(self.ctx)


class 가이드_01(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=101, textId=20000010) # 폭탄을 던지세요
        self.set_effect(triggerIds=[90021], visible=True) # 이벤트 UI 에 맞는 사운드
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=90001, spawnIds=[301]):
            return 차타이머2(self.ctx)
        if self.time_expired(timerId='5'):
            return 가이드_01_02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=101) # 폭탄을 던지세요


class 가이드_01_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=90001, spawnIds=[301]):
            return 차타이머2(self.ctx)


class 차타이머2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 가이드_02(self.ctx)


class 가이드_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[90100]):
            return 오스칼_배웅(self.ctx)
        if self.monster_dead(boxIds=[190]):
            return 가이드_02_02(self.ctx)


class 가이드_02_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[90100]):
            return 오스칼_배웅(self.ctx)


class 오스칼_배웅(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=199, patrolName='MS2PatrolData_2016') # 오스칼 플레이어를 쳐다봄...


initial_state = 대기시간
