""" trigger/52000052_qd/03_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4023], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3103], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3003], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3103], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5203], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn01(self.ctx)


class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4023], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_203')
        self.set_conversation(type=1, spawnId=201, script='$52000052_QD__02_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1303, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2303, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$52000052_QD__02_FINDWAY__2$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round03_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[101,201])


class Round03_Start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1003], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2003], animationEffect=False) # 전투용 준타
        self.set_conversation(type=1, spawnId=1003, script='$52000052_QD__02_FINDWAY__3$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=903, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='03RoundSuccess', value=1):
            return Round03_Sucess01(self.ctx)


class Round03_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9003, spawnIds=[2203]):
            return Round03_Sucess02(self.ctx)


class Round03_Sucess02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2203, patrolName='MS2PatrolData_2003')
        self.destroy_monster(spawnIds=[1003])
        self.create_monster(spawnIds=[103], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3003], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3103], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3003], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3103], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5203], visible=True) # Sound_CrystalOn
        self.set_conversation(type=1, spawnId=103, script='$52000052_QD__02_FINDWAY__4$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round03_RouteSelect(self.ctx)


class Round03_RouteSelect(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2203])
        self.create_monster(spawnIds=[203], animationEffect=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round03_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round03_PickRoute_Right(self.ctx)


class Round03_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1303, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2303, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound04(self.ctx)


class GoToRound04(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='FindWayRight', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Round03_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1303, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2303, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound08(self.ctx)


class GoToRound08(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=8, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
