""" trigger/02000420_bf/message.xml """
import common


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Message', value=1):
            return 메시지출력01(self.ctx)


class 메시지출력01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20042001, textId=20042001) # "파풀라투스의 보호막은 태엽 폭탄을 던져 제거해야 합니다." 메시지 출력

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 메시지출력02대기(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20042001)


class 메시지출력02대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Message', value=2):
            return 메시지출력02(self.ctx)


class 메시지출력02(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20042002, textId=20042002) # "연산 큐브를 밟아서 보호막 유지 시간을 조절해야 합니다." 메시지 출력

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 메시지출력03대기(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20042002)


class 메시지출력03대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Message', value=3):
            return 메시지출력03(self.ctx)


class 메시지출력03(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20042003, textId=20042003) # "떨어지는 물체로 바닥 유리를 파괴하여 태엽 폭탄을 꺼내야 합니다."  메시지 출력

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20042003)


class 종료(common.Trigger):
    pass


initial_state = 전투시작
