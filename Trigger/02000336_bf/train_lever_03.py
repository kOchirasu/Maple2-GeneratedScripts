""" trigger/02000336_bf/train_lever_03.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8161,8162,8163,8164], visible=False) # 안보이는 상태
        self.set_interact_object(triggerIds=[10000898], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000898], stateValue=0):
            return 작동_01(self.ctx)
        if self.count_users(boxId=709, boxId=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=113, textId=20003363, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000898], stateValue=0):
            return 작동_01(self.ctx)


class 작동_01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8161,8162,8163,8164], visible=True, delay=300, scale=10) # 파란 선으로
        self.set_mesh(triggerIds=[8261,8262,8263,8264], visible=False, delay=300, scale=10) # 빨간 선이
        self.set_effect(triggerIds=[7012], visible=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 작동_02(self.ctx)


class 작동_02(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(triggerIds=[8064,8065,8066,8067,8068], visible=False, delay=0, scale=10) # 벽은 사라지고
        self.set_skill(triggerIds=[5808], enable=True) # 벽 날리는 스킬
        self.set_mesh(triggerIds=[8069], visible=False, delay=30, scale=0) # 드럼통 폭발
        self.set_mesh(triggerIds=[8161,8162,8163,8164], visible=False, delay=0, scale=10) # 파란 선도 마저 삭제


initial_state = 대기
