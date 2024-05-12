""" trigger/02000378_bf/03_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=25, visible=False, enable=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
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
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4023], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.create_monster(spawnIds=[904,905,906], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_203')
        self.set_conversation(type=1, spawnId=201, script='$02000378_BF__03_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1303, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2303, key='RouteSelected', value=1)
        self.set_conversation(type=1, spawnId=201, script='$02000378_BF__03_FINDWAY__1$', arg4=2, arg5=1) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=101, script='$02000378_BF__03_FINDWAY__2$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round03_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[101,201])


class Round03_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1003], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2003], animationEffect=False) # 전투용 준타
        self.set_conversation(type=1, spawnId=1003, script='$02000378_BF__03_FINDWAY__3$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=903, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='03RoundSuccess', value=1):
            return Round03_Sucess02(self.ctx)


# 20170223 업데이트 던전 개편 단축 			
#     <state name="Round03_Sucess01" >	
#         <onEnter>				
# 				</onEnter>		
# 			<condition name="NPC를감지했으면" arg1="9003" arg2="2203">	
# 			<transition state="Round03_Sucess02"/>	
# 		</condition> 		
#     <onExit> 
#     </onExit>	
#     </state>
class Round03_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawnId=2203, patrolName='MS2PatrolData_2003')
        self.move_npc(spawnId=2003, patrolName='MS2PatrolData_2003')
        self.destroy_monster(spawnIds=[1003])
        self.create_monster(spawnIds=[103], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3003], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        # <action name="메쉬를설정한다" arg1="3103" arg2="1" arg3="0" arg4="0" arg5="0" />  CrystalOn
        self.set_mesh_animation(triggerIds=[3003], visible=False, arg3=0, arg4=0) # CrystalOff
        # <action name="메쉬애니를설정한다" arg1="3103" arg2="1" arg3="0" arg4="0" />  CrystalOn
        self.set_effect(triggerIds=[5203], visible=True) # Sound_CrystalOn
        self.set_portal(portalId=25, visible=True, enable=True, minimapVisible=False)
        self.set_conversation(type=1, spawnId=103, script='$02000378_BF__03_FINDWAY__4$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round03_RouteSelect(self.ctx)


class Round03_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawnIds=[2203])
        self.destroy_monster(spawnIds=[2003])
        self.create_monster(spawnIds=[203], animationEffect=False) # 연출용 준타
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_103New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(rate=50):
            return None # Missing State: Round03_PickRoute_Left
        """
        """
        if self.random_condition(rate=50):
            return None # Missing State: Round03_PickRoute_Right
        """
        if self.wait_tick(waitTick=500):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[103])
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_203New')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[203])
        self.destroy_monster(spawnIds=[904,905,906])


initial_state = Wait
