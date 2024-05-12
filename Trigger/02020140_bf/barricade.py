""" trigger/02020140_bf/barricade.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 칸막이대기시작(self.ctx)


class 칸막이대기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_mesh(triggerIds=[608], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[609], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 칸막이대기알림(self.ctx)


class 칸막이대기알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020140_BF__BARRICADE__0$', arg3='3000')
        self.dungeon_enable_give_up(isEnable='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_time_out():
            # 던전 시간 다 된경우
            return 던전실패종료(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            # 던전을 포기해서 실패한 경우
            return 던전실패종료(self.ctx)
        if self.wait_tick(waitTick=30000):
            return 칸막이막기(self.ctx)


class 칸막이막기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[605], visible=True)
        self.set_mesh(triggerIds=[608], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[609], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_time_out():
            # 던전 시간 다 된경우
            return 던전실패종료(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            # 던전을 포기해서 실패한 경우
            return 던전실패종료(self.ctx)


class 던전실패종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전실패로 던전 종료되면 시작지점 막은거 다시 풀기
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_mesh(triggerIds=[608], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[609], visible=False, arg3=0, delay=0, scale=0)


initial_state = 시작대기중
