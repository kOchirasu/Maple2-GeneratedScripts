""" trigger/02000378_bf/08_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=23, visible=False, enable=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(triggerIds=[4028], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3008], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3108], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3008], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3108], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5208], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal(self.ctx)


"""
class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4028], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_108')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_208')
        self.set_conversation(type=1, spawnId=203, script='$02000378_BF__08_FINDWAY__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return None # Missing State: ReadyToWalkIn02

"""


"""
class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1308, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2308, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return None # Missing State: ReadyToWalkIn03

"""


"""
class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=103, script='$02000378_BF__08_FINDWAY__1$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round08_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[103,203])

"""


# 20170223 업데이트 던전 개편 단축
# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4028], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_user_value(triggerId=1308, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2308, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[2008], animationEffect=False)
        # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=107, script='$02000378_BF__08_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round08_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[108])


class Round08_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1008], animationEffect=False) # 수호대상 틴차이
        self.set_conversation(type=1, spawnId=1008, script='$02000378_BF__08_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=908, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='08RoundSuccess', value=1):
            return Round08_Sucess02(self.ctx)


"""
class Round08_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9008, spawnIds=[2208]):
            return Round08_Sucess02(self.ctx)

"""


# 20170223 업데이트 던전 개편 단축
class Round08_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=2008, patrolName='MS2PatrolData_2008')
        # self.move_npc(spawnId=2208, patrolName='MS2PatrolData_2008')
        self.destroy_monster(spawnIds=[1008])
        self.create_monster(spawnIds=[108], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3008], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        # <action name="메쉬를설정한다" arg1="3108" arg2="1" arg3="0" arg4="0" arg5="0" />  CrystalOn
        self.set_mesh_animation(triggerIds=[3008], visible=False, arg3=0, arg4=0) # CrystalOff
        # <action name="메쉬애니를설정한다" arg1="3108" arg2="1" arg3="0" arg4="0" /> CrystalOn
        self.set_effect(triggerIds=[5208], visible=True) # Sound_CrystalOn
        self.set_portal(portalId=23, visible=True, enable=True, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        self.set_conversation(type=1, spawnId=108, script='$02000378_BF__08_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round08_RouteSelect(self.ctx)


class Round08_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2008])
        # self.destroy_monster(spawnIds=[2208])
        self.create_monster(spawnIds=[208], animationEffect=False) # 연출용 준타
        self.move_npc(spawnId=108, patrolName='MS2PatrolData_108New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(rate=50):
            return None # Missing State: Round08_PickRoute_Left
        """
        """
        if self.random_condition(rate=50):
            return None # Missing State: Round08_PickRoute_Right
        """
        if self.wait_tick(waitTick=500):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[108])
        self.move_npc(spawnId=208, patrolName='MS2PatrolData_208New')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[208])


initial_state = Wait
