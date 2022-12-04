""" trigger/02000347_bf/main.xml """
import trigger_api


# 플레이어 감지
class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[9001], visible=False, animationEffect=False, animationDelay=0) # 사다리 가려
        self.set_ladder(triggerIds=[9002], visible=False, animationEffect=False, animationDelay=0) # 사다리 가려
        self.set_ladder(triggerIds=[9003], visible=False, animationEffect=False, animationDelay=0) # 사다리 가려
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        self.set_interact_object(triggerIds=[10000787], state=0) # 보상 상태 (없음)
        self.set_mesh(triggerIds=[6001,6011], visible=True) # 벽 생성
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], visible=False) # 길 차단

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=60001, boxId=1):
            return 오브젝티브_01(self.ctx)


class 오브젝티브_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 오브젝티브_02(self.ctx)


class 오브젝티브_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001,8002], returnView=True)
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[101], animationEffect=True) # 보스 등장
        self.set_cinematic_ui(type=3, script='$02000347_BF__MAIN1__0$') # 오브젝티브
        self.set_timer(timerId='5', seconds=5, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 시작_01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 플레이어 감지하면 1초 대기
class 시작_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_count_ui(text='$02000347_BF__MAIN1__2$', stage=0, count=3)
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 시작_02(self.ctx)


class 시작_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[9001], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        self.set_ladder(triggerIds=[9002], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        self.set_ladder(triggerIds=[9003], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 클리어(self.ctx)


class 클리어(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (on)
        self.set_event_ui(type=7, arg2='$02000347_BF__MAIN1__1$', arg3='3000')
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], visible=True, delay=0, scale=10) # 길 생성
        self.set_mesh(triggerIds=[6011], visible=False, delay=0, scale=0) # 벽 삭제
        self.set_interact_object(triggerIds=[10000787], state=1) # 보상 상태 (없음)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 클리어_02(self.ctx)


class 클리어_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=110, textId=40009) # 포탈 이용하세요


initial_state = 대기
