""" trigger/02000350_bf/timeattack_r24_06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=140, spawnIds=[124099]):
            return 몹스폰(self.ctx)


class 몹스폰(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[124006], score=32000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[124099]):
            self.destroy_monster(spawnIds=[124006])
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[124006]):
            return 몹스폰(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
