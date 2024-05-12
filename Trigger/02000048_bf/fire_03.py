""" trigger/02000048_bf/fire_03.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000308], state=1)
        self.set_mesh(trigger_ids=[203], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[303], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000308], state=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[203], visible=True, start_delay=0, interval=0, fade=1)
        self.set_effect(trigger_ids=[303], visible=True)
        self.spawn_monster(spawn_ids=[403], auto_target=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawn_id=403, patrol_name='MS2PatrolData_403')
        self.set_dialogue(type=1, spawn_id=403, script='$02000048_BF__FIRE_03__0$', time=2)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몬스터와전투(self.ctx)


class 몬스터와전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[403]):
            return 딜레이(self.ctx)
        if not self.monster_in_combat(spawn_ids=[403]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[403]):
            self.reset_timer(timer_id='1')
        if self.monster_dead(spawn_ids=[403]):
            return 소멸대기(self.ctx)
        if self.time_expired(timer_id='1'):
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 딜레이(self.ctx)
        if self.monster_in_combat(spawn_ids=[403]):
            return 몬스터소멸(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[403])
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
