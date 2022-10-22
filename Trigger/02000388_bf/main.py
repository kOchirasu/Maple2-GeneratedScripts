""" trigger/02000388_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[301,302,303,304,305], arg2=True)
        set_actor(triggerId=3001, visible=True, initialSequence='Closed')
        set_actor(triggerId=3002, visible=True, initialSequence='Closed')
        set_interact_object(triggerIds=[10001096], state=1)
        set_breakable(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821], enabled=False)
        set_breakable(triggerIds=[1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850], enabled=False)
        set_breakable(triggerIds=[1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871], enabled=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return RoomCheck()


class RoomCheck(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return CheckUserCount()
        if not is_dungeon_room():
            return QuestDungeonStart()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return mermaid_01()

state.DungeonStart = DungeonStart


class QuestDungeonStart(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[50001517], questStates=[1]):
            return mermaid_01()
        if quest_user_detected(boxIds=[702], questIds=[50001517], questStates=[2]):
            return moveuser_00()
        if quest_user_detected(boxIds=[702], questIds=[50001518], questStates=[1]):
            return moveuser_00()


class moveuser_00(state.State):
    def on_enter(self):
        move_user(mapId=2000390, portalId=2)


class mermaid_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8001,8002], returnView=False)
        create_monster(spawnIds=[102], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return mermaid_02()


class mermaid_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        set_skip(state=scene_04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return mermaid_02_talk()


class mermaid_02_talk(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__1$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        select_camera(triggerId=8006, enable=True)
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__2$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__3$', arg4=3, arg5=3)
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__4$', arg4=3, arg5=6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002')
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__5$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_01_A')
        set_mesh(triggerIds=[7001,7002], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=3001, visible=True, initialSequence='Opening')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return open_door_01()


class open_door_01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__6$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__7$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_local_camera(cameraId=8100, enable=True)
        set_breakable(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821], enabled=True)
        set_effect(triggerIds=[7101], visible=True)
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703]):
            return battle_01()


class battle_01(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__8$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__9$', arg4=2, arg5=1)
        create_monster(spawnIds=[201,202,203,204], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204]):
            return battle_02()


class battle_02(state.State):
    def on_enter(self):
        set_skip(state=open_door_03)
        select_camera(triggerId=8007, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2005')
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__10$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=704, spawnIds=[101]):
            return open_door_ready()


class open_door_ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return open_door_02()


class open_door_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2007')
        set_mesh(triggerIds=[7003,7004], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=3002, visible=True, initialSequence='Opening')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return open_door_03()


class open_door_03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_local_camera(cameraId=8100, enable=True)
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2006')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2008')
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__11$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__12$', arg4=2, arg5=0)
        set_breakable(triggerIds=[1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850], enabled=True)
        set_effect(triggerIds=[7102], visible=True)
        create_monster(spawnIds=[205,206,207,208,209], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[205,206,207,208,209]):
            return battle_03()


class battle_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__13$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__14$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001096], arg2=0):
            return battle_04()


class battle_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7103], visible=True)
        set_breakable(triggerIds=[1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871], enabled=True)
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__15$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__16$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return move_02()


class move_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2010')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2009')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705]):
            return ship_01()


class ship_01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000388_BF__MAIN__17$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$02000388_BF__MAIN__18$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[706]):
            return ship_02()


class ship_02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000388_BF__MAIN__19$', arg3='3000')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001097], arg2=0):
            return ship_03()


class ship_03(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001098], arg2=0):
            return ship_end()


class ship_end(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=ending_02)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ending()


class ending(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7104], visible=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8003,8004,8005,8006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return ending_02()


class ending_02(state.State):
    def on_enter(self):
        set_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ending_03()


class ending_03(state.State):
    def on_enter(self):
        move_user(mapId=2000389, portalId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ending_04()


class ending_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return end()


class end(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7101], visible=False)
        set_effect(triggerIds=[7102], visible=False)
        set_effect(triggerIds=[7103], visible=False)
        set_effect(triggerIds=[7104], visible=False)
        destroy_monster(spawnIds=[101,102])


