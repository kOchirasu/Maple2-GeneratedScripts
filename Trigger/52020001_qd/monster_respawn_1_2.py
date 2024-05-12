""" trigger/52020001_qd/monster_respawn_1_2.xml """
import trigger_api


class 체력조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=70, spawn_id=6000018, is_relative=True):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[6000022], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = 체력조건
