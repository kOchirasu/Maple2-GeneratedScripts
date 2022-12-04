""" trigger/02000336_bf/train_open.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[16014,16015,16016], visible=False) # 안보이는 상태
        self.set_interact_object(triggerIds=[10000805], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=706, boxId=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=113, textId=20003363)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000805], stateValue=0):
            return 작동_01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=113)


class 작동_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[16011,16012,16013], visible=False, delay=300, scale=10) # 빨간 선이
        self.set_mesh(triggerIds=[16014,16015,16016], visible=True, delay=300, scale=10) # 파란 선으로
        self.set_effect(triggerIds=[7013], visible=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_skill(triggerIds=[5802], enable=True) # 벽 날리는 스킬
        self.set_mesh(triggerIds=[16001], visible=False, delay=30, scale=0) # 드럼통 폭발
        self.set_mesh(triggerIds=[16014,16015,16016], visible=False, delay=0, scale=10) # 파란 선도 마저 삭제
        self.set_mesh(triggerIds=[16000], visible=False, delay=50, scale=1) # 유리창 해제
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return 작동_03(self.ctx)


class 작동_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[305,306,307,308], animationEffect=False) # 기본 배치 될 몬스터 등장


initial_state = 대기
