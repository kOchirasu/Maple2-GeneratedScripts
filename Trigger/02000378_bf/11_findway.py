""" trigger/02000378_bf/11_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4031], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3011], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3111], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3011], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3111], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5211], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal(self.ctx)


# 왼쪽에서 진입 	
#     <state name="ReadyToWalkIn01" >	
#         <onEnter>		
# 			<action name="메쉬를설정한다" arg1="4031" arg2="0" arg3="0" arg4="0" arg5="0" /> 			
# 			<action name="NPC를이동시킨다" arg1="108" arg2="MS2PatrolData_111" />			
# 			<action name="NPC를이동시킨다" arg1="208" arg2="MS2PatrolData_211" />	
# 			<action name="대화를설정한다" arg1="1" arg2="208" arg3="$02000378_BF__11_FINDWAY__0$" arg4="2" arg5="0" />	  				
# 				</onEnter>	
# 				<condition name="WaitTick" waitTick="2000">  
# 					<transition state="ReadyToWalkIn02"/>  
# 				</condition>					
#     <onExit> 
#     </onExit>
#     </state>	
# 	
#     <state name="ReadyToWalkIn02" > 
#         <onEnter>			
# 			<action name="SetUserValue" triggerID="1311" key="RouteSelected" value="1" /> 		
# 			<action name="SetUserValue" triggerID="2311" key="RouteSelected" value="1" /> 						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="2000">  
# 					<transition state="ReadyToWalkIn03"/>
# 				</condition>		
#     <onExit> 
#     </onExit>
#     </state>		
# 
#     <state name="ReadyToWalkIn03" > 	
#         <onEnter>			
# 			<action name="대화를설정한다" arg1="1" arg2="108" arg3="$02000378_BF__11_FINDWAY__1$" arg4="2" arg5="2" />	    						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="5000">  
# 					<transition state="Round11_Start"/>
# 				</condition>		
#     <onExit> 
# 			<action name="몬스터소멸시킨다" arg1="108,208" />		
#     </onExit>
#     </state>
# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4031], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_user_value(triggerId=1311, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2311, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[2011], animationEffect=False)
        # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=111, script='$02000378_BF__11_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round11_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[111])


class Round11_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1011], animationEffect=False) # 수호대상 틴차이
        self.set_conversation(type=1, spawnId=1011, script='$02000378_BF__11_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=911, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='11RoundSuccess', value=1):
            return Round11_Sucess(self.ctx)


class Round11_Sucess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=2011, patrolName='MS2PatrolData_2011')
        self.destroy_monster(spawnIds=[1011])
        self.create_monster(spawnIds=[111], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3011], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3111], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3011], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3111], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5211], visible=True) # Sound_CrystalOn
        self.set_conversation(type=1, spawnId=111, script='$02000378_BF__11_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Round11_RouteSelect(self.ctx)


class Round11_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2011])
        self.create_monster(spawnIds=[211], animationEffect=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round11_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round11_PickRoute_Right(self.ctx)


class Round11_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1311, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2311, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal19(self.ctx)


class GoToPortal19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_19')
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_29')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Round11_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1311, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2311, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal10(self.ctx)


class GoToPortal10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=12, key='FindWay', value=1)
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_10')
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_20')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[111,211])


initial_state = Wait
