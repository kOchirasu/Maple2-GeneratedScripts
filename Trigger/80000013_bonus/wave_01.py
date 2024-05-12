""" trigger/80000013_bonus/wave_01.xml """
import trigger_api


# 플레이어 감지
class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[199]):
            return 생성랜덤(self.ctx)
        return 차타이머1(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1) # 임시

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 차타이머1(self.ctx)
        if self.npc_detected(box_id=702, spawn_ids=[199]):
            return 차타이머1(self.ctx)


class 차타이머1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if not self.npc_detected(box_id=702, spawn_ids=[199]):
            return 시작(self.ctx)
        """
        if self.time_expired(timer_id='3'):
            return 생성랜덤(self.ctx)


# 몬스터 랜덤 생성
class 생성랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=3):
            return 번생성1(self.ctx)
        if self.random_condition(weight=3):
            return 번생성2(self.ctx)
        if self.random_condition(weight=3):
            return 번생성3(self.ctx)
        if self.random_condition(weight=3):
            return 번생성4(self.ctx)
        if self.random_condition(weight=3):
            return 번생성5(self.ctx)
        if self.random_condition(weight=3):
            return 번생성6(self.ctx)
        if self.random_condition(weight=3):
            return 번생성7(self.ctx)
        if self.random_condition(weight=3):
            return 번생성8(self.ctx)
        if self.random_condition(weight=3):
            return 번생성9(self.ctx)


class 번생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[106], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[107], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[108], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 번생성9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


initial_state = 시작
