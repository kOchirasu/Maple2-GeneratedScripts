""" trigger/03000145_bf/save_05.xml """
import trigger_api


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=1)
        self.set_mesh(trigger_ids=[5001], visible=False, fade=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000471], state=1)
        self.spawn_monster(spawn_ids=[501], auto_target=False)
        self.spawn_monster(spawn_ids=[502], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000471], state=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_mesh(trigger_ids=[5001], visible=True, fade=1)
        self.destroy_monster(spawn_ids=[501])
        self.destroy_monster(spawn_ids=[502])
        self.spawn_monster(spawn_ids=[511], auto_target=False)
        self.spawn_monster(spawn_ids=[512], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 도망갈준비1(self.ctx)


class 도망갈준비1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_dialogue(type=1, spawn_id=511, script='$03000145_BF__SAVE_05__0$', time=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 도망갈준비2(self.ctx)


class 도망갈준비2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=1, spawn_id=512, script='$03000145_BF__SAVE_05__1$', time=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 도망시작(self.ctx)


class 도망시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=511, patrol_name='MS2PatrolData_511')
        self.move_npc(spawn_id=512, patrol_name='MS2PatrolData_512')

    def on_tick(self) -> trigger_api.Trigger:
        return 도망중(self.ctx)


class 도망중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=4)
        self.set_dialogue(type=1, spawn_id=511, script='$03000145_BF__SAVE_05__2$', time=2, arg5=0)
        self.set_dialogue(type=1, spawn_id=512, script='$03000145_BF__SAVE_05__3$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 도망끝(self.ctx)


class 도망끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='7', seconds=10)
        self.destroy_monster(spawn_ids=[511])
        self.destroy_monster(spawn_ids=[512])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return 트리거초기화(self.ctx)


initial_state = 트리거초기화
