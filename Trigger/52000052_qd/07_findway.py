""" trigger/52000052_qd/07_findway.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=22, visible=False, enable=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(triggerIds=[4027], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3007], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3107], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3007], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3107], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5207], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn01(self.ctx)


class ReadyToWalkIn01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4027], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_107')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_207')
        self.set_conversation(type=1, spawnId=202, script='$52000052_QD__04_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1307, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2307, key='RouteSelected', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000052_QD__04_FINDWAY__1$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round07_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[102,202])


class Round07_Start(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1007], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2007], animationEffect=False) # 전투용 준타
        self.set_conversation(type=1, spawnId=1007, script='$52000052_QD__04_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=907, key='MobWaveStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='07RoundSuccess', value=1):
            return Round07_Sucess02(self.ctx)


class Round07_Sucess02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2007, patrolName='MS2PatrolData_2007')
        # action name="NPC를이동시킨다" arg1="2207" arg2="MS2PatrolData_2007" /
        self.destroy_monster(spawnIds=[1007])
        self.create_monster(spawnIds=[107], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3007], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3007], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_effect(triggerIds=[5207], visible=True) # Sound_CrystalOn
        self.set_portal(portalId=22, visible=True, enable=True, minimapVisible=False)
        self.set_conversation(type=1, spawnId=107, script='$52000052_QD__04_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round07_RouteSelect(self.ctx)


class Round07_RouteSelect(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2007])
        self.create_monster(spawnIds=[207], animationEffect=False) # 연출용 준타
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_107New')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return GoToRound12(self.ctx)
        """
        <condition name="랜덤조건" arg1="50">    
                    <transition state="Round07_PickRoute_Left"/>    
                </condition> 
                <condition name="랜덤조건" arg1="50"> 
                    <transition state="Round07_PickRoute_Right" />
                </condition>
        """


class GoToRound12(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[107])
        self.move_npc(spawnId=207, patrolName='MS2PatrolData_207New')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[207])


# 20170223 업데이트 던전 개편 단축
class Round07_PickRoute_Left(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1307, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2307, key='MakeFalse', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound09(self.ctx)


class GoToRound09(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=9, key='FindWay', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Round07_PickRoute_Right(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1307, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2307, key='MakeTrue', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound10(self.ctx)


class GoToRound10(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=10, key='FindWayLeft', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
