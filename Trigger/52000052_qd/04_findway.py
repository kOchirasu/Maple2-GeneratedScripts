""" trigger/52000052_qd/04_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(triggerIds=[4024], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3004], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3104], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3004], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3104], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5204], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWayLeft', value=0)
        self.set_user_value(key='FindWayRight', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWayLeft', value=1):
            return ReadyToWalkIn_FromLeft01(self.ctx)
        if self.user_value(key='FindWayRight', value=1):
            return ReadyToWalkIn_FromRight01(self.ctx)


# 왼쪽에서 진입
class ReadyToWalkIn_FromLeft01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4024], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_104L')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_204L')
        self.set_conversation(type=1, spawnId=202, script='$52000052_QD__04_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn_FromLeft02(self.ctx)


class ReadyToWalkIn_FromLeft02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1304, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2304, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn_FromLeft03(self.ctx)


class ReadyToWalkIn_FromLeft03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=102, script='$52000052_QD__04_FINDWAY__1$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round04_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[102,202])


# 오른쪽에서 진입
class ReadyToWalkIn_FromRight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4024], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_104R')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_204R')
        self.set_conversation(type=1, spawnId=203, script='$52000052_QD__04_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn_FromRight02(self.ctx)


class ReadyToWalkIn_FromRight02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1304, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2304, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn_FromRight03(self.ctx)


class ReadyToWalkIn_FromRight03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=103, script='$52000052_QD__04_FINDWAY__1$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round04_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[103,203])


class Round04_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1004], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2004], animationEffect=False) # 전투용 준타
        self.set_conversation(type=1, spawnId=1004, script='$52000052_QD__04_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=904, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='04RoundSuccess', value=1):
            return Round04_Sucess02(self.ctx)


"""
class Round04_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9004, spawnIds=[2204]):
            return Round04_Sucess02(self.ctx)

"""


# 20170223 업데이트 던전 개편 단축
class Round04_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawnId=2204, patrolName='MS2PatrolData_2004')
        self.move_npc(spawnId=2004, patrolName='MS2PatrolData_2004')
        self.destroy_monster(spawnIds=[1004])
        self.create_monster(spawnIds=[104], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3004], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        # <action name="메쉬를설정한다" arg1="3104" arg2="1" arg3="0" arg4="0" arg5="0" />  CrystalOn
        self.set_mesh_animation(triggerIds=[3004], visible=False, arg3=0, arg4=0) # CrystalOff
        # <action name="메쉬애니를설정한다" arg1="3104" arg2="1" arg3="0" arg4="0" />  CrystalOn
        self.set_effect(triggerIds=[5204], visible=True) # Sound_CrystalOn
        self.set_portal(portalId=21, visible=True, enable=True, minimapVisible=False)
        self.set_conversation(type=1, spawnId=104, script='$52000052_QD__04_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round04_RouteSelect(self.ctx)


class Round04_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawnIds=[2204])
        self.destroy_monster(spawnIds=[2004])
        self.create_monster(spawnIds=[204], animationEffect=False) # 연출용 준타
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_104New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(rate=50):
            return Round04_PickRoute_Left(self.ctx)
        """
        """
        if self.random_condition(rate=50):
            return Round04_PickRoute_Right(self.ctx)
        """
        if self.wait_tick(waitTick=1000):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[104])
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204New')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[204])


# 20170223 업데이트 던전 개편 단축
class Round04_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1304, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2304, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound05(self.ctx)


class GoToRound05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=5, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Round04_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1304, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2304, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound06(self.ctx)


class GoToRound06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=6, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
