""" trigger/52000099_qd/main.xml """
from common import *
import state


class 퀘스트체크50100520(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50100520], questStates=[3]):
            return phase_end_01()
        if quest_user_detected(boxIds=[701], questIds=[50100520], questStates=[2]):
            return phase_end_01()
        if quest_user_detected(boxIds=[701], questIds=[50100520], questStates=[1]):
            return ready()


class 퀘스트체크50100540(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50100540], questStates=[3]):
            return phase_end_01()
        if quest_user_detected(boxIds=[701], questIds=[50100540], questStates=[2]):
            return phase_end_01()
        if quest_user_detected(boxIds=[701], questIds=[50100540], questStates=[1]):
            return phase_end_01()


class ready(state.State):
    def on_enter(self):
        remove_buff(boxId=701, skillId=99910180)
        set_actor(triggerId=3101, visible=False, initialSequence='Attack_Idle_A')
        set_actor(triggerId=3102, visible=False, initialSequence='Attack_Idle_A')
        set_local_camera(cameraId=8017, enable=False) # LocalTargetCamera
        set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], arg2=True)
        set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], arg2=True)
        set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], arg2=True)
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=False)
        create_monster(spawnIds=[101], arg2=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[7001], visible=False)
        set_effect(triggerIds=[7002], visible=False)
        set_effect(triggerIds=[7003], visible=False)
        set_effect(triggerIds=[7004], visible=True)
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return ready2()


class ready2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        move_user(mapId=52000099, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start2()


class start2(state.State):
    def on_enter(self):
        set_skip(state=scene_07)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8001,8002,8003], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2001')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__20$', duration=5000, align='left')
        select_camera_path(pathIds=[8004,8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2003')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2004')
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__21$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006,8007], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2006')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2005')
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__22$', duration=3000, align='left')
        set_effect(triggerIds=[7001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7002], visible=True)
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__23$', duration=3000, align='left')
        set_npc_emotion_sequence(spawnId=101, sequenceName='IceSphere_A,Attack_Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=71000007, level=1, arg4=False, arg5=False)
        add_buff(boxIds=[701], skillId=71000008, level=1, arg4=False, arg5=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25200991, textId=25200991, duration=5000)
        # <action name="몬스터소멸시킨다" arg1="101"/>
        # <action name="몬스터를생성한다" arg1="102" arg2="1"/>
        create_monster(spawnIds=[201,202,205,204], arg2=True)
        reset_camera(interpolationTime=0)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        # <action name="SetLocalCamera" cameraId="8011" enable="1"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_09()


class scene_09(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], arg2=False)
        set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], arg2=False)
        set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], arg2=False)
        add_balloon_talk(spawnId=101, msg='$52000099_QD__MAIN__24$', duration=3000)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,204,205]):
            return scene_10()


class scene_10(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='$52000099_QD__MAIN__25$', duration=3000)
        create_monster(spawnIds=[201,202,203], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203]):
            return scene_11()


class scene_11(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='$52000099_QD__MAIN__26$', duration=3000)
        create_monster(spawnIds=[206,207,203,202], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[206,207,203,202]):
            return scene_12()


class scene_12(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[123], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_13()


class scene_13(state.State):
    def on_enter(self):
        move_user(mapId=52000099, portalId=2)
        set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], arg2=True)
        set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], arg2=True)
        set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], arg2=True)
        select_camera_path(pathIds=[8011,8012], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_14()


class scene_14(state.State):
    def on_enter(self):
        set_skip(state=phase_b_scene_05)
        remove_buff(boxId=103, skillId=71000007)
        remove_buff(boxId=103, skillId=71000008)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return phase_b_scene_02()


class phase_b_scene_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_achievement(triggerId=701, type='trigger', achieve='Defence1Clear')
        move_npc(spawnId=123, patrolName='MS2PatrolData_2102')
        move_user(mapId=52000099, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return phase_b_scene_03()


class phase_b_scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8015,8016], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2008')
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__27$', duration=5000, align='left')
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__28$', duration=5000, align='left')
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__17$', duration=3000, align='left')
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__18$', duration=3000, align='left')
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__19$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return phase_b_scene_04()


class phase_b_scene_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return phase_b_scene_05()


class phase_b_scene_05(state.State):
    def on_enter(self):
        set_skip()
        destroy_monster(spawnIds=[122], arg2=True)
        destroy_monster(spawnIds=[123], arg2=True)
        create_monster(spawnIds=[124], arg2=True)
        set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], arg2=False)
        set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], arg2=False)
        set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], arg2=False)
        add_buff(boxIds=[701], skillId=71000007, level=1, arg4=False, arg5=False)
        add_buff(boxIds=[701], skillId=71000008, level=1, arg4=False, arg5=False)
        set_mesh(triggerIds=[3001,3003,3004], visible=True)
        move_user(mapId=52000099, portalId=3)
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_local_camera(cameraId=8017, enable=True) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return phase_b_scene_06()


