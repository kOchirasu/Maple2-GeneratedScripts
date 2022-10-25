""" trigger/82000001_survival/201_boat.xml """
import common


# 맵 외곽 동선
class BoatPatrol(common.Trigger):
    def on_enter(self):
        self.npc_to_patrol_in_box(boxId=9501, npcId=11400001, spawnId='interactObject', patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return BoatPatrol(self.ctx)


initial_state = BoatPatrol
