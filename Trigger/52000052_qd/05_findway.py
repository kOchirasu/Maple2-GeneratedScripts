""" trigger/52000052_qd/05_findway.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4025], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3005], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3105], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3005], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3105], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5205], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn01(self.ctx)


# 왼쪽에서 진입
class ReadyToWalkIn01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4025], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_105')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_205')
        self.set_conversation(type=1, spawnId=204, script='$52000052_QD__04_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1305, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2305, key='RouteSelected', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=104, script='$52000052_QD__04_FINDWAY__1$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round05_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[104,204])


class Round05_Start(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1005], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2005], animationEffect=False) # 전투용 준타
        self.set_conversation(type=1, spawnId=1005, script='$52000052_QD__04_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=905, key='MobWaveStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='05RoundSuccess', value=1):
            return Round05_Sucess(self.ctx)


class Round05_Sucess(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2005, patrolName='MS2PatrolData_2005')
        self.destroy_monster(spawnIds=[1005])
        self.create_monster(spawnIds=[105], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3005], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3105], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3005], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3105], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5205], visible=True) # Sound_CrystalOn
        self.set_conversation(type=1, spawnId=105, script='$52000052_QD__04_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round05_RouteSelect(self.ctx)


class Round05_RouteSelect(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2005])
        self.create_monster(spawnIds=[205], animationEffect=False) # 연출용 준타

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            return Round05_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round05_PickRoute_Right(self.ctx)


class Round05_PickRoute_Left(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1305, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2305, key='MakeFalse', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal11(self.ctx)


class GoToPortal11(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_11')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_21')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Round05_PickRoute_Right(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1305, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2305, key='MakeTrue', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal12(self.ctx)


class GoToPortal12(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=12, key='FindWay', value=1)
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_12')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_22')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[105,205])


initial_state = Wait
