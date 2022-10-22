""" trigger/52100013_qd/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False)
        enable_spawn_point_pc(spawnId=11001, isEnable=True)
        enable_spawn_point_pc(spawnId=11002, isEnable=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[101,102], arg2=True)
        set_mesh(triggerIds=[1001,1002,1003], visible=True)
        set_mesh(triggerIds=[2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166,2167,2168,2169,2170,2171,2172,2173,2174,2175,2176,2177,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199], visible=False)
        move_user(mapId=52100013, portalId=2)
        set_local_camera(cameraId=8001, enable=True) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return ready()


class ready(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return dungeonReady()
        if not is_dungeon_room():
            return questReady()


class dungeonReady(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_local_camera(cameraId=8001, enable=True) # LocalTargetCamera
        set_gravity(gravity=-25)
        create_monster(spawnIds=[201], arg2=True)
        enable_spawn_point_pc(spawnId=11001, isEnable=False)
        enable_spawn_point_pc(spawnId=11002, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_01()


class questReady(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_local_camera(cameraId=8001, enable=True) # LocalTargetCamera
        set_gravity(gravity=-25)
        create_monster(spawnIds=[210], arg2=True)
        enable_spawn_point_pc(spawnId=11001, isEnable=False)
        enable_spawn_point_pc(spawnId=11002, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_01()
        if quest_user_detected(boxIds=[701], questIds=[50100080], questStates=[2]):
            return QuestEnd()
        if quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[1]):
            return QuestEnd()


class QuestEnd(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[210,501,502,503,504,505,506,507,508,509,510]) # 수중 위 몬스터 제거


class scene_01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52100013_QD__MAIN__0$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=101, script='$52100013_QD__MAIN__1$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52100013_QD__MAIN__2$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$52100013_QD__MAIN__3$', arg4=2, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2005')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2006')


