""" trigger/52000052_qd/01_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=False, arg3=0, delay=0, scale=0) # MobGround_AlawaysOff
        self.set_mesh(triggerIds=[4001,4002,4003,4004,4005,4006,4007,4008], visible=True, arg3=0, delay=0, scale=0) # LaserTotemBarrier_AlawaysOn
        self.set_mesh(triggerIds=[4100,4101,4102,4103,4104,4105,4106], visible=False, arg3=0, delay=0, scale=0) # JuntaFlyGround_AlawaysOff
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3101], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3001], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3101], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5201], visible=False) # Sound_CrystalOn
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, boxId=1):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[100,200], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=500, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Dialogue02(self.ctx)


class Dialogue02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001557, script='$52000052_QD__01_FINDWAY__0$', arg4=5) # 준타
        self.set_skip(state=Dialogue02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Dialogue02Skip(self.ctx)


class Dialogue02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToWalkIn01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_100')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_200')
        self.set_conversation(type=1, spawnId=200, arg4=3, arg5=0) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1301, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2301, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$52000052_QD__01_FINDWAY__1$', arg4=3, arg5=0) # 준타
        self.set_conversation(type=1, spawnId=100, script='$52000052_QD__01_FINDWAY__2$', arg4=2, arg5=3) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5300):
            return Round01_Start(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[100,200])


class Round01_Start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001], animationEffect=False) # 수호대상 틴차이
        self.create_monster(spawnIds=[2001], animationEffect=False) # 전투용 준타
        self.set_user_value(triggerId=901, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='01RoundSuccess', value=1):
            return Round01_Sucess(self.ctx)


class Round01_Sucess(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001')
        self.destroy_monster(spawnIds=[1001])
        self.create_monster(spawnIds=[101], animationEffect=False) # 연출용 틴차이
        self.set_effect(triggerIds=[5201], visible=True) # Sound_CrystalOn
        self.set_mesh(triggerIds=[3001], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3101], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3001], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3101], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_conversation(type=1, spawnId=101, script='$52000052_QD__01_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round01_RouteSelect(self.ctx)


class Round01_RouteSelect(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2001])
        self.create_monster(spawnIds=[201], animationEffect=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round01_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round01_PickRoute_Right(self.ctx)


class Round01_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1301, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2301, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound02(self.ctx)


class GoToRound02(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Round01_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1301, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2301, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToRound03(self.ctx)


class GoToRound03(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=3, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
