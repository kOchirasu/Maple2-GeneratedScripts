""" trigger/52000069_qd/tria_bunker.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[606], visible=False)
        self.set_effect(triggerIds=[607], visible=False)
        self.set_effect(triggerIds=[608], visible=False)
        self.set_effect(triggerIds=[609], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.set_agent(triggerIds=[8009], visible=True)
        self.set_agent(triggerIds=[8010], visible=True)
        self.set_agent(triggerIds=[8011], visible=True)
        self.set_agent(triggerIds=[8012], visible=True)
        self.set_agent(triggerIds=[8013], visible=True)
        self.set_agent(triggerIds=[8014], visible=True)
        self.set_agent(triggerIds=[8015], visible=True)
        self.set_agent(triggerIds=[8016], visible=True)
        self.set_agent(triggerIds=[8017], visible=True)
        self.set_agent(triggerIds=[8018], visible=True)
        self.set_agent(triggerIds=[8019], visible=True)
        self.set_agent(triggerIds=[8020], visible=True)
        self.set_agent(triggerIds=[8021], visible=True)
        self.create_monster(spawnIds=[1000,1001,1002,1003], animationEffect=False)
        self.create_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110], animationEffect=False)
        self.create_monster(spawnIds=[1201,1202,1203], animationEffect=False)
        self.create_monster(spawnIds=[2001,2101,2102,2103,2104,2105,2106,2107,2108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_scene_skip(state=연출종료)
            self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.add_cinematic_talk(npcId=11000064, illustId='Lennon_normal', msg='$52000069_QD__TRIA_BUNKER__0$', duration=9195, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.add_buff(boxIds=[199], skillId=70000109, level=1, isPlayer=False, isSkillSet=False) # 초생회
        self.select_camera(triggerId=301, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003A')
        self.set_conversation(type=1, spawnId=1003, script='$52000069_QD__TRIA_BUNKER__1$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 차연출2(self.ctx)


class 차연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_Devlin_Appear_01.xml ')
        self.set_npc_emotion_sequence(spawnId=2001, sequenceName='AttackReady_A')
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프레이대사01(self.ctx)


class 프레이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=303, enable=True)
        self.set_npc_emotion_sequence(spawnId=2003, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11000119, illustId='Fray_serious', msg='$52000069_QD__TRIA_BUNKER__2$', duration=4000, align='center')
        self.set_scene_skip(state=대사스킵용01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 돌격(self.ctx)


class 대사스킵용01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 돌격(self.ctx)


class 돌격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.select_camera(triggerId=304, enable=True)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_agent(triggerIds=[8009], visible=False)
        self.set_agent(triggerIds=[8010], visible=False)
        self.set_agent(triggerIds=[8011], visible=False)
        self.set_agent(triggerIds=[8012], visible=False)
        self.set_agent(triggerIds=[8013], visible=False)
        self.set_agent(triggerIds=[8014], visible=False)
        self.set_agent(triggerIds=[8015], visible=False)
        self.set_agent(triggerIds=[8016], visible=False)
        self.set_agent(triggerIds=[8017], visible=False)
        self.set_agent(triggerIds=[8018], visible=False)
        self.set_agent(triggerIds=[8019], visible=False)
        self.set_agent(triggerIds=[8020], visible=False)
        self.set_agent(triggerIds=[8021], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 지원군대기(self.ctx)


class 지원군대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=304, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=20000):
            return 지원군등장(self.ctx)


class 지원군등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1201,1202,1203])
        self.destroy_monster(spawnIds=[2101,2102,2103])
        self.create_monster(spawnIds=[1004,1005,1301,1302,1303,1304], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 지원군연출(self.ctx)


class 지원군연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=1, spawnId=1004, script='$52000069_QD__TRIA_BUNKER__3$', arg4=4, arg5=0)
        self.set_conversation(type=1, spawnId=1005, script='$52000069_QD__TRIA_BUNKER__4$', arg4=4, arg5=0)
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004A')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005A')
        self.move_npc(spawnId=1301, patrolName='MS2PatrolData_1301A')
        self.move_npc(spawnId=1302, patrolName='MS2PatrolData_1302A')
        self.move_npc(spawnId=1303, patrolName='MS2PatrolData_1303A')
        self.move_npc(spawnId=1304, patrolName='MS2PatrolData_1304A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 임무종료대기(self.ctx)


class 임무종료대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_buff(boxId=199, skillId=70000107)
        self.select_camera(triggerId=305, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 데블린사망딜레이(self.ctx)


class 데블린사망딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return NPC교체(self.ctx)


class NPC교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000069, portalId=2)
        self.create_monster(spawnIds=[1006,1007,1009], animationEffect=False)
        self.destroy_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110])
        self.destroy_monster(spawnIds=[1003,1004,1005,1301,1302,1303,1304,2001,2101,2102,2103,2104,2105,2106,2107,2108])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에레브연출시작(self.ctx)


class 에레브연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=NPC교체2, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=306, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 에레브대사01(self.ctx)


class 에레브대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawnId=1000, sequenceName='Talk_A')
        self.set_sound(triggerId=90000, enable=True) # TriaAttack
        self.set_conversation(type=2, spawnId=11000075, script='$52000069_QD__TRIA_BUNKER__5$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 에레브대사02(self.ctx)


class 에레브대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000064, script='$52000069_QD__TRIA_BUNKER__6$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 에레브대사03(self.ctx)


class 에레브대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001975, script='$52000069_QD__TRIA_BUNKER__7$', arg4=4)
        self.set_onetime_effect(id=1991, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_02_00001991.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브대사04(self.ctx)


class 에레브대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=90000, enable=False) # TriaAttack
        self.add_cinematic_talk(npcId=11000075, illustId='Ereb_surprise', msg='$52000069_QD__TRIA_BUNKER__8$', duration=4000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드리아등장(self.ctx)


class 마드리아등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=True)
        self.select_camera(triggerId=307, enable=True)
        self.create_monster(spawnIds=[2000], animationEffect=False, animationDelay=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 방향전환(self.ctx)


class 방향전환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[609], visible=True)
        self.move_npc(spawnId=1006, patrolName='MS2PatrolData_1006A')
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1007A')
        # self.move_npc(spawnId=1008, patrolName='MS2PatrolData_1008A')
        self.move_npc(spawnId=1009, patrolName='MS2PatrolData_1009A')
        self.move_user_path(patrolName='MS2PatrolData_PCA')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 광역마법(self.ctx)


class 광역마법(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.move_npc(spawnId=2000, patrolName='MS2PatrolData_2000A')
        self.set_effect(triggerIds=[609], visible=True)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[605], visible=True)
        self.set_effect(triggerIds=[606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 처맞음(self.ctx)


class 처맞음(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_npc_emotion_sequence(spawnId=1006, sequenceName='Damg_A')
        self.set_npc_emotion_sequence(spawnId=1007, sequenceName='Damg_A')
        self.set_npc_emotion_sequence(spawnId=1009, sequenceName='Damg_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=250):
            return 쓰러짐(self.ctx)


class 쓰러짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=1006, sequenceName='Down_Idle_A', duration=1E+09)
        self.set_npc_emotion_loop(spawnId=1007, sequenceName='Down_Idle_A', duration=1E+09)
        # self.set_npc_emotion_loop(spawnId=1008, sequenceName='Down_Idle', duration=1E+09)
        self.set_npc_emotion_loop(spawnId=1009, sequenceName='Dead_Idle_A', duration=1E+09)
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=12000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 쓰러짐2(self.ctx)


class 쓰러짐2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1001,1002])
        self.select_camera(triggerId=309, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마드리아워킹(self.ctx)


class 마드리아워킹(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=308, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마드리아오버숄더(self.ctx)


class 마드리아오버숄더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__9$', arg4=7) # 대사
        self.set_onetime_effect(id=1992, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_03_00001992.xml')
        self.select_camera(triggerId=310, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 마드리아공격(self.ctx)


class 마드리아공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11000075, illustId='Ereb_serious', msg='$52000069_QD__TRIA_BUNKER__10$', duration=3000, align='center')
        self.select_camera(triggerId=311, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드리아공격2(self.ctx)


class 마드리아공격2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__11$', arg4=12) # 대사
        self.set_onetime_effect(id=1993, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_04_00001993.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12500):
            return 마드리아공격3(self.ctx)


class 마드리아공격3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__12$', arg4=11) # 대사
        self.set_onetime_effect(id=1994, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_05_00001994.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11200):
            return 마드리아공격4(self.ctx)


class 마드리아공격4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__13$', arg4=8) # 대사
        self.set_onetime_effect(id=1995, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_06_00001995.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8100):
            return 마드리아공격5(self.ctx)


class 마드리아공격5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=1000, sequenceName='Damg_A')
        self.select_camera(triggerId=315, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브각성(self.ctx)


class 에레브각성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[607], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 에레브각성2(self.ctx)


class 에레브각성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=1000, sequenceName='Damg_Idle_B', duration=1E+09)
        self.select_camera(triggerId=312, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마드리아놀람(self.ctx)


class 마드리아놀람(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=314, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라눈속임(self.ctx)


class 카메라눈속임(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=312, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 에레브버프2(self.ctx)


class 에레브버프2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=313, enable=True)
        self.set_npc_emotion_sequence(spawnId=1000, sequenceName='Spell_A')
        self.set_onetime_effect(id=2100287, enable=True, path='BG/Common/Sound/Eff_System_Chapter8_Destruction_of_Ereb_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 화이트아웃(self.ctx)


class 화이트아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[608], visible=True)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드리아대사01(self.ctx)


class 마드리아대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__14$', arg4=7) # 대사
        self.set_onetime_effect(id=1996, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_07_00001996.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 마드리아대사02(self.ctx)


class 마드리아대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__15$', arg4=3) # 대사
        self.set_onetime_effect(id=1997, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_08_00001997.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return NPC교체2(self.ctx)


class NPC교체2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.remove_buff(boxId=199, skillId=70000109)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[607], visible=False)
        self.set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        self.destroy_monster(spawnIds=[1000,1006,1007,1009,2000,1001,1002])
        self.move_user(mapId=52000069, portalId=2)
        self.create_monster(spawnIds=[1000,1006,1007,1010,1011,1001,1002,9999], animationEffect=False)
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(triggerId=91000, type='trigger', achieve='TriaSeigeClear')
        self.set_sound(triggerId=90000, enable=True) # TriaAttack
        self.select_camera(triggerId=313, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
