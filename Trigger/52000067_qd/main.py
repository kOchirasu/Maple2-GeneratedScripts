""" trigger/52000067_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_time_scale(enable=False, startScale=1, endScale=1, duration=0, interpolator=0)
        self.reset_camera(interpolationTime=0)
        self.set_interact_object(triggerIds=[10001073], state=2)
        self.set_effect(triggerIds=[7005], visible=False) # mask_black
        self.set_effect(triggerIds=[7001], visible=False)
        # <action name="카메라경로를선택한다" arg1="8001" arg2="0"/>
        self.set_effect(triggerIds=[7010], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7011], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7012], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7013], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7014], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7015], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7016], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7110], visible=False) # 다크 포탈 폭발
        self.set_effect(triggerIds=[7111], visible=False) # 다크 포탈 폭발
        self.set_effect(triggerIds=[7112], visible=False) # 다크 포탈 폭발
        self.set_effect(triggerIds=[7113], visible=False) # 다크 포탈 폭발
        self.set_effect(triggerIds=[7114], visible=False) # 다크 포탈 폭발
        self.set_effect(triggerIds=[7115], visible=False) # 다크 포탈 폭발
        self.set_effect(triggerIds=[7116], visible=False) # 다크 포탈 폭발
        self.set_effect(triggerIds=[7301], visible=False) # 다크 포탈 생성음
        self.set_effect(triggerIds=[7302], visible=False) # 다크 포탈 생성음
        self.set_effect(triggerIds=[7303], visible=False) # 다크 포탈 생성음
        self.set_effect(triggerIds=[7304], visible=False) # 다크 포탈 생성음
        self.set_effect(triggerIds=[7305], visible=False) # 로봇 랜딩음
        self.set_effect(triggerIds=[7306], visible=False) # 데블린 워리어 등장음
        self.set_effect(triggerIds=[7307], visible=False) # 수리 음
        self.set_effect(triggerIds=[7308], visible=False) # 로봇 스파크 음
        self.set_effect(triggerIds=[7309], visible=False) # 로봇 움직임 음
        self.set_effect(triggerIds=[7310], visible=False) # 로봇 탑승 음
        self.set_effect(triggerIds=[7117], visible=False) # 감전
        self.set_actor(triggerId=4999, visible=False, initialSequence='Regen_A')
        self.set_actor(triggerId=4001, visible=False, initialSequence='Attack_02_H')
        self.set_actor(triggerId=4002, visible=False, initialSequence='Dead_Idle_A')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=52000067, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return ready(self.ctx)
        """
        <condition name="WaitTick" waitTick="3000" > 
                    <transition state="fadein"/>
            </condition>
        """


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[7005], visible=True) # mask_black
        self.set_cinematic_ui(type=9, script='$52000067_QD__MAIN__0$', arg3=False)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7005], visible=False) # mask_black
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.remove_buff(boxId=702, skillId=99910070)
        self.create_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119], animationEffect=True) # 다크윈드
        self.create_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514], animationEffect=True) # 침략자
        self.create_monster(spawnIds=[551,552,553,554,555], animationEffect=True)
        self.create_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536], animationEffect=True)
        self.create_monster(spawnIds=[121,121,123], animationEffect=False) # 블랙윈드 대원
        self.create_monster(spawnIds=[752,753,754], animationEffect=False) # 보디가드
        self.move_user_path(patrolName='MS2PatrolData_1002')
        self.select_camera_path(pathIds=[8001,8002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return portal_01(self.ctx)


class portal_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7301], visible=True) # 다크 포탈 생성음
        self.set_effect(triggerIds=[7010], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return portal_02(self.ctx)


class portal_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7302], visible=True) # 다크 포탈 생성음
        self.set_effect(triggerIds=[7016], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return portal_03(self.ctx)


class portal_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7303], visible=True) # 다크 포탈 생성음
        self.set_effect(triggerIds=[7013], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return portal_04(self.ctx)


class portal_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7304], visible=True) # 다크 포탈 생성음
        self.set_effect(triggerIds=[7012], visible=True) # 다크 포탈
        self.set_effect(triggerIds=[7014], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return portal_05(self.ctx)


class portal_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7015], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return portal_06(self.ctx)


class portal_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7011], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_03a(self.ctx)


class scene_03a(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__1$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03b(self.ctx)


class scene_03b(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1003')
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__2$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_03c(self.ctx)


class scene_03c(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2002')
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__3$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03c_02(self.ctx)


class scene_03c_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7305], visible=True) # 로봇 랜딩음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return scene_03d(self.ctx)


class scene_03d(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000067_QD__MAIN__22$', arg4=2, arg5=0)
        self.move_user_path(patrolName='MS2PatrolData_1004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4001, visible=True, initialSequence='Regen_A')
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_time_scale(enable=True, startScale=1, endScale=0.1, duration=2, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return scene_05_a(self.ctx)


class scene_05_a(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Jump_Damg_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1400):
            return scene_05_b(self.ctx)


class scene_05_b(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_05_d(self.ctx)


class scene_05_d(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.1, endScale=1, duration=1, interpolator=2) # 1초 뒤 복원
        self.select_camera_path(pathIds=[8099,8005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=False, startScale=1, endScale=1, duration=1, interpolator=0) # 종료
        self.select_camera_path(pathIds=[8005,8006], returnView=False)
        self.set_actor(triggerId=4001, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=False, startScale=0, endScale=0, duration=0, interpolator=0) # 1초 뒤 복원
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2003')
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__4$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006,8007], returnView=False)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__5$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__6$', arg4=3)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return fadeout(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.remove_buff(boxId=702, skillId=99910070)
        self.destroy_monster(spawnIds=[201])
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,123])
        self.destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514])
        self.destroy_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529,531,532,533,534,535,536,537,538,539])
        self.destroy_monster(spawnIds=[551,552,553,554,555,556,557,558,559])
        self.destroy_monster(spawnIds=[751,752,753,754,756,757,758,759,761,762])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Skip_2(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201])
        self.create_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119], animationEffect=True) # 다크윈드
        self.create_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514], animationEffect=True) # 침략자
        self.create_monster(spawnIds=[551,552,553,554,555], animationEffect=True)
        self.create_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536], animationEffect=True)
        self.create_monster(spawnIds=[121,121,123], animationEffect=False) # 블랙윈드 대원
        self.create_monster(spawnIds=[752,753,754], animationEffect=False) # 보디가드
        self.move_user_path(patrolName='MS2PatrolData_1002')
        self.select_camera_path(pathIds=[8001,8002], returnView=False)
        self.set_actor(triggerId=4001, visible=True, initialSequence='Regen_A')
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_effect(triggerIds=[7010], visible=True) # 다크 포탈
        self.set_effect(triggerIds=[7011], visible=True) # 다크 포탈
        self.set_effect(triggerIds=[7012], visible=True) # 다크 포탈
        self.set_effect(triggerIds=[7013], visible=True) # 다크 포탈
        self.set_effect(triggerIds=[7014], visible=True) # 다크 포탈
        self.set_effect(triggerIds=[7015], visible=True) # 다크 포탈
        self.set_effect(triggerIds=[7016], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2002')
        self.set_effect(triggerIds=[7005], visible=True) # mask_black
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2003')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200671, textId=25200671)
        self.set_mesh(triggerIds=[6004,6005], visible=True, arg3=0, delay=0, scale=10) # 투명 벽
        self.set_conversation(type=1, spawnId=201, script='$52000067_QD__MAIN__7$', arg4=3, arg5=2)
        self.set_interact_object(triggerIds=[10001073], state=1)
        self.set_actor(triggerId=4001, visible=False, initialSequence='Regen_A')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[7005], visible=False) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001073], stateValue=0):
            return play(self.ctx)


class play(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7310], visible=True) # 로봇 탑승 음
        self.hide_guide_summary(entityId=25200671)
        self.set_conversation(type=1, spawnId=201, script='$52000067_QD__MAIN__8$', arg4=3, arg5=0)
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005], visible=False, arg3=0, delay=0, scale=10) # 투명 벽
        self.set_interact_object(triggerIds=[10001073], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return GuideMission(self.ctx)
        if self.monster_dead(boxIds=[801,802,803,804,805,806,807]):
            return boss_event(self.ctx)


class GuideMission(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52000067_QD__MAIN__9$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[801,802,803,804,805,806,807]):
            return boss_event(self.ctx)


class boss_event(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[7005], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return boss_event_02(self.ctx)


class boss_event_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000067, portalId=2)
        self.set_effect(triggerIds=[7005], visible=False) # mask_black
        self.select_camera_path(pathIds=[8008,8009], returnView=False)
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,123])
        self.destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514])
        self.destroy_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529,531,532,533,534,535,536,537,538,539])
        self.destroy_monster(spawnIds=[551,552,553,554,555,556,557,558,559])
        self.destroy_monster(spawnIds=[801,802,803,804,805,806,807])
        # <action name="몬스터소멸시킨다" arg1="851,852,853,854,855,856,857,858,859,861,862,863,864,865,866,867" />
        self.destroy_monster(spawnIds=[751,752,753,754,756,757,758,759,761,762])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return boss_event_03(self.ctx)


class boss_event_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7306], visible=True) # 데블린 워리어 등장음
        self.create_monster(spawnIds=[999], animationEffect=True, animationDelay=5000)
        self.set_scene_skip(state=Skip_3, action='nextState')
        # <action name="액터를설정한다" arg1="4999" arg2="0" arg3="Regen_A" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return boss_event_04(self.ctx)


class boss_event_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010,8011], returnView=False)
        self.set_npc_emotion_sequence(spawnId=999, sequenceName='AttackReady_A')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return boss_event_05(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return boss_event_05(self.ctx)


class boss_event_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8012], returnView=False)
        self.set_effect(triggerIds=[7005], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return boss_event_06(self.ctx)


class boss_event_06(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[7005], visible=False) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return boss_event_07(self.ctx)


class boss_event_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[999]):
            return ending_ready(self.ctx)


class ending_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ending(self.ctx)


class ending(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_4, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[7005], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ending_02(self.ctx)


class ending_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[6300,6301,6302,6303,6304,6305,6306,6307,6308,6309,6310], visible=False)
        self.set_visible_breakable_object(triggerIds=[6311,6312,6313,6314,6315,6316,6317,6318,6319,6320,6321], visible=False)
        self.set_visible_breakable_object(triggerIds=[6322,6323,6324,6325,6326,6327,6328,6329,6330,6331], visible=False)
        self.remove_buff(boxId=702, skillId=99910070)
        self.set_cinematic_ui(type=9, script='$52000067_QD__MAIN__10$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_02_b(self.ctx)


class ending_02_b(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[851,852,853,854,855,856,857,858,859,860], animationEffect=True)
        self.create_monster(spawnIds=[861,862,863,864,865,866,867,868,869,870], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ending_03(self.ctx)


class ending_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7307], visible=True) # 수리 음
        self.set_conversation(type=1, spawnId=861, script='$52000067_QD__MAIN__11$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=853, script='$52000067_QD__MAIN__12$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=851, script='$52000067_QD__MAIN__13$', arg4=3, arg5=3)
        self.set_conversation(type=1, spawnId=861, script='$52000067_QD__MAIN__14$', arg4=3, arg5=4)
        self.set_conversation(type=1, spawnId=862, script='$52000067_QD__MAIN__15$', arg4=3, arg5=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8014,8015], returnView=False)
        self.set_effect(triggerIds=[7005], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return ending_04(self.ctx)


class ending_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7117], visible=True) # 감전 이펙트
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2003')
        self.move_user(mapId=52000067, portalId=3)
        self.set_actor(triggerId=4002, visible=True, initialSequence='Dead_Idle_A')
        self.set_effect(triggerIds=[7005], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_05(self.ctx)


class ending_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8016,8017], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_06(self.ctx)


class ending_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7308], visible=True) # 로봇 스파크 음
        self.set_effect(triggerIds=[7005], visible=False) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ending_07(self.ctx)


class ending_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__16$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ending_08(self.ctx)


class ending_08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__17$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ending_09(self.ctx)


class ending_09(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8018], returnView=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_09_b(self.ctx)


class ending_09_b(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ending_10(self.ctx)


class ending_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__18$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ending_11(self.ctx)


class ending_11(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2005')
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__19$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ending_12(self.ctx)


class ending_12(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__20$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ending_12_b(self.ctx)


class ending_12_b(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_13(self.ctx)


class ending_13(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_14(self.ctx)


class ending_14(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8019], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ending_15(self.ctx)


class ending_15(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__21$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ending_16(self.ctx)


class ending_16(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8020], returnView=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_1006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return ending_17(self.ctx)


class ending_17(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7309], visible=True) # 로봇 움직임 음
        self.set_actor(triggerId=4002, visible=True, initialSequence='Dead_Damg_A')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ending_18(self.ctx)


class Skip_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_achievement(triggerId=702, type='trigger', achieve='CityWarfareClear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end02(self.ctx)


class ending_18(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7005], visible=True) # mask_black
        self.set_achievement(triggerId=702, type='trigger', achieve='CityWarfareClear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end01(self.ctx)


class end01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.play_scene_movie(fileName='Aftermath_Madria.swf')
        self.set_scene_skip(state=end02, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return end02(self.ctx)


class end02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000055, portalId=1)


initial_state = idle
