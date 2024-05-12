""" trigger/02000336_bf/train_lever_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False) # 안보이는 상태
        self.set_interact_object(triggerIds=[10000896], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000896], stateValue=0):
            return 작동_01(self.ctx)
        if self.count_users(boxId=708, minUsers='1'):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=113, textId=20003363, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000896], stateValue=0):
            return 작동_01(self.ctx)


class 작동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, delay=300, scale=10) # 빨간 선이
        self.set_mesh(triggerIds=[8101,8102,8103,8104], visible=False, delay=300, scale=10) # 파란 선으로
        self.set_effect(triggerIds=[7010], visible=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(triggerIds=[8050,8051,8052,8053,8054], visible=False, delay=0, scale=10) # 벽은 사라지고
        self.set_skill(triggerIds=[5806], enable=True) # 벽 날리는 스킬
        self.set_mesh(triggerIds=[8055], visible=False, delay=30, scale=0) # 드럼통 폭발
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, delay=0, scale=10) # 파란 선도 마저 삭제


initial_state = 대기
