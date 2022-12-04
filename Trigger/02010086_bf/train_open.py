""" trigger/02010086_bf/train_open.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=False) # 전원 붙는 소리
        self.set_effect(triggerIds=[7002], visible=False) # 전원 붙는 소리
        self.set_mesh(triggerIds=[1061,1062,1063], visible=False) # 안보이는 상태
        self.set_mesh(triggerIds=[2011,2012,2013], visible=False) # 안보이는 상태
        self.set_interact_object(triggerIds=[10000896], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000896], stateValue=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=113, textId=20003363) # [b:레버]를 조작하여 드럼통을 폭파시키세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000896], stateValue=0):
            return 작동_01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=113)


class 작동_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=True) # 전원 붙는 소리
        self.set_effect(triggerIds=[7002], visible=True) # 전원 붙는 소리
        self.set_mesh(triggerIds=[1071,1072,1073], visible=False, delay=300, scale=10) # 빨간 선이
        self.set_mesh(triggerIds=[1061,1062,1063], visible=True, delay=300, scale=10) # 파란 선으로
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1055], visible=False, delay=30, scale=0) # 드럼통 폭발
        self.set_mesh(triggerIds=[1061,1062,1063], visible=False, delay=0, scale=10) # 파란 선도 마저 삭제
        self.set_mesh(triggerIds=[1005], visible=False, delay=50, scale=1) # 유리창 해제
        self.set_actor(triggerId=1022, visible=True, initialSequence='Opened') # 문 열림
        self.set_mesh(triggerIds=[1021], visible=False, delay=0, scale=10) # 벽 해제
        self.set_timer(timerId='1', seconds=1)


initial_state = 대기
