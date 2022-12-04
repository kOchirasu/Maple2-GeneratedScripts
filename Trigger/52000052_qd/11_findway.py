""" trigger/52000052_qd/11_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4031], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3011], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3111], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3011], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3111], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5211], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn01(self.ctx)


# 왼쪽에서 진입
class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4031], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.move_npc(spawnId=108, patrolName='MS2PatrolData_111')
        self.move_npc(spawnId=208, patrolName='MS2PatrolData_211')
        self.set_conversation(type=1, spawnId=208, script='$52000052_QD__04_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1311, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2311, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=108, script='$52000052_QD__04_FINDWAY__1$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round11_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[108,208])


class Round11_Start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1011], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2011], animationEffect=False) # 전투용 준타
        self.set_conversation(type=1, spawnId=1011, script='$52000052_QD__04_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=911, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='11RoundSuccess', value=1):
            return Round11_Sucess(self.ctx)


class Round11_Sucess(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2011, patrolName='MS2PatrolData_2011')
        self.destroy_monster(spawnIds=[1011])
        self.create_monster(spawnIds=[111], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3011], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3111], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3011], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3111], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5211], visible=True) # Sound_CrystalOn
        self.set_conversation(type=1, spawnId=111, script='$52000052_QD__04_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Round11_RouteSelect(self.ctx)


class Round11_RouteSelect(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2011])
        self.create_monster(spawnIds=[211], animationEffect=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round11_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round11_PickRoute_Right(self.ctx)


class Round11_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1311, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2311, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal19(self.ctx)


class GoToPortal19(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_19')
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_29')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Round11_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1311, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2311, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal10(self.ctx)


class GoToPortal10(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=12, key='FindWay', value=1)
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_10')
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_20')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[111,211])


initial_state = Wait
