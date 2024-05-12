""" trigger/02000297_bf/main2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1001,1002,1003,1004], animationEffect=False)
        self.destroy_monster(spawnIds=[1005])
        self.destroy_monster(spawnIds=[1006])
        self.destroy_monster(spawnIds=[1007])
        self.set_mesh(triggerIds=[107], visible=False, arg3=0, delay=0, scale=0) # InvisibleBarrier
        self.set_mesh(triggerIds=[31000,31001,31002,31003,31004,31005], visible=True, arg3=0, delay=0, scale=0) # Stairs
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[107], visible=True, arg3=0, delay=0, scale=0) # InvisibleBarrier
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=888888, enable=True)
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData1')
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 레논01(self.ctx)


class 레논01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000064, script='$02000297_BF__MAIN2__0$', arg4=2)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 벨라01(self.ctx)


class 벨라01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000057, script='$02000297_BF__MAIN2__1$', arg4=3)
        self.set_conversation(type=2, spawnId=11000057, script='$02000297_BF__MAIN2__2$', arg4=3)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9925):
            return 벨라02(self.ctx)


class 벨라02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData3')
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 레논02(self.ctx)


class 레논02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000064, script='$02000297_BF__MAIN2__3$', arg4=2)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 레논03(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class 레논03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1004])
        self.destroy_monster(spawnIds=[1001])
        self.create_monster(spawnIds=[1005], animationEffect=False)
        self.create_monster(spawnIds=[1008], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 블랙01(self.ctx)


class 블랙01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData0')
        self.set_conversation(type=2, spawnId=11000006, script='$02000297_BF__MAIN2__4$', arg4=2)
        self.set_conversation(type=2, spawnId=11000006, script='$02000297_BF__MAIN2__5$', arg4=2)
        self.set_conversation(type=2, spawnId=11000057, script='$02000297_BF__MAIN2__6$', arg4=3)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 카메라복귀(self.ctx)


class 카메라복귀(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=888888, enable=False)
        self.set_mesh(triggerIds=[107], visible=False, arg3=0, delay=0, scale=0) # InvisibleBarrier
        self.set_mesh(triggerIds=[31000,31001,31002,31003,31004,31005], visible=False, arg3=0, delay=0, scale=0) # Stairs
        self.create_monster(spawnIds=[6200], animationEffect=False)
        self.destroy_monster(spawnIds=[1003])
        self.destroy_monster(spawnIds=[1002])
        self.destroy_monster(spawnIds=[1001])
        self.destroy_monster(spawnIds=[1004])
        self.create_monster(spawnIds=[1005], animationEffect=False)
        self.create_monster(spawnIds=[1006], animationEffect=True)
        self.create_monster(spawnIds=[1008], animationEffect=False)
        self.set_user_value(triggerId=999991, key='BattleStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[6200]):
            return 엔딩연출1(self.ctx)


class 엔딩연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[31000,31001,31002,31003,31004,31005], visible=True, arg3=0, delay=0, scale=0) # Stairs

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 엔딩연출(self.ctx)


class 엔딩연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=888888, enable=True)
        self.destroy_monster(spawnIds=[1006])
        self.create_monster(spawnIds=[1007], animationEffect=False)
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData5')
        self.set_skip(state=연출종료2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 블랙03(self.ctx)


class 블랙03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000006, script='$02000297_BF__MAIN2__7$', arg4=3)
        self.set_conversation(type=2, spawnId=11000064, script='$02000297_BF__MAIN2__8$', arg4=3)
        self.set_conversation(type=2, spawnId=11000006, script='$02000297_BF__MAIN2__9$', arg4=3)
        self.set_skip(state=연출종료2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11101):
            return 연출종료2(self.ctx)


class 연출종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # Missing State: State
        self.set_skip()
        self.select_camera(triggerId=888888, enable=False)
        self.destroy_monster(spawnIds=[1005])
        self.destroy_monster(spawnIds=[1008])
        self.destroy_monster(spawnIds=[1007])
        self.set_achievement(triggerId=9001, type='trigger', achieve='ClearKatramusSecond')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
