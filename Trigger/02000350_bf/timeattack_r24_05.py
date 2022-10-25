""" trigger/02000350_bf/timeattack_r24_05.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=140, spawnIds=[124099]):
            return 몹스폰(self.ctx)


class 몹스폰(common.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[124005], score=32000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[124099]):
            self.destroy_monster(spawnIds=[124005])
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[124005]):
            return 몹스폰(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
