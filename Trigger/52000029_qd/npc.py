""" trigger/52000029_qd/npc.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[2001]):
            self.destroy_monster(spawnIds=[2001])
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
