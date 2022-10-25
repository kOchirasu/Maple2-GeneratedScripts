""" trigger/02000378_bf/02_findway.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=24, visible=False, enable=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
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
        self.create_monster(spawnIds=[901,902,903], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        self.set_conversation(type=1, spawnId=201, script='$02000378_BF__02_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1302, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2302, key='RouteSelected', value=1)
        self.set_conversation(type=1, spawnId=201, script='$02000378_BF__02_FINDWAY__1$', arg4=2, arg5=1) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000378_BF__02_FINDWAY__2$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round02_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[101,201])


class Round02_Start(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1002], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2002], animationEffect=False) # 전투용 준타
        self.set_conversation(type=1, spawnId=1002, script='$02000378_BF__02_FINDWAY__3$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=902, key='MobWaveStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='02RoundSuccess', value=1):
            return Round02_Sucess02(self.ctx)


class Round02_Sucess02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002')
        self.destroy_monster(spawnIds=[1002])
        self.create_monster(spawnIds=[102], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3002], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3002], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_effect(triggerIds=[5202], visible=True) # Sound_CrystalOn
        self.set_portal(portalId=24, visible=True, enable=True, minimapVisible=False)
        self.set_conversation(type=1, spawnId=102, script='$02000378_BF__02_FINDWAY__4$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round02_RouteSelect(self.ctx)


class Round02_RouteSelect(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2002])
        self.create_monster(spawnIds=[202], animationEffect=False) # 연출용 준타
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_102New')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound12(self.ctx)
        """
        <condition name="랜덤조건" arg1="50">    
                    <transition state="Round02_PickRoute_Left"/>    
                </condition> 
                <condition name="랜덤조건" arg1="50"> 
                    <transition state="Round02_PickRoute_Right" />
                </condition>
        """


class GoToRound12(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_202New')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit02(self.ctx)


class Quit02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[901,902,903])


initial_state = Wait
