""" trigger/84000004_wd/main.xml """
import common


class 시작_타이머설정(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4000', seconds=300, startDelay=1, interval=0) # 5분 타이머. 기념촬영장은 맥시멈 5분만 돌아가도록 한다. 포털을 사용할 수 없기 때문에 시간에 제한을 둔다.
        self.set_portal(portalId=10001, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 카메라세팅(self.ctx)


class 카메라세팅(common.Trigger):
    def on_enter(self):
        self.set_photo_studio(isEnable=True) # 자유각도변환 UI ON
        self.set_portal(portalId=10001, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 강제퇴장대기(self.ctx)


class 강제퇴장대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='exitstudio', value=1):
            return 강제퇴장준비(self.ctx)
        if self.time_expired(timerId='4000'):
            return 강퇴안내(self.ctx)


class 강퇴안내(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=28400138) # 가이드 메시지 : 잠시 후, 기념 촬영장이 폐쇄됩니다. 모두 퇴장해 주세요.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 강제퇴장준비(self.ctx)


class 강제퇴장준비(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=28400138) # 가이드 메시지 : 잠시 후, 기념 촬영장이 폐쇄됩니다. 모두 퇴장해 주세요.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 강제퇴장(self.ctx)


class 강제퇴장(common.Trigger):
    def on_enter(self):
        self.room_expire() # 방을 완전 폐쇄해버리는 명령어. 룸스테이지에서 제한시간이 다 되었을때의 처리와 같은 로직


initial_state = 시작_타이머설정
