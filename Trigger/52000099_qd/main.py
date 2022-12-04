""" trigger/52000099_qd/main.xml """
import trigger_api


class 퀘스트체크50100520(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[50100520], questStates=[3]):
            return phase_end_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100520], questStates=[2]):
            return phase_end_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100520], questStates=[1]):
            return ready(self.ctx)


class 퀘스트체크50100540(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[50100540], questStates=[3]):
            return phase_end_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100540], questStates=[2]):
            return phase_end_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100540], questStates=[1]):
            return phase_end_01(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=701, skillId=99910180)
        self.set_actor(triggerId=3101, visible=False, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=3102, visible=False, initialSequence='Attack_Idle_A')
        self.set_local_camera(cameraId=8017, enable=False) # LocalTargetCamera
        self.set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=True)
        self.set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=True)
        self.set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=True)
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=False)
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_effect(triggerIds=[7002], visible=False)
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7004], visible=True)
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return ready2(self.ctx)


class ready2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.move_user(mapId=52000099, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start2(self.ctx)


class start2(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=scene_07)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8001,8002,8003], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__20$', duration=5000, align='left')
        self.select_camera_path(pathIds=[8004,8005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2003')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2004')
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__21$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006,8007], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2005')
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__22$', duration=3000, align='left')
        self.set_effect(triggerIds=[7001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7002], visible=True)
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__23$', duration=3000, align='left')
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='IceSphere_A,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8009], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=71000007, level=1, isPlayer=False, isSkillSet=False)
        self.add_buff(boxIds=[701], skillId=71000008, level=1, isPlayer=False, isSkillSet=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25200991, textId=25200991, duration=5000)
        # <action name="몬스터소멸시킨다" arg1="101"/>
        # <action name="몬스터를생성한다" arg1="102" arg2="1"/>
        self.create_monster(spawnIds=[201,202,205,204], animationEffect=True)
        self.reset_camera(interpolationTime=0)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # <action name="SetLocalCamera" cameraId="8011" enable="1"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=False)
        self.set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=False)
        self.set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=False)
        self.add_balloon_talk(spawnId=101, msg='$52000099_QD__MAIN__24$', duration=3000)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,204,205]):
            return scene_10(self.ctx)


class scene_10(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='$52000099_QD__MAIN__25$', duration=3000)
        self.create_monster(spawnIds=[201,202,203], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203]):
            return scene_11(self.ctx)


class scene_11(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='$52000099_QD__MAIN__26$', duration=3000)
        self.create_monster(spawnIds=[206,207,203,202], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[206,207,203,202]):
            return scene_12(self.ctx)


