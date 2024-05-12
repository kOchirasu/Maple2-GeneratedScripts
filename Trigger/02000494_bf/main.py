""" trigger/02000494_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100,3200], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 전투01(self.ctx)
        if self.user_detected(box_ids=[1002]):
            return 전투01(self.ctx)


class 전투01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106,107], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105,106,107]):
            return 포털개방(self.ctx)


class 포털개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100,3200], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115], visible=True, start_delay=0, interval=100, fade=1)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True, start_delay=0, interval=100, fade=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
