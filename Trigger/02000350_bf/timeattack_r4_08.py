""" trigger/02000350_bf/timeattack_r4_08.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=140, spawnIds=[104099]):
            return 몹스폰(self.ctx)


class 몹스폰(common.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[104008], score=4100)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[104099]):
            self.destroy_monster(spawnIds=[104008])
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[104008]):
            return 몹스폰(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