class scene_12(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[123], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_13(self.ctx)


class scene_13(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000099, portalId=2)
        self.set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=True)
        self.set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=True)
        self.set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=True)
        self.select_camera_path(pathIds=[8011,8012], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_14(self.ctx)


class scene_14(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=phase_b_scene_05)
        self.remove_buff(boxId=103, skillId=71000007)
        self.remove_buff(boxId=103, skillId=71000008)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return phase_b_scene_02(self.ctx)


class phase_b_scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(triggerId=701, type='trigger', achieve='Defence1Clear')
        self.move_npc(spawnId=123, patrolName='MS2PatrolData_2102')
        self.move_user(mapId=52000099, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return phase_b_scene_03(self.ctx)


class phase_b_scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8015,8016], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2008')
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__27$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__28$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__17$', duration=3000, align='left')
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__18$', duration=3000, align='left')
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__19$', duration=5000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return phase_b_scene_04(self.ctx)


class phase_b_scene_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return phase_b_scene_05(self.ctx)


class phase_b_scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.destroy_monster(spawnIds=[122], arg2=True)
        self.destroy_monster(spawnIds=[123], arg2=True)
        self.create_monster(spawnIds=[124], animationEffect=True)
        self.set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=False)
        self.set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=False)
        self.set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=False)
        self.add_buff(boxIds=[701], skillId=71000007, level=1, isPlayer=False, isSkillSet=False)
        self.add_buff(boxIds=[701], skillId=71000008, level=1, isPlayer=False, isSkillSet=False)
        self.set_mesh(triggerIds=[3001,3003,3004], visible=True)
        self.move_user(mapId=52000099, portalId=3)
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_local_camera(cameraId=8017, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return phase_b_scene_06(self.ctx)


class phase_b_scene_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='81', seconds=81, startDelay=1, interval=1)
        self.show_guide_summary(entityId=25200993, textId=25200993)
        self.create_monster(spawnIds=[208], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_07(self.ctx)


class phase_b_scene_07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[209], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_08(self.ctx)


class phase_b_scene_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[210], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_09(self.ctx)


class phase_b_scene_09(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[212,213], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_10(self.ctx)


class phase_b_scene_10(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[211], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_11(self.ctx)


class phase_b_scene_11(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[214,216], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_12(self.ctx)


class phase_b_scene_12(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[209,210], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_13(self.ctx)


class phase_b_scene_13(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[211,211], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_14(self.ctx)


class phase_b_scene_14(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[213,214], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_15(self.ctx)


class phase_b_scene_15(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[215,216], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_16(self.ctx)


class phase_b_scene_16(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[210,211], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_17(self.ctx)


class phase_b_scene_17(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[212,213], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_18(self.ctx)


class phase_b_scene_18(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[212,213,214], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return phase_b_scene_19(self.ctx)


class phase_b_scene_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='81'):
            return phase_b_scene_end(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[207,208,209,210,211,212,213,214,215,216,217,218,219,220])


class phase_b_scene_end(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=True)
        self.set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=True)
        self.set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=True)
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=False)
        self.hide_guide_summary(entityId=25200993)
        self.set_local_camera(cameraId=8017, enable=False) # LocalTargetCamera
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=phase_b_skip_1)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52000099, portalId=3)
        self.set_achievement(triggerId=701, type='trigger', achieve='Defence2Clear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return phase_b_scene_end_02(self.ctx)


class phase_b_scene_end_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A'])
        # <action name="SetPcEmotionLoop" arg1="Emotion_Disappoint_Idle_A" arg2="7000" />
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8018,8017], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return phase_b_scene_end_03(self.ctx)


class phase_b_scene_end_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8019,8020], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return phase_b_scene_end_04(self.ctx)


class phase_b_scene_end_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3101, visible=True, initialSequence='Regen_A')
        self.set_actor(triggerId=3102, visible=True, initialSequence='Regen_A')
        self.set_effect(triggerIds=[7006], visible=True)
        self.set_effect(triggerIds=[7007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return phase_b_scene_end_05(self.ctx)


class phase_b_scene_end_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3101, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=3102, visible=True, initialSequence='Idle_A')
        self.set_pc_emotion_sequence(sequenceNames=['Jump_Damg_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return phase_b_scene_end_06(self.ctx)


class phase_b_scene_end_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3101, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=3102, visible=True, initialSequence='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return phase_b_scene_end_07(self.ctx)


class phase_b_scene_end_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7004], visible=True)
        self.move_user(mapId=52000099, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return phase_b_scene_end_07_ready(self.ctx)


class phase_b_scene_end_07_ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3102, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return phase_b_scene_end_08(self.ctx)


class phase_b_scene_end_08(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[124], arg2=True)
        self.select_camera_path(pathIds=[8021], returnView=False)
        self.create_monster(spawnIds=[106], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A'])
        self.add_cinematic_talk(npcId=11004034, illustId='LapentaMage_Idle', msg='$52000099_QD__MAIN__33$', duration=4000, align='Left')
        self.add_cinematic_talk(npcId=11003087, illustId='11003087', msg='$52000099_QD__MAIN__34$', duration=2000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return phase_b_scene_end_09(self.ctx)


class phase_b_scene_end_09(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8022], returnView=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2009')
        self.add_cinematic_talk(npcId=11000076, illustId='11000076', msg='$52000099_QD__MAIN__29$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=11004034, illustId='LapentaMage_Idle', msg='$52000099_QD__MAIN__30$', duration=5000, align='left')
        self.set_actor(triggerId=3101, visible=False, initialSequence='Regen_A')
        self.set_actor(triggerId=3102, visible=False, initialSequence='Regen_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return phase_b_scene_end_10(self.ctx)


class phase_b_scene_end_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        self.add_cinematic_talk(npcId=11000076, illustId='11000076', msg='$52000099_QD__MAIN__31$', duration=5000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return phase_c_01(self.ctx)


class phase_c_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8023], returnView=False)
        self.create_monster(spawnIds=[110], animationEffect=True)
        self.create_monster(spawnIds=[126], animationEffect=True)
        self.set_effect(triggerIds=[7100], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_02(self.ctx)


class phase_c_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.set_effect(triggerIds=[7101], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_03(self.ctx)


class phase_c_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.set_effect(triggerIds=[7102], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_04(self.ctx)


class phase_c_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.set_effect(triggerIds=[7103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_05(self.ctx)


class phase_c_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.set_effect(triggerIds=[7104], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_06(self.ctx)


class phase_c_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[115], animationEffect=True)
        self.set_effect(triggerIds=[7105], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_07(self.ctx)


class phase_c_07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[116], animationEffect=True)
        self.set_effect(triggerIds=[7106], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_08(self.ctx)


class phase_c_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[117], animationEffect=True)
        self.set_effect(triggerIds=[7107], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_09(self.ctx)


class phase_c_09(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[118], animationEffect=True)
        self.set_effect(triggerIds=[7108], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_10(self.ctx)


class phase_c_10(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[119], animationEffect=True)
        self.set_effect(triggerIds=[7109], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_11(self.ctx)


class phase_c_11(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[120], animationEffect=True)
        self.set_effect(triggerIds=[7110], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_c_12(self.ctx)


class phase_c_12(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[121], animationEffect=True)
        self.set_effect(triggerIds=[7111], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return phase_c_13(self.ctx)


class phase_c_13(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8022], returnView=False)
        self.set_conversation(type=2, spawnId=11000076, script='$52000099_QD__MAIN__32$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return phase_c_14(self.ctx)


class phase_c_14(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        self.move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        self.move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        self.move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        self.move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        self.move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        self.move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        self.move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2090')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return phase_c_15(self.ctx)


class phase_c_15(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return phase_c_16(self.ctx)


class phase_c_16(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=False)
        self.set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=False)
        self.set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270,3101,3102], visible=False)
        self.create_monster(spawnIds=[201,202,205,204], animationEffect=True)
        self.create_monster(spawnIds=[211,212,215,214], animationEffect=True)
        self.create_monster(spawnIds=[215,216,217,218], animationEffect=True)
        self.add_buff(boxIds=[701], skillId=99910180, level=1, isPlayer=False, isSkillSet=False)
        self.destroy_monster(spawnIds=[103])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timerId='82', seconds=82, startDelay=1, interval=1)
        self.reset_camera(interpolationTime=0)
        self.set_local_camera(cameraId=8023, enable=True) # LocalTargetCamera
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,205,204,211,212,215,214]):
            return phase_c_end(self.ctx)
        if self.time_expired(timerId='82'):
            return phase_c_end(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='82')
        self.destroy_monster(spawnIds=[201,202,205,204,211,212,215,214])


class phase_c_end(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_local_camera(cameraId=8023, enable=False) # LocalTargetCamera
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return phase_c_end_02(self.ctx)

    def on_exit(self):
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        self.move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        self.move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        self.move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        self.move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        self.move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        self.move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        self.move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2090')


class phase_b_skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3101, visible=False)
        self.set_actor(triggerId=3102, visible=False)
        self.destroy_monster(spawnIds=[124], arg2=True) # 전두용 오르데 삭제
        self.destroy_monster(spawnIds=[126], arg2=True)
        self.destroy_monster(spawnIds=[110], arg2=True)
        self.destroy_monster(spawnIds=[111], arg2=True)
        self.destroy_monster(spawnIds=[112], arg2=True)
        self.destroy_monster(spawnIds=[113], arg2=True)
        self.destroy_monster(spawnIds=[114], arg2=True)
        self.destroy_monster(spawnIds=[115], arg2=True)
        self.destroy_monster(spawnIds=[116], arg2=True)
        self.destroy_monster(spawnIds=[117], arg2=True)
        self.destroy_monster(spawnIds=[118], arg2=True)
        self.destroy_monster(spawnIds=[119], arg2=True)
        self.destroy_monster(spawnIds=[120], arg2=True)
        self.destroy_monster(spawnIds=[121], arg2=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_b_skip_2(self.ctx)


class phase_b_skip_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[126], animationEffect=True) # 비전두용 오르데 소환
        self.create_monster(spawnIds=[106], animationEffect=True) # 비전투 라네모네 소환
        self.create_monster(spawnIds=[110], animationEffect=True)
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.create_monster(spawnIds=[115], animationEffect=True)
        self.create_monster(spawnIds=[116], animationEffect=True)
        self.create_monster(spawnIds=[117], animationEffect=True)
        self.create_monster(spawnIds=[118], animationEffect=True)
        self.create_monster(spawnIds=[119], animationEffect=True)
        self.create_monster(spawnIds=[120], animationEffect=True)
        self.create_monster(spawnIds=[121], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_b_skip_3(self.ctx)


class phase_b_skip_3(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        self.move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        self.move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        self.move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        self.move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        self.move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        self.move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        self.move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2090')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return phase_b_skip_4(self.ctx)


class phase_b_skip_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52000099, portalId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return phase_b_skip_5(self.ctx)


class phase_b_skip_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=False)
        self.set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=False)
        self.set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270,3101,3102], visible=False)
        self.create_monster(spawnIds=[201,202,205,204], animationEffect=True)
        self.create_monster(spawnIds=[211,212,215,214], animationEffect=True)
        self.create_monster(spawnIds=[215,216,217,218], animationEffect=True)
        self.add_buff(boxIds=[701], skillId=99910180, level=1, isPlayer=False, isSkillSet=False)
        self.destroy_monster(spawnIds=[103])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timerId='82', seconds=82, startDelay=1, interval=1)
        self.reset_camera(interpolationTime=0)
        self.set_local_camera(cameraId=8023, enable=True) # LocalTargetCamera
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,205,204,211,212,215,214]):
            return phase_b_skip_end(self.ctx)
        if self.time_expired(timerId='82'):
            return phase_b_skip_end(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='82')
        self.destroy_monster(spawnIds=[201,202,205,204,211,212,215,214])


class phase_b_skip_end(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_local_camera(cameraId=8023, enable=False) # LocalTargetCamera
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return phase_c_end_02(self.ctx)

    def on_exit(self):
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        self.move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        self.move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        self.move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        self.move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        self.move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        self.move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        self.move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2090')


class phase_end_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3101, visible=False)
        self.set_actor(triggerId=3102, visible=False)
        self.set_visible_breakable_object(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=False)
        self.set_visible_breakable_object(triggerIds=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=False)
        self.set_visible_breakable_object(triggerIds=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=False)
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_02(self.ctx)


class phase_end_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[126], animationEffect=True) # 비전투 오르데 소환
        self.create_monster(spawnIds=[110], animationEffect=True)
        self.create_monster(spawnIds=[106], animationEffect=True) # 비전투 라네모네 소환
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.set_effect(triggerIds=[7101], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_03(self.ctx)


class phase_end_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.set_effect(triggerIds=[7102], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_04(self.ctx)


class phase_end_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.set_effect(triggerIds=[7103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_05(self.ctx)


class phase_end_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.set_effect(triggerIds=[7104], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_06(self.ctx)


class phase_end_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[115], animationEffect=True)
        self.set_effect(triggerIds=[7105], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_07(self.ctx)


class phase_end_07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[116], animationEffect=True)
        self.set_effect(triggerIds=[7106], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_08(self.ctx)


class phase_end_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[117], animationEffect=True)
        self.set_effect(triggerIds=[7107], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_09(self.ctx)


class phase_end_09(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[118], animationEffect=True)
        self.set_effect(triggerIds=[7108], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_10(self.ctx)


class phase_end_10(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[119], animationEffect=True)
        self.set_effect(triggerIds=[7109], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_11(self.ctx)


class phase_end_11(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[120], animationEffect=True)
        self.set_effect(triggerIds=[7110], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return phase_end_12(self.ctx)


class phase_end_12(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[121], animationEffect=True)
        self.set_effect(triggerIds=[7111], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return phase_end(self.ctx)


class phase_end(trigger_api.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8023, enable=False) # LocalTargetCamera
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return phase_c_end_02(self.ctx)

    def on_exit(self):
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_2081')
        self.move_npc(spawnId=120, patrolName='MS2PatrolData_2082')
        self.move_npc(spawnId=119, patrolName='MS2PatrolData_2083')
        self.move_npc(spawnId=118, patrolName='MS2PatrolData_2085')
        self.move_npc(spawnId=117, patrolName='MS2PatrolData_2091')
        self.move_npc(spawnId=116, patrolName='MS2PatrolData_2092')
        self.move_npc(spawnId=115, patrolName='MS2PatrolData_2087')
        self.move_npc(spawnId=114, patrolName='MS2PatrolData_2088')
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_2084')
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_2089')
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_2086')
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2090')


class phase_c_end_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(triggerId=701, type='trigger', achieve='AlonRpClear')
        self.reset_camera(interpolationTime=0)
        self.move_user(mapId=52000099, portalId=2)
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.remove_buff(boxId=701, skillId=99910180)


initial_state = 퀘스트체크50100520
