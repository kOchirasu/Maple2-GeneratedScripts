""" trigger/63000041_cs/main.xml """
import trigger_api


# 플레이어 감지
# 60002 : 모든 영역
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(pathIds=[8001], returnView=False) # 디폴트 카메라
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_effect(triggerIds=[7002], visible=False)
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7004], visible=False)
        self.set_effect(triggerIds=[7005], visible=True) # mask_black
        self.set_effect(triggerIds=[7006], visible=False)
        self.set_effect(triggerIds=[7301], visible=False) # Eff_Object_WoodenCart_01
        self.set_effect(triggerIds=[7302], visible=False) # Eff_Object_Intro_Zoomin_01
        self.set_effect(triggerIds=[7303], visible=False) # Eff_Object_Quest_Footsteps_01
        self.set_effect(triggerIds=[7304], visible=False) # Eff_Object_Madria_Regen_01
        self.set_effect(triggerIds=[7305], visible=False) # Eff_Object_Bella_Regen_01
        self.set_effect(triggerIds=[7306], visible=False) # Eff_Object_ExplosionRumble_01
        self.set_effect(triggerIds=[7307], visible=False) # Eff_Object_Fireburning_01
        self.set_effect(triggerIds=[7309], visible=False) # Eff_Object_Madria_Magic_Regen_01
        self.set_npc_emotion_loop(spawnId=505, sequenceName='Down_Idle_A', duration=600000)
        self.set_npc_emotion_loop(spawnId=506, sequenceName='Down_Idle_A', duration=600000)
        self.set_npc_emotion_loop(spawnId=507, sequenceName='Down_Idle_A', duration=600000)
        self.set_npc_emotion_loop(spawnId=508, sequenceName='Down_Idle_A', duration=600000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702]):
            return scene_ready1(self.ctx)


class scene_ready1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[101,102], animationEffect=True) # 수레, 조디
        self.create_monster(spawnIds=[201,202,203], animationEffect=True) # 짐꾼
        self.create_monster(spawnIds=[301,302,303], animationEffect=True) # 짐꾼
        self.create_monster(spawnIds=[501,502,503,504,505,506,507,508], animationEffect=True) # 짐꾼
        self.create_monster(spawnIds=[666], animationEffect=True) # 마드리아
        self.move_user(mapId=63000041, portalId=1)
        self.set_scene_skip(state=skip_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_set1(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[7005], visible=False)


class scene_set1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7301], visible=True)
        self.select_camera_path(pathIds=[8001,8002,8003,8004,8005,8006], returnView=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_2002')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_2003')
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_3001')
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=303, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1101')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1102')
        self.move_user_path(patrolName='MS2PatrolData_1103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01_b1(self.ctx)


class scene_01_b1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return scene_01_1(self.ctx)


class scene_01_1(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__0$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2300):
            return scene_01_c1(self.ctx)


class scene_01_c1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7302], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return scene_02_1(self.ctx)


class scene_02_1(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$63000041_CS__MAIN__1$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03_1(self.ctx)


class scene_03_1(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__2$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_04_1(self.ctx)


class scene_04_1(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__3$', duration=3000, delayTick=0)
        self.add_balloon_talk(spawnId=201, msg='$63000041_CS__MAIN__4$', duration=3000, delayTick=1000)
        self.add_balloon_talk(spawnId=203, msg='$63000041_CS__MAIN__5$', duration=3000, delayTick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_01_2(self.ctx)


class scene_01_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7303], visible=True)
        self.create_monster(spawnIds=[401,402,403], animationEffect=True) # 근위병
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_4001')
        self.move_npc(spawnId=402, patrolName='MS2PatrolData_4002')
        self.move_npc(spawnId=403, patrolName='MS2PatrolData_4003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_02_2(self.ctx)


class scene_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=402, msg='$63000041_CS__MAIN__6$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=403, msg='$63000041_CS__MAIN__7$', duration=2000, delayTick=1000)
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__8$', duration=3000, delayTick=2000)
        self.add_balloon_talk(spawnId=401, msg='$63000041_CS__MAIN__9$', duration=3000, delayTick=4000)
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__10$', duration=3000, delayTick=7000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return scene_03_2(self.ctx)


class scene_03_2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=402, patrolName='MS2PatrolData_4013')
        self.move_npc(spawnId=403, patrolName='MS2PatrolData_4012')
        self.add_balloon_talk(spawnId=402, msg='$63000041_CS__MAIN__11$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2300):
            return scene_04_2(self.ctx)


class scene_04_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7303], visible=True)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2011')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_2012')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_2013')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2300):
            return scene_05_2(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[201,202,203,101,301,302,303,402,403,506])


