""" trigger/52100022_qd/01_bossbattle.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901,902,903])
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False) # ExitTop
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False) # ExitUnder
        self.enable_spawn_point_pc(spawnId=10000, isEnable=True) # PC스포너 제어
        self.enable_spawn_point_pc(spawnId=10001, isEnable=False)
        self.enable_spawn_point_pc(spawnId=10002, isEnable=False)
        self.enable_spawn_point_pc(spawnId=10003, isEnable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return Boss01SpawnDelay(self.ctx)
        if self.user_detected(boxIds=[9002]):
            return Boss02SpawnDelay(self.ctx)
        if self.user_detected(boxIds=[9003]):
            return Boss03SpawnDelay(self.ctx)


# 오른쪽
class Boss01SpawnDelay(trigger_api.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=10000, isEnable=False) # 기본 스포너
        self.enable_spawn_point_pc(spawnId=10001, isEnable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Boss01Spawn(self.ctx)


class Boss01Spawn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901], animationEffect=False) # 23100084
        self.set_user_value(triggerId=1122330, key='AgentOff', value=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Boss01Talk01(self.ctx)


class Boss01Talk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003068, script='$02000382_BF__01_BOSSBATTLE__0$', arg4=4) # 설눈이
        self.set_skip(state=Boss01Talk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Boss01Talk01Skip(self.ctx)


class Boss01Talk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=502, enable=True)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Boss01Talk02(self.ctx)


class Boss01Talk02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003069, script='$02000382_BF__01_BOSSBATTLE__1$', arg4=5) # 에르다
        self.set_skip(state=Boss01Talk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Boss01Talk02Skip(self.ctx)


class Boss01Talk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901]):
            return LeavePortalOn(self.ctx)


# 중앙
class Boss02SpawnDelay(trigger_api.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=10000, isEnable=False) # 기본 스포너
        self.enable_spawn_point_pc(spawnId=10002, isEnable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Boss02Spawn(self.ctx)


class Boss02Spawn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[902], animationEffect=False) # 23000086

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Boss02CameraSet(self.ctx)


class Boss02CameraSet(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=511, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Boss02Talk01(self.ctx)


class Boss02Talk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003068, script='$02000382_BF__01_BOSSBATTLE__2$', arg4=3) # 설눈이
        self.set_skip(state=Boss02Talk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Boss02Talk01Skip(self.ctx)


class Boss02Talk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=512, enable=True)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Boss02Talk02(self.ctx)


class Boss02Talk02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003069, script='$02000382_BF__01_BOSSBATTLE__3$', arg4=4) # 에르다
        self.set_skip(state=Boss02Talk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Boss02Talk02Skip(self.ctx)


class Boss02Talk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[902]):
            return LeavePortalOn(self.ctx)


# 왼쪽
class Boss03SpawnDelay(trigger_api.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=10000, isEnable=False) # 기본 스포너
        self.enable_spawn_point_pc(spawnId=10003, isEnable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Boss03Spawn(self.ctx)


class Boss03Spawn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[903], animationEffect=False) # 23000087
        self.set_user_value(triggerId=1122330, key='AgentOff', value=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=521, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Boss03Talk01(self.ctx)


class Boss03Talk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003068, script='$02000382_BF__01_BOSSBATTLE__4$', arg4=4) # 설눈이
        self.set_skip(state=Boss03Talk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Boss03Talk01Skip(self.ctx)


class Boss03Talk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=522, enable=True)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Boss03Talk02(self.ctx)


class Boss03Talk02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003069, script='$02000382_BF__01_BOSSBATTLE__5$', arg4=5) # 에르다
        self.set_skip(state=Boss03Talk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Boss03Talk02Skip(self.ctx)


class Boss03Talk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[903]):
            return LeavePortalOn(self.ctx)


# 종료
class LeavePortalOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='BossKill', value=1)
        self.destroy_monster(spawnIds=[901,902,903])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_achievement(triggerId=9900, type='trigger', achieve='ClearSnowQueen')
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True) # ExitTop
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True) # ExitUnder


initial_state = Wait
