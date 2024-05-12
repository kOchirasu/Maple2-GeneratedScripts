""" trigger/02010086_bf/train_open_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000897], state=0)
        self.set_effect(triggerIds=[7003], visible=False) # 전원 붙는 소리
        self.set_effect(triggerIds=[7004], visible=False) # 전원 붙는 소리
        self.set_mesh(triggerIds=[1161,1162,1163], visible=False) # 파랑 안보이는 상태

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000897], stateValue=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        # [b:레버]를 조작하여 드럼통을 폭파시키세요.
        self.show_guide_summary(entityId=113, textId=20003363)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000897], stateValue=0):
            return 작동_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=113)


class 작동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7003], visible=True) # 전원 붙는 소리
        self.set_effect(triggerIds=[7004], visible=True) # 전원 붙는 소리
        self.set_mesh(triggerIds=[1171,1172,1173], visible=False, delay=300, scale=10) # 빨간 선이
        self.set_mesh(triggerIds=[1161,1162,1163], visible=True, delay=300, scale=10) # 파란 선으로
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2111], visible=False, delay=30, scale=0) # 드럼통 폭발
        self.set_mesh(triggerIds=[1161,1162,1163], visible=False, delay=0, scale=10) # 파란 선도 마저 삭제
        self.set_mesh(triggerIds=[2101], visible=False, delay=50, scale=1) # 유리창 해제
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 벽제거(self.ctx)


class 벽제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (켬)


initial_state = 대기
