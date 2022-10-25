""" trigger/02000551_bf/startportal.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False) # 최초 입구에 있는 전투판으로 가는  포탈 최초에는 감추기
        self.set_effect(triggerIds=[8101,8102,8103,8104,8105], visible=False) # 최초 시작 지점에 나오는 화살표 표시 끄기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 포탈활성화(self.ctx)


class 포탈활성화(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True) # 최초 입구에 있는 전투판으로 가는  포탈 활성화
        self.dungeon_enable_give_up(isEnable='1')
        self.set_event_ui(type=1, arg2='$02020140_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.dungeon_time_out():
            return 던전실패종료(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패종료(self.ctx)
        if self.wait_tick(waitTick=30000):
            return 포탈감추기(self.ctx)


class 포탈감추기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False) # 전투판으로 가는  포탈  감추기

    def on_tick(self) -> common.Trigger:
        if self.dungeon_time_out():
            return 던전실패종료(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패종료(self.ctx)


class 던전실패종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True) # 최초 입구에 있는 전투판으로 가는  포탈 활성화


initial_state = 시작대기중