class phase_b_scene_06(state.State):
    def on_enter(self):
        set_timer(timerId='81', seconds=81, clearAtZero=True, display=True)
        show_guide_summary(entityId=25200993, textId=25200993)
        create_monster(spawnIds=[208], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_07()


class phase_b_scene_07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[209], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_08()


class phase_b_scene_08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[210], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_09()


class phase_b_scene_09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[212,213], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_10()


class phase_b_scene_10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[211], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_11()


class phase_b_scene_11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[214,216], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_12()


class phase_b_scene_12(state.State):
    def on_enter(self):
        create_monster(spawnIds=[209,210], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_13()


class phase_b_scene_13(state.State):
    def on_enter(self):
        create_monster(spawnIds=[211,211], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_14()


class phase_b_scene_14(state.State):
    def on_enter(self):
        create_monster(spawnIds=[213,214], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_15()


class phase_b_scene_15(state.State):
    def on_enter(self):
        create_monster(spawnIds=[215,216], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_16()


class phase_b_scene_16(state.State):
    def on_enter(self):
        create_monster(spawnIds=[210,211], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_17()


class phase_b_scene_17(state.State):
    def on_enter(self):
        create_monster(spawnIds=[212,213], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_18()


class phase_b_scene_18(state.State):
    def on_enter(self):
        create_monster(spawnIds=[212,213,214], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return phase_b_scene_19()


class phase_b_scene_19(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='81'):
            return phase_b_scene_end()

    def on_exit(self):
        destroy_monster(spawnIds=[207,208,209,210,211,212,213,214,215,216,217,218,219,220])


class phase_b_scene_end(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], arg2=True)
        set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], arg2=True)
        set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], arg2=True)
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=False)
        hide_guide_summary(entityId=25200993)
        set_local_camera(cameraId=8017, enable=False) # LocalTargetCamera
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=phase_b_skip_1)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52000099, portalId=3)
        set_achievement(triggerId=701, type='trigger', achieve='Defence2Clear')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return phase_b_scene_end_02()


class phase_b_scene_end_02(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A'])
        # <action name="SetPcEmotionLoop" arg1="Emotion_Disappoint_Idle_A" arg2="7000" />
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8018,8017], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return phase_b_scene_end_03()


class phase_b_scene_end_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8019,8020], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return phase_b_scene_end_04()


