""" trigger/02000350_bf/timeattack_r8_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=140, spawnIds=[108099]):
            return 몹스폰(self.ctx)


class 몹스폰(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[108005], score=8000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[108099]):
            self.destroy_monster(spawnIds=[108005])
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[108005]):
            return 몹스폰(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
