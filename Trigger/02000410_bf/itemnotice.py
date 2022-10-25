""" trigger/02000410_bf/itemnotice.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 전투시작(self.ctx)


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ItemNotice01', value=1):
            return 필수아이템01(self.ctx)


class 필수아이템01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20041008, textId=20041008) # 부활불가 되었고 이제 파티가 전멸되면 게임오버 된다는 내여을 시스템메시지를 통해서 알려줌, 참고로 파티원전멸 체크 트리거는 ClearCheck.xml 이것임

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 다음대기(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20041008)


class 다음대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ItemNotice02', value=1):
            return 필수아이템02(self.ctx)


class 필수아이템02(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20041009, textId=20041009) # 부활불가 되었고 이제 파티가 전멸되면 게임오버 된다는 내여을 시스템메시지를 통해서 알려줌, 참고로 파티원전멸 체크 트리거는 ClearCheck.xml 이것임

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20041009)


class 종료(common.Trigger):
    pass


initial_state = Ready