class phase_b_scene_end_04(state.State):
    def on_enter(self):
        set_actor(triggerId=3101, visible=True, initialSequence='Regen_A')
        set_actor(triggerId=3102, visible=True, initialSequence='Regen_A')
        set_effect(triggerIds=[7006], visible=True)
        set_effect(triggerIds=[7007], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return phase_b_scene_end_05()


class phase_b_scene_end_05(state.State):
    def on_enter(self):
        set_actor(triggerId=3101, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=3102, visible=True, initialSequence='Idle_A')
        set_pc_emotion_sequence(sequenceNames=['Jump_Damg_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return phase_b_scene_end_06()


class phase_b_scene_end_06(state.State):
    def on_enter(self):
        set_actor(triggerId=3101, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=3102, visible=True, initialSequence='Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return phase_b_scene_end_07()


class phase_b_scene_end_07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7004], visible=True)
        move_user(mapId=52000099, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return phase_b_scene_end_07_ready()


class phase_b_scene_end_07_ready(state.State):
    def on_enter(self):
        set_actor(triggerId=3102, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return phase_b_scene_end_08()


class phase_b_scene_end_08(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[124], arg2=True)
        select_camera_path(pathIds=[8021], returnView=False)
        create_monster(spawnIds=[106], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A'])
        add_cinematic_talk(npcId=11004034, illustId='LapentaMage_Idle', msg='$52000099_QD__MAIN__33$', duration=4000, align='Left')
        add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__34$', duration=2000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return phase_b_scene_end_09()


class phase_b_scene_end_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022], returnView=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_2009')
        add_cinematic_talk(npcId=11000076, illustId='11000076', msg='$52000099_QD__MAIN__29$', duration=5000, align='left')
        add_cinematic_talk(npcId=11004034, illustId='LapentaMage_Idle', msg='$52000099_QD__MAIN__30$', duration=5000, align='left')
        set_actor(triggerId=3101, visible=False, initialSequence='Regen_A')
        set_actor(triggerId=3102, visible=False, initialSequence='Regen_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return phase_b_scene_end_10()


class phase_b_scene_end_10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        add_cinematic_talk(npcId=11000076, illustId='11000076', msg='$52000099_QD__MAIN__31$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return phase_c_01()


class phase_c_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8023], returnView=False)
        create_monster(spawnIds=[110], arg2=True)
        create_monster(spawnIds=[126], arg2=True)
        set_effect(triggerIds=[7100], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_02()


class phase_c_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=True)
        set_effect(triggerIds=[7101], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_03()


class phase_c_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[112], arg2=True)
        set_effect(triggerIds=[7102], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_04()


class phase_c_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113], arg2=True)
        set_effect(triggerIds=[7103], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_05()


class phase_c_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114], arg2=True)
        set_effect(triggerIds=[7104], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_06()


class phase_c_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[115], arg2=True)
        set_effect(triggerIds=[7105], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_07()


class phase_c_07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[116], arg2=True)
        set_effect(triggerIds=[7106], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_08()


class phase_c_08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[117], arg2=True)
        set_effect(triggerIds=[7107], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_09()


class phase_c_09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[118], arg2=True)
        set_effect(triggerIds=[7108], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_10()


class phase_c_10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[119], arg2=True)
        set_effect(triggerIds=[7109], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_11()


class phase_c_11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[120], arg2=True)
        set_effect(triggerIds=[7110], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_c_12()


class phase_c_12(state.State):
    def on_enter(self):
        create_monster(spawnIds=[121], arg2=True)
        set_effect(triggerIds=[7111], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return phase_c_13()


class phase_c_13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022], returnView=False)
        set_conversation(type=2, spawnId=11000076, script='$52000099_QD__MAIN__32$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return phase_c_14()


class phase_c_14(state.State):
    def on_enter(self):
        move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        move_npc(spawnId=110, patrolName='MS2PatrolData_2090')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return phase_c_15()


class phase_c_15(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return phase_c_16()


class phase_c_16(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], arg2=False)
        set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], arg2=False)
        set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270,3101,3102], arg2=False)
        create_monster(spawnIds=[201,202,205,204], arg2=True)
        create_monster(spawnIds=[211,212,215,214], arg2=True)
        create_monster(spawnIds=[215,216,217,218], arg2=True)
        add_buff(boxIds=[701], skillId=99910180, level=1, arg4=False, arg5=False)
        destroy_monster(spawnIds=[103])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_timer(timerId='82', seconds=82, clearAtZero=True, display=True)
        reset_camera(interpolationTime=0)
        set_local_camera(cameraId=8023, enable=True) # LocalTargetCamera
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,205,204,211,212,215,214]):
            return phase_c_end()
        if time_expired(timerId='82'):
            return phase_c_end()

    def on_exit(self):
        reset_timer(timerId='82')
        destroy_monster(spawnIds=[201,202,205,204,211,212,215,214])


