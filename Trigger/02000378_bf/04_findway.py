""" trigger/02000378_bf/04_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(triggerIds=[4024], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3004], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3104], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3004], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3104], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5204], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal(self.ctx)


# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4024], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_user_value(triggerId=1304, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2304, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[2004], animationEffect=False) # 전투용 준타
        self.create_monster(spawnIds=[104], animationEffect=False)


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=104, script='$02000378_BF__04_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round04_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[104])


class Round04_Start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1004], animationEffect=False) # 수호대상 틴차이
        self.set_conversation(type=1, spawnId=1004, script='$02000378_BF__04_FINDWAY__4$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=904, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='04RoundSuccess', value=1):
            return Round04_Sucess02(self.ctx)


class Round04_Sucess02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2004, patrolName='MS2PatrolData_2004')
        self.destroy_monster(spawnIds=[1004])
        self.create_monster(spawnIds=[104], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3004], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3004], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_effect(triggerIds=[5204], visible=True) # Sound_CrystalOn
        self.set_portal(portalId=21, visible=True, enable=True, minimapVisible=False)
        self.set_conversation(type=1, spawnId=104, script='$02000378_BF__04_FINDWAY__5$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round04_RouteSelect(self.ctx)


class Round04_RouteSelect(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2004])
        self.create_monster(spawnIds=[204], animationEffect=False) # 연출용 준타
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_104New')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound12(self.ctx)
        """
        <condition name="랜덤조건" arg1="50">    
                    <transition state="Round04_PickRoute_Left"/>    
                </condition> 
                <condition name="랜덤조건" arg1="50"> 
                    <transition state="Round04_PickRoute_Right" />
                </condition>
        """


class GoToRound12(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204New')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[204])


initial_state = Wait
