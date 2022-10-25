""" trigger/02000294_bf/main2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[10001])
        self.destroy_monster(spawnIds=[10002])
        self.destroy_monster(spawnIds=[10003])
        self.destroy_monster(spawnIds=[10004])

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Battle_01', value=1):
            return 트리거01진행(self.ctx)


class 트리거01진행(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10001], animationEffect=False)
        self.create_monster(spawnIds=[10002], animationEffect=False)
        self.create_monster(spawnIds=[10003], animationEffect=False)
        self.create_monster(spawnIds=[10004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리거02시작(self.ctx)


class 트리거02시작(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=10001, patrolName='MS2PatrolData0')
        self.move_npc(spawnId=10002, patrolName='MS2PatrolData1')
        self.move_npc(spawnId=10003, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=10004, patrolName='MS2PatrolData3')


initial_state = 대기