class scene_05_2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8007], returnView=False)
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Talk_A')
        self.add_balloon_talk(spawnId=401, msg='$63000041_CS__MAIN__12$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_talk_01_2(self.ctx)


class scene_talk_01_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__13$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_talk_02_2(self.ctx)


class scene_talk_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Talk_A')
        self.add_balloon_talk(spawnId=401, msg='$63000041_CS__MAIN__14$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_talk_03_2(self.ctx)


class scene_talk_03_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__15$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_talk_04_2(self.ctx)


class scene_talk_04_2(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=401, msg='$63000041_CS__MAIN__16$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_talk_05_2(self.ctx)


class scene_talk_05_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.add_balloon_talk(spawnId=0, msg='$63000041_CS__MAIN__17$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_talk_06_2(self.ctx)


class scene_talk_06_2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_4021')
        self.add_balloon_talk(spawnId=401, msg='$63000041_CS__MAIN__18$', duration=3000, delayTick=0)
        self.add_balloon_talk(spawnId=401, msg='$63000041_CS__MAIN__19$', duration=3000, delayTick=3000)
        self.add_balloon_talk(spawnId=401, msg='$63000041_CS__MAIN__20$', duration=3000, delayTick=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7500):
            return scene_06_2(self.ctx)


class scene_06_2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_4011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_07_2(self.ctx)


class scene_07_2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1112')
        self.move_user_path(patrolName='MS2PatrolData_1113')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_08_2(self.ctx)


class scene_08_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7306], visible=True)
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_effect(triggerIds=[7002], visible=True)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1122')
        self.move_user_path(patrolName='MS2PatrolData_1123')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_09_2(self.ctx)


class scene_09_2(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[401])
        self.add_balloon_talk(spawnId=0, msg='$63000041_CS__MAIN__55$', duration=3000, delayTick=0)
        self.add_balloon_talk(spawnId=0, msg='$63000041_CS__MAIN__21$', duration=3000, delayTick=1000)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return scene_10_2(self.ctx)


class scene_10_2(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__22$', duration=3000, delayTick=3000)
        # <action name="유저를이동시킨다" arg1="63000041" arg2="2"/>
        self.move_npc(spawnId=666, patrolName='MS2PatrolData_6661')
        self.move_user_path(patrolName='MS2PatrolData_1132')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_01_ready3(self.ctx)


class scene_01_ready3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8008,8009,8010], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1133')
        self.move_user(mapId=63000041, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6500):
            return scene_01_3(self.ctx)


class scene_01_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8011,8012], returnView=False)
        self.set_effect(triggerIds=[7307], visible=True) # Eff_Object_Fireburning_01
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__23$', duration=4000, align='center')
        self.set_onetime_effect(id=1966, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_01_00001966.xml')
        self.show_caption(scale=2.3, type='NameCaption', title='$63000041_CS__MAIN__56$', desc='$63000041_CS__MAIN__57$', align='centerLeft', offsetRateX=-0.15, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return scene_02_3(self.ctx)


class scene_02_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__24$', duration=8000, align='center')
        self.set_onetime_effect(id=1967, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_02_00001967.xml')
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=10000)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Attack_Idle_A', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return scene_03_3(self.ctx)


class scene_03_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8013], returnView=False)
        self.set_effect(triggerIds=[7309], visible=True) # Eff_Object_Madria_Magic_Regen_01
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__25$', duration=3000, align='center')
        self.set_onetime_effect(id=1968, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_03_00001968.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_npc_emotion_sequence(spawnId=666, sequenceName='Attack_01_A')
            return scene_04_3(self.ctx)


class scene_04_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7004], visible=True)
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=4000)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Dead_A', duration=2000000)
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__26$', duration=3000, delayTick=0)
        self.create_monster(spawnIds=[701,702,703,704], animationEffect=True, animationDelay=500) # 스티치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return scene_05_3(self.ctx)


