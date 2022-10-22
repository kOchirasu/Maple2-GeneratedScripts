""" trigger/52100022_qd/01_bossbattle.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[901,902,903])
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False) # ExitTop
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False) # ExitUnder
        enable_spawn_point_pc(spawnId=10000, isEnable=True) # PC스포너 제어
        enable_spawn_point_pc(spawnId=10001, isEnable=False)
        enable_spawn_point_pc(spawnId=10002, isEnable=False)
        enable_spawn_point_pc(spawnId=10003, isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return Boss01SpawnDelay()
        if user_detected(boxIds=[9002]):
            return Boss02SpawnDelay()
        if user_detected(boxIds=[9003]):
            return Boss03SpawnDelay()


#  오른쪽 
class Boss01SpawnDelay(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=10000, isEnable=False) # 기본 스포너
        enable_spawn_point_pc(spawnId=10001, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Boss01Spawn()


class Boss01Spawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901], arg2=False) # 23100084
        set_user_value(triggerId=1122330, key='AgentOff', value=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Boss01Talk01()


class Boss01Talk01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003068, script='$02000382_BF__01_BOSSBATTLE__0$', arg4=4) # 설눈이
        set_skip(state=Boss01Talk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Boss01Talk01Skip()


class Boss01Talk01Skip(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Boss01Talk02()


class Boss01Talk02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003069, script='$02000382_BF__01_BOSSBATTLE__1$', arg4=5) # 에르다
        set_skip(state=Boss01Talk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Boss01Talk02Skip()


class Boss01Talk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901]):
            return LeavePortalOn()


#  중앙 
class Boss02SpawnDelay(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=10000, isEnable=False) # 기본 스포너
        enable_spawn_point_pc(spawnId=10002, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Boss02Spawn()


class Boss02Spawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[902], arg2=False) # 23000086

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Boss02CameraSet()


class Boss02CameraSet(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=511, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Boss02Talk01()


class Boss02Talk01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003068, script='$02000382_BF__01_BOSSBATTLE__2$', arg4=3) # 설눈이
        set_skip(state=Boss02Talk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Boss02Talk01Skip()


class Boss02Talk01Skip(state.State):
    def on_enter(self):
        select_camera(triggerId=512, enable=True)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Boss02Talk02()


class Boss02Talk02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003069, script='$02000382_BF__01_BOSSBATTLE__3$', arg4=4) # 에르다
        set_skip(state=Boss02Talk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Boss02Talk02Skip()


class Boss02Talk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[902]):
            return LeavePortalOn()


#  왼쪽 
class Boss03SpawnDelay(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=10000, isEnable=False) # 기본 스포너
        enable_spawn_point_pc(spawnId=10003, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Boss03Spawn()


class Boss03Spawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[903], arg2=False) # 23000087
        set_user_value(triggerId=1122330, key='AgentOff', value=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=521, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Boss03Talk01()


class Boss03Talk01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003068, script='$02000382_BF__01_BOSSBATTLE__4$', arg4=4) # 설눈이
        set_skip(state=Boss03Talk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Boss03Talk01Skip()


class Boss03Talk01Skip(state.State):
    def on_enter(self):
        select_camera(triggerId=522, enable=True)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Boss03Talk02()


class Boss03Talk02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003069, script='$02000382_BF__01_BOSSBATTLE__5$', arg4=5) # 에르다
        set_skip(state=Boss03Talk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Boss03Talk02Skip()


class Boss03Talk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[903]):
            return LeavePortalOn()


#  종료 
class LeavePortalOn(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='BossKill', value=1)
        destroy_monster(spawnIds=[901,902,903])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        dungeon_clear()
        set_achievement(triggerId=9900, type='trigger', achieve='ClearSnowQueen')
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True) # ExitTop
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True) # ExitUnder


