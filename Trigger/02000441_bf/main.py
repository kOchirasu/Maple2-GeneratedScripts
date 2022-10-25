""" trigger/02000441_bf/main.xml """
import common


# 플레이어 감지
class idle(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[85000], visible=True, arg3=0, delay=0, scale=0)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[301,302,303,304,305], animationEffect=True)
        self.set_actor(triggerId=3001, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=3002, visible=True, initialSequence='Closed')
        self.set_interact_object(triggerIds=[10001096], state=0)
        self.set_interact_object(triggerIds=[10001097], state=2)
        self.set_interact_object(triggerIds=[10001098], state=2)
        self.set_breakable(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821], enable=False)
        self.set_breakable(triggerIds=[1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850], enable=False)
        self.set_breakable(triggerIds=[1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='start', value=1):
            return QuestDungeonStart(self.ctx)


class QuestDungeonStart(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> common.Trigger:
        if self.true():
            return mermaid_01(self.ctx)


class mermaid_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8001,8002], returnView=False)
        self.create_monster(spawnIds=[102], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=700):
            return mermaid_02(self.ctx)


class mermaid_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.set_skip(state=scene_04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return mermaid_02_talk(self.ctx)


class mermaid_02_talk(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__1$', arg4=2, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_01(self.ctx)


class scene_01(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.select_camera(triggerId=8006, enable=True)
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__2$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__19$', arg4=3, arg5=3)
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__3$', arg4=3, arg5=6)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2002')
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__4$', arg4=2, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_01_A')
        self.set_mesh(triggerIds=[7001,7002], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=3001, visible=True, initialSequence='Opening')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return open_door_01(self.ctx)


class open_door_01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__5$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__6$', arg4=2, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
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

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[703]):
            return battle_01(self.ctx)


class battle_01(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__7$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__8$', arg4=2, arg5=1)
        self.create_monster(spawnIds=[201,202,203,204], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[201,202]):
            return battle_01_2(self.ctx)


class battle_01_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[20101,20202,20303,20404,20505,20606,20708,20408], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[20101,20202,20303,20404,20505,20606,20708,20408]):
            return battle_02(self.ctx)


class battle_02(common.Trigger):
    def on_enter(self):
        self.set_skip(state=open_door_03)
        self.select_camera(triggerId=8007, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2005')
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__9$', arg4=3, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=704, spawnIds=[101]):
            return open_door_ready(self.ctx)


class open_door_ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return open_door_02(self.ctx)


class open_door_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2007')
        self.set_mesh(triggerIds=[7003,7004], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=3002, visible=True, initialSequence='Opening')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return open_door_03(self.ctx)


class open_door_03(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_local_camera(cameraId=8100, enable=True)
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2008')
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__10$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__11$', arg4=2, arg5=0)
        self.set_breakable(triggerIds=[1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850], enable=True)
        self.set_effect(triggerIds=[7102], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return open_door_03_2(self.ctx)


class open_door_03_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[707]):
            return open_door_03_3(self.ctx)


class open_door_03_3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205,206,207,208,209], animationEffect=True)
        self.set_user_value(triggerId=2038806, key='monster_respawn', value=1)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[209]):
            return battle_03(self.ctx)


class battle_03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__12$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__13$', arg4=2, arg5=2)
        self.set_interact_object(triggerIds=[10001096], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001096], stateValue=0):
            return battle_04(self.ctx)


class battle_04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7103], visible=True)
        self.set_breakable(triggerIds=[1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871], enable=True)
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__14$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__15$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return move_02(self.ctx)


class move_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2010')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2009')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[705]):
            return ship_01(self.ctx)


class ship_01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000441_BF__MAIN__16$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$02000441_BF__MAIN__17$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[706]):
            return ship_01_1(self.ctx)


class ship_01_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[301,302,303,304,305]):
            return ship_01_2(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[401,402], animationEffect=True)
        self.set_user_value(triggerId=2038805, key='monster_buff', value=1)


class ship_01_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[401,402]):
            return ship_02(self.ctx)


class ship_02(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001097], state=1)
        self.set_interact_object(triggerIds=[10001098], state=1)
        self.set_event_ui(type=1, arg2='$02000441_BF__MAIN__18$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001097], stateValue=0):
            return ship_03(self.ctx)


class ship_03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001098], stateValue=0):
            return ship_end(self.ctx)


class ship_end(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=ending_02)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ending(self.ctx)


class ending(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7104], visible=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8003,8004,8005,8006], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return ending_02(self.ctx)


class ending_02(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ending_03(self.ctx)


class ending_03(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000442, portalId=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_04(self.ctx)


class ending_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7101], visible=False)
        self.set_effect(triggerIds=[7102], visible=False)
        self.set_effect(triggerIds=[7103], visible=False)
        self.set_effect(triggerIds=[7104], visible=False)
        self.destroy_monster(spawnIds=[101,102])


initial_state = idle
