""" trigger/02000350_bf/timeattack_r4_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=140, spawnIds=[104099]):
            return 몹스폰(self.ctx)


class 몹스폰(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[104004], score=4100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[104099]):
            self.destroy_monster(spawnIds=[104004])
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[104004]):
            return 몹스폰(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