class scene_05_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1901,1902], visible=True)
        self.reset_camera(interpolationTime=0.5)
        # <action name="카메라경로를선택한다" arg1="8014" arg2="1"/>
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=20063041, textId=20063041, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.move_user(mapId=63000041, portalId=2)
        self.add_balloon_talk(spawnId=666, msg='$63000041_CS__MAIN__27$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[701,702,703,704]):
            return fadeout(self.ctx)
        """
        <condition name="WaitTick" waitTick="15000" > 
            <transition state="fadeout"/>
        </condition>
        """


class fadeout(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7004], visible=False)
        self.destroy_monster(spawnIds=[701,702,703,704])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=63000041, portalId=2)
        self.set_effect(triggerIds=[7005], visible=True) # mask_black
        self.set_scene_skip(state=skip_a_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=6000)
        self.set_effect(triggerIds=[7005], visible=False) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_06_a3(self.ctx)


class scene_06_a3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8016,8021], returnView=False)
        # <action name="카메라경로를선택한다" arg1="8024" arg2="0"/>
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__28$', duration=8000, align='center')
        self.set_onetime_effect(id=1969, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_04_00001969.xml')
        self.add_balloon_talk(spawnId=666, msg='$63000041_CS__MAIN__29$', duration=8000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return scene_06_b3(self.ctx)


class scene_06_b3(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=666, sequenceName='Attack_022_C')
        self.set_effect(triggerIds=[7003], visible=True)
        self.set_effect(triggerIds=[7310], visible=True) # Eff_Object_Madria_Pc_Magic_On_01
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__30$', duration=5000, align='center')
        self.add_balloon_talk(spawnId=666, msg='$63000041_CS__MAIN__31$', duration=5000, delayTick=0)
        self.set_onetime_effect(id=1970, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_05_00001970.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return scene_06_c3(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[7004], visible=True)
        self.set_npc_emotion_sequence(spawnId=666, sequenceName='Attack_01_B')


class scene_06_c3(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=200000)
        self.face_emotion(spawnId=0, emotionName='PC_Pain_86000')
        self.set_effect(triggerIds=[7004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_06_d3(self.ctx)


class scene_06_d3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_06_3(self.ctx)


class scene_06_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7004], visible=False)
        self.set_effect(triggerIds=[7309], visible=False)
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__32$', duration=5000, align='center')
        self.add_balloon_talk(spawnId=666, msg='$63000041_CS__MAIN__33$', duration=5000, delayTick=0)
        self.set_onetime_effect(id=1971, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_06_00001971.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_07_3(self.ctx)


class scene_07_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_08_3(self.ctx)


class scene_08_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8017], returnView=False)
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__34$', duration=7500, align='center')
        self.add_balloon_talk(spawnId=666, msg='$63000041_CS__MAIN__35$', duration=7500, delayTick=500)
        self.set_onetime_effect(id=1972, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_07_00001972.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return scene_09_3(self.ctx)


class scene_09_3(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=666, patrolName='MS2PatrolData_6662')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_10_3(self.ctx)


class scene_10_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8018,8019], returnView=False)
        self.set_effect(triggerIds=[7305], visible=True) # Eff_Object_Bella_Regen_01
        self.create_monster(spawnIds=[888], animationEffect=True) # 벨라

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return scene_11_3(self.ctx)


class scene_11_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8025], returnView=False)
        self.add_cinematic_talk(npcId=11001852, msg='$63000041_CS__MAIN__36$', duration=5000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_12_3(self.ctx)


class scene_12_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__37$', duration=8000, align='center')
        self.set_onetime_effect(id=1973, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_08_00001973.xml')
        self.move_npc(spawnId=666, patrolName='MS2PatrolData_6663')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return scene_13_3(self.ctx)


class scene_13_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001852, msg='$63000041_CS__MAIN__38$', duration=5000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_14_3(self.ctx)


class scene_14_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__39$', duration=4000, align='center')
        self.set_onetime_effect(id=1974, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_09_00001974.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_15_3(self.ctx)


class scene_15_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=888, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11001852, msg='$63000041_CS__MAIN__40$', duration=8000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return scene_16_3(self.ctx)


class scene_16_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__41$', duration=6000, align='center')
        self.set_onetime_effect(id=1975, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_10_00001975.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return scene_17_3(self.ctx)


class scene_17_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8020], returnView=False)
        self.add_cinematic_talk(npcId=11001852, msg='$63000041_CS__MAIN__42$', duration=5000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_18_3(self.ctx)


class scene_18_3(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=666, patrolName='MS2PatrolData_6664')
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__43$', duration=6000, align='center')
        self.set_onetime_effect(id=1976, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_11_00001976.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return scene_19_3(self.ctx)


class scene_19_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=888, sequenceName='Attack_01_B')
        self.move_npc(spawnId=666, patrolName='MS2PatrolData_6662')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_20_3(self.ctx)


class scene_20_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001851, msg='$63000041_CS__MAIN__44$', duration=5000, align='center')
        self.set_onetime_effect(id=1977, enable=True, path='BG/Common/Sound/Eff_Madria_Tutorial_12_00001977.xml')
        self.move_npc(spawnId=888, patrolName='MS2PatrolData_8801')
        self.select_camera_path(pathIds=[8022], returnView=False)
        self.set_effect(triggerIds=[7006], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return scene_21_3(self.ctx)


class scene_21_3(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=666, patrolName='MS2PatrolData_8801')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_22_3(self.ctx)


class scene_22_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8023], returnView=False)
        self.destroy_monster(spawnIds=[888])
        self.destroy_monster(spawnIds=[666])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_1_4(self.ctx)


class scene_1_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7006], visible=False)
        self.set_effect(triggerIds=[7306], visible=True)
        self.set_effect(triggerIds=[7002], visible=True)
        self.create_monster(spawnIds=[705], animationEffect=True) # 연출용 루카락스

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_2_4(self.ctx)


