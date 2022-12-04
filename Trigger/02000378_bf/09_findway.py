""" trigger/02000378_bf/09_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4029], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3009], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3109], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3009], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3109], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5209], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal(self.ctx)


# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4029], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_user_value(triggerId=1309, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2309, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[2009], animationEffect=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=109, script='$02000378_BF__09_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round09_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[109])


class Round09_Start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1009], animationEffect=False) # 수호대상 틴차이
        self.set_conversation(type=1, spawnId=1009, script='$02000378_BF__09_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=909, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='09RoundSuccess', value=1):
            return Round09_Sucess(self.ctx)


class Round09_Sucess(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2009, patrolName='MS2PatrolData_2009')
        self.destroy_monster(spawnIds=[1009])
        self.create_monster(spawnIds=[109], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3009], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3109], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3009], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3109], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5209], visible=True) # Sound_CrystalOn
        self.set_conversation(type=1, spawnId=109, script='$02000378_BF__09_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round09_RouteSelect(self.ctx)


class Round09_RouteSelect(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2009])
        self.create_monster(spawnIds=[209], animationEffect=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round09_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round09_PickRoute_Right(self.ctx)


class Round09_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1309, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2309, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal15(self.ctx)


class GoToPortal15(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=109, patrolName='MS2PatrolData_15')
        self.move_npc(spawnId=209, patrolName='MS2PatrolData_25')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Round09_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1309, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2309, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal16(self.ctx)


class GoToPortal16(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=12, key='FindWay', value=1)
        self.move_npc(spawnId=109, patrolName='MS2PatrolData_16')
        self.move_npc(spawnId=209, patrolName='MS2PatrolData_26')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[109,209])


initial_state = Wait
