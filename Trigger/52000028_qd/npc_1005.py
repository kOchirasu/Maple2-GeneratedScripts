""" trigger/52000028_qd/npc_1005.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[1005]):
            self.destroy_monster(spawnIds=[1005])
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
