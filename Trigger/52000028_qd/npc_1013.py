""" trigger/52000028_qd/npc_1013.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[1013]):
            self.destroy_monster(spawnIds=[1013])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