class scene_2_4(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8026], returnView=False)
        self.set_effect(triggerIds=[7002], visible=True)
        self.set_effect(triggerIds=[7014], visible=True)
        self.set_npc_emotion_sequence(spawnId=705, sequenceName='AttackReady_A') # 루카락스 울부짖음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return growling(self.ctx)


class growling(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1978, enable=True, path='BG/Common/Sound/Eff_Mob_Whale_Dead_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_3_4(self.ctx)


class scene_3_4(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8009], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_4_4(self.ctx)


class scene_4_4(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=705, patrolName='MS2PatrolData_1134')
        self.set_onetime_effect(id=1979, enable=True, path='BG/Common/Sound/Eff_Object_Explosion_Debris_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_5_4(self.ctx)


class scene_5_4(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8027], returnView=False)
        self.destroy_monster(spawnIds=[705])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_6_4(self.ctx)


class scene_6_4(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000041_CS__MAIN__45$', duration=3000)
        self.set_effect(triggerIds=[7312], visible=True) # Eff_Object_Light_01
        self.set_effect(triggerIds=[7311], visible=True) # Eff_Object_ButterFly_01

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_7_4(self.ctx)


class scene_7_4(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000041_CS__MAIN__46$', duration=3000)
        self.set_onetime_effect(id=1980, enable=True, path='BG/Common/Sound/Eff_Object_Explosion_Debris_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_8_4(self.ctx)


class scene_8_4(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0, emotionName='PC_Shy_Pain_3000')
        self.add_cinematic_talk(npcId=0, msg='$63000041_CS__MAIN__47$', duration=3000)
        self.set_onetime_effect(id=1981, enable=True, path='BG/Common/Sound/Eff_Object_Explosion_Debris_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_9_4(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[7310], visible=False) # Eff_Object_PC_Regen_01_off
        self.set_effect(triggerIds=[7311], visible=False) # Eff_Object_ButterFly_01_off
        self.set_effect(triggerIds=[7312], visible=False) # Eff_Object_Light_01_off


class scene_9_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_10_4(self.ctx)


class scene_10_4(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.move_user(mapId=63000041, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_11_4(self.ctx)


class scene_11_4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[706], animationEffect=True) # 전투용 루카락스
        self.set_effect(triggerIds=[7310], visible=False) # Eff_Object_PC_Regen_01_off
        self.set_effect(triggerIds=[7311], visible=False) # Eff_Object_ButterFly_01_off
        self.set_effect(triggerIds=[7312], visible=False) # Eff_Object_Light_01_off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_12_4(self.ctx)


class scene_12_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$63000041_CS__MAIN__48$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_13_4(self.ctx)


class scene_13_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=18000):
            return whiteout(self.ctx)


class whiteout(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[706])
        self.set_onetime_effect(id=1982, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_14_4(self.ctx)


class scene_14_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_sound(triggerId=7102, enable=True)
        self.set_scene_skip(state=end_warp, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_15_4(self.ctx)


class scene_15_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$63000041_CS__MAIN__49$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_16_4(self.ctx)


class scene_16_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$63000041_CS__MAIN__50$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_17_4(self.ctx)


class scene_17_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$63000041_CS__MAIN__51$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_18_4(self.ctx)


class scene_18_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$63000041_CS__MAIN__52$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_19_4(self.ctx)


class scene_19_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$63000041_CS__MAIN__53$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_20_4(self.ctx)


class scene_20_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$63000041_CS__MAIN__54$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7005], visible=True) # mask_black
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return end_warp(self.ctx)


class end_warp(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=702, type='trigger', achieve='meetmadria1st')
        self.move_user(mapId=52010026, portalId=6001)


class skip_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=63000041, portalId=2)
        self.move_npc(spawnId=666, patrolName='MS2PatrolData_6661')
        self.select_camera_path(pathIds=[8007], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return skip_02(self.ctx)


class skip_02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,201,202,203,101,301,302,303,401,402,403,506])
        self.select_camera_path(pathIds=[8035], returnView=False)
        self.set_effect(triggerIds=[7309], visible=True) # Eff_Object_Madria_Magic_Regen_01

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return skip_03(self.ctx)


class skip_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[7004], visible=True)
        self.add_balloon_talk(spawnId=102, msg='$63000041_CS__MAIN__26$', duration=3000, delayTick=0)
        self.create_monster(spawnIds=[701,702,703,704], animationEffect=True, animationDelay=500) # 스티치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return skip_04(self.ctx)


class skip_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1901,1902], visible=True)
        self.reset_camera(interpolationTime=0.5)
        # <action name="카메라경로를선택한다" arg1="8014" arg2="1"/>
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=20063041, textId=20063041, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.move_user(mapId=63000041, portalId=2)
        self.add_balloon_talk(spawnId=666, msg='$63000041_CS__MAIN__27$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[701,702,703,704]):
            return fadeout(self.ctx)
        """
        <condition name="WaitTick" waitTick="15000" > 
            <transition state="fadeout"/>
        </condition>
        """


class skip_a_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=100)
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7004], visible=False)
        self.set_effect(triggerIds=[7309], visible=False)
        self.set_effect(triggerIds=[7006], visible=False)
        self.destroy_monster(spawnIds=[888])
        self.destroy_monster(spawnIds=[666])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_10_4(self.ctx)


initial_state = idle
