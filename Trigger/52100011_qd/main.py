""" trigger/52100011_qd/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[301,302,303,304,305], animationEffect=True)
        self.set_actor(triggerId=3001, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=3002, visible=True, initialSequence='Closed')
        self.set_interact_object(triggerIds=[10002054], state=1)
        self.set_breakable(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821], enable=False)
        self.set_breakable(triggerIds=[1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850], enable=False)
        self.set_breakable(triggerIds=[1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return RoomCheck(self.ctx)


class RoomCheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return CheckUserCount(self.ctx)
        if not self.is_dungeon_room():
            return QuestDungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702]):
            return mermaid_01(self.ctx)


class QuestDungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[50100080], questStates=[1]):
            return mermaid_01(self.ctx)
        if self.quest_user_detected(boxIds=[702], questIds=[50100080], questStates=[2]):
            return moveuser_00(self.ctx)
        if self.quest_user_detected(boxIds=[702], questIds=[50100080], questStates=[1]):
            return moveuser_00(self.ctx)


class moveuser_00(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52100013, portalId=2)


class mermaid_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8001,8002], returnView=False)
        self.create_monster(spawnIds=[102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return mermaid_02(self.ctx)


class mermaid_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.set_skip(state=scene_04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return mermaid_02_talk(self.ctx)


class mermaid_02_talk(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$52100011_QD__MAIN__0$', align='left', duration=2000)
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$52100011_QD__MAIN__1$', align='right', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.select_camera(triggerId=8006, enable=True)
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$52100011_QD__MAIN__2$', align='left', duration=3000)
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$52100011_QD__MAIN__3$', align='right', duration=3000)
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$52100011_QD__MAIN__4$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2002')
        self.set_conversation(type=1, spawnId=102, script='$52100011_QD__MAIN__5$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_01_A')
        self.set_mesh(triggerIds=[7001,7002], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=3001, visible=True, initialSequence='Opening')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return open_door_01(self.ctx)


class open_door_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52100011_QD__MAIN__6$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52100011_QD__MAIN__7$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_local_camera(cameraId=8100, enable=True)
        self.set_breakable(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821], enable=True)
        self.set_effect(triggerIds=[7101], visible=True)
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703]):
            return battle_01(self.ctx)


class battle_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera
        self.set_conversation(type=1, spawnId=102, script='$52100011_QD__MAIN__8$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52100011_QD__MAIN__9$', arg4=2, arg5=1)
        self.create_monster(spawnIds=[201,202,203,204], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204]):
            return battle_02(self.ctx)


class battle_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=open_door_03)
        self.select_camera(triggerId=8007, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2005')
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$52100011_QD__MAIN__10$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=704, spawnIds=[101]):
            return open_door_ready(self.ctx)


class open_door_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return open_door_02(self.ctx)


class open_door_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2007')
        self.set_mesh(triggerIds=[7003,7004], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=3002, visible=True, initialSequence='Opening')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return open_door_03(self.ctx)


class open_door_03(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_local_camera(cameraId=8100, enable=True)
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2008')
        self.set_conversation(type=1, spawnId=102, script='$52100011_QD__MAIN__11$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=101, script='$52100011_QD__MAIN__12$', arg4=2, arg5=0)
        self.set_breakable(triggerIds=[1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850], enable=True)
        self.set_effect(triggerIds=[7102], visible=True)
        self.create_monster(spawnIds=[205,206,207,208,209], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[205,206,207,208,209]):
            return battle_03(self.ctx)


class battle_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52100011_QD__MAIN__13$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52100011_QD__MAIN__14$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002054], stateValue=0):
            return battle_04(self.ctx)


class battle_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7103], visible=True)
        self.set_breakable(triggerIds=[1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871], enable=True)
        self.set_conversation(type=1, spawnId=102, script='$52100011_QD__MAIN__15$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52100011_QD__MAIN__16$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return move_02(self.ctx)


class move_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2010')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2009')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[705]):
            return ship_01(self.ctx)


class ship_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52100011_QD__MAIN__17$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52100011_QD__MAIN__18$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[706]):
            return ship_02(self.ctx)


class ship_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52100011_QD__MAIN__19$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002055], stateValue=0):
            return ship_03(self.ctx)


class ship_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002056], stateValue=0):
            return ship_end(self.ctx)


class ship_end(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=ending_02)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ending(self.ctx)


class ending(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7104], visible=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8003,8004,8005,8006], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return ending_02(self.ctx)


class ending_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ending_03(self.ctx)


class ending_03(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52100012, portalId=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_04(self.ctx)


class ending_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7101], visible=False)
        self.set_effect(triggerIds=[7102], visible=False)
        self.set_effect(triggerIds=[7103], visible=False)
        self.set_effect(triggerIds=[7104], visible=False)
        self.destroy_monster(spawnIds=[101,102])


initial_state = idle
