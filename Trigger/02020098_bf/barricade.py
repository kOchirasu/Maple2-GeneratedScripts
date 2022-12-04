""" trigger/02020098_bf/barricade.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311], visible=False, arg3=0, delay=0, scale=0) # 스타트포인트 지점의 칸막이 트리거메쉬 최초에는 감추기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10]):
            return 칸막이대기시작(self.ctx)


class 칸막이대기시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 칸막이대기알림(self.ctx)


class 칸막이대기알림(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020098_BF__BARRICADE__0$', arg3='3000')
        self.dungeon_enable_give_up(isEnable='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=22000):
            return 칸막이막기(self.ctx)


class 칸막이막기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311], visible=True, arg3=1, delay=120, scale=0.5) # 시작지점의 칸막이 막기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 트리거종료(self.ctx)


class 트리거종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
