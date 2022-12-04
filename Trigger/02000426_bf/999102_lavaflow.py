""" trigger/02000426_bf/999102_lavaflow.xml """
import trigger_api


class 전투체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LavaflowHigh', value=1):
            self.set_user_value(triggerId=999102, key='LavaflowHigh', value=0)
            return 칸이동3(self.ctx)
        if self.user_value(key='LavaflowLow', value=1):
            self.set_user_value(triggerId=999102, key='LavaflowLow', value=0)
            return 칸이동2(self.ctx)
        if self.user_value(key='BattleEnd2', value=1):
            return 종료(self.ctx)


class 칸이동3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=28000):
            return 리턴(self.ctx)
        if self.user_value(key='BattleEnd2', value=1):
            return 종료(self.ctx)


class 칸이동2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=25000):
            return 리턴(self.ctx)
        if self.user_value(key='BattleEnd2', value=1):
            return 종료(self.ctx)


class 리턴(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.destroy_monster(spawnIds=[1001])
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001])


initial_state = 전투체크
