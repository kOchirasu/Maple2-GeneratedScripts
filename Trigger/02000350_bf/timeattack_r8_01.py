""" trigger/02000350_bf/timeattack_r8_01.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=140, spawnIds=[108099]):
            return 몹스폰(self.ctx)


class 몹스폰(common.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[108001], score=8000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[108099]):
            self.destroy_monster(spawnIds=[108001])
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[108001]):
            return 몹스폰(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