class phase_c_end(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_local_camera(cameraId=8023, enable=False) # LocalTargetCamera
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return phase_c_end_02()

    def on_exit(self):
        move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        move_npc(spawnId=110, patrolName='MS2PatrolData_2090')


class phase_b_skip_1(state.State):
    def on_enter(self):
        set_actor(triggerId=3101, visible=False)
        set_actor(triggerId=3102, visible=False)
        destroy_monster(spawnIds=[124], arg2=True) # 전두용 오르데 삭제
        destroy_monster(spawnIds=[126], arg2=True)
        destroy_monster(spawnIds=[110], arg2=True)
        destroy_monster(spawnIds=[111], arg2=True)
        destroy_monster(spawnIds=[112], arg2=True)
        destroy_monster(spawnIds=[113], arg2=True)
        destroy_monster(spawnIds=[114], arg2=True)
        destroy_monster(spawnIds=[115], arg2=True)
        destroy_monster(spawnIds=[116], arg2=True)
        destroy_monster(spawnIds=[117], arg2=True)
        destroy_monster(spawnIds=[118], arg2=True)
        destroy_monster(spawnIds=[119], arg2=True)
        destroy_monster(spawnIds=[120], arg2=True)
        destroy_monster(spawnIds=[121], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_b_skip_2()


class phase_b_skip_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[126], arg2=True) # 비전두용 오르데 소환
        create_monster(spawnIds=[106], arg2=True) # 비전투 라네모네 소환
        create_monster(spawnIds=[110], arg2=True)
        create_monster(spawnIds=[111], arg2=True)
        create_monster(spawnIds=[112], arg2=True)
        create_monster(spawnIds=[113], arg2=True)
        create_monster(spawnIds=[114], arg2=True)
        create_monster(spawnIds=[115], arg2=True)
        create_monster(spawnIds=[116], arg2=True)
        create_monster(spawnIds=[117], arg2=True)
        create_monster(spawnIds=[118], arg2=True)
        create_monster(spawnIds=[119], arg2=True)
        create_monster(spawnIds=[120], arg2=True)
        create_monster(spawnIds=[121], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_b_skip_3()


class phase_b_skip_3(state.State):
    def on_enter(self):
        move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        move_npc(spawnId=110, patrolName='MS2PatrolData_2090')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return phase_b_skip_4()


class phase_b_skip_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52000099, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return phase_b_skip_5()


class phase_b_skip_5(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], arg2=False)
        set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], arg2=False)
        set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270,3101,3102], arg2=False)
        create_monster(spawnIds=[201,202,205,204], arg2=True)
        create_monster(spawnIds=[211,212,215,214], arg2=True)
        create_monster(spawnIds=[215,216,217,218], arg2=True)
        add_buff(boxIds=[701], skillId=99910180, level=1, arg4=False, arg5=False)
        destroy_monster(spawnIds=[103])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_timer(timerId='82', seconds=82, clearAtZero=True, display=True)
        reset_camera(interpolationTime=0)
        set_local_camera(cameraId=8023, enable=True) # LocalTargetCamera
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,205,204,211,212,215,214]):
            return phase_b_skip_end()
        if time_expired(timerId='82'):
            return phase_b_skip_end()

    def on_exit(self):
        reset_timer(timerId='82')
        destroy_monster(spawnIds=[201,202,205,204,211,212,215,214])


class phase_b_skip_end(state.State):
    def on_enter(self):
        set_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_local_camera(cameraId=8023, enable=False) # LocalTargetCamera
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return phase_c_end_02()

    def on_exit(self):
        move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        move_npc(spawnId=110, patrolName='MS2PatrolData_2090')


class phase_end_01(state.State):
    def on_enter(self):
        set_actor(triggerId=3101, visible=False)
        set_actor(triggerId=3102, visible=False)
        set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], arg2=False)
        set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], arg2=False)
        set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], arg2=False)
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_02()


class phase_end_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[126], arg2=True) # 비전투 오르데 소환
        create_monster(spawnIds=[110], arg2=True)
        create_monster(spawnIds=[106], arg2=True) # 비전투 라네모네 소환
        create_monster(spawnIds=[111], arg2=True)
        set_effect(triggerIds=[7101], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_03()


class phase_end_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[112], arg2=True)
        set_effect(triggerIds=[7102], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_04()


class phase_end_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113], arg2=True)
        set_effect(triggerIds=[7103], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_05()


class phase_end_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114], arg2=True)
        set_effect(triggerIds=[7104], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_06()


class phase_end_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[115], arg2=True)
        set_effect(triggerIds=[7105], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_07()


class phase_end_07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[116], arg2=True)
        set_effect(triggerIds=[7106], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_08()


class phase_end_08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[117], arg2=True)
        set_effect(triggerIds=[7107], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_09()


class phase_end_09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[118], arg2=True)
        set_effect(triggerIds=[7108], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_10()


class phase_end_10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[119], arg2=True)
        set_effect(triggerIds=[7109], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_11()


class phase_end_11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[120], arg2=True)
        set_effect(triggerIds=[7110], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return phase_end_12()


class phase_end_12(state.State):
    def on_enter(self):
        create_monster(spawnIds=[121], arg2=True)
        set_effect(triggerIds=[7111], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return phase_end()


class phase_end(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8023, enable=False) # LocalTargetCamera
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return phase_c_end_02()

    def on_exit(self):
        move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        move_npc(spawnId=110, patrolName='MS2PatrolData_2090')


class phase_c_end_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_achievement(triggerId=701, type='trigger', achieve='AlonRpClear')
        reset_camera(interpolationTime=0)
        move_user(mapId=52000099, portalId=2)
        create_monster(spawnIds=[104], arg2=True)
        remove_buff(boxId=701, skillId=99910180)


