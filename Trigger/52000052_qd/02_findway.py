""" trigger/52000052_qd/02_findway.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4022], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3102], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3002], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3102], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5202], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn01(self.ctx)


class ReadyToWalkIn01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4022], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        self.set_conversation(type=1, spawnId=201, script='$52000052_QD__02_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1302, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2302, key='RouteSelected', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$52000052_QD__02_FINDWAY__2$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round02_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[101,201])


class Round02_Start(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1002], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2002], animationEffect=False) # 전투용 준타
        self.set_conversation(type=1, spawnId=1002, script='$52000052_QD__02_FINDWAY__3$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=902, key='MobWaveStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='02RoundSuccess', value=1):
            return Round02_Sucess01(self.ctx)


class Round02_Sucess01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9002, spawnIds=[2202]):
            return Round02_Sucess02(self.ctx)


class Round02_Sucess02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2202, patrolName='MS2PatrolData_2002')
        self.destroy_monster(spawnIds=[1002])
        self.create_monster(spawnIds=[102], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3002], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3102], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3002], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3102], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5202], visible=True) # Sound_CrystalOn
        self.set_conversation(type=1, spawnId=102, script='$52000052_QD__02_FINDWAY__4$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round02_RouteSelect(self.ctx)


class Round02_RouteSelect(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2202])
        self.create_monster(spawnIds=[202], animationEffect=False) # 연출용 준타

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            return Round02_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round02_PickRoute_Right(self.ctx)


class Round02_PickRoute_Left(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1302, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2302, key='MakeFalse', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound04(self.ctx)


class GoToRound04(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='FindWayLeft', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Round02_PickRoute_Right(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1302, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2302, key='MakeTrue', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound07(self.ctx)


class GoToRound07(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7, key='FindWay', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
