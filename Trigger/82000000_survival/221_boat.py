""" trigger/82000000_survival/221_boat.xml """
import trigger_api


# 맵 외곽 동선
class BoatPatrol(trigger_api.Trigger):
    def on_enter(self):
        self.npc_to_patrol_in_box(boxId=9521, npcId=11400001, spawnId='interactObject', patrolName='MS2PatrolData_221')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return BoatPatrol(self.ctx)


initial_state = BoatPatrol
