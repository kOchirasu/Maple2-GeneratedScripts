""" trigger/52000067_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_time_scale(enable=False, startScale=1, endScale=1, duration=0, interpolator=0)
        reset_camera(interpolationTime=0)
        set_interact_object(triggerIds=[10001073], state=2)
        set_effect(triggerIds=[7005], visible=False) # mask_black
        set_effect(triggerIds=[7001], visible=False)
        # <action name="카메라경로를선택한다" arg1="8001" arg2="0"/>
        set_effect(triggerIds=[7010], visible=False) # 다크 포탈
        set_effect(triggerIds=[7011], visible=False) # 다크 포탈
        set_effect(triggerIds=[7012], visible=False) # 다크 포탈
        set_effect(triggerIds=[7013], visible=False) # 다크 포탈
        set_effect(triggerIds=[7014], visible=False) # 다크 포탈
        set_effect(triggerIds=[7015], visible=False) # 다크 포탈
        set_effect(triggerIds=[7016], visible=False) # 다크 포탈
        set_effect(triggerIds=[7110], visible=False) # 다크 포탈 폭발
        set_effect(triggerIds=[7111], visible=False) # 다크 포탈 폭발
        set_effect(triggerIds=[7112], visible=False) # 다크 포탈 폭발
        set_effect(triggerIds=[7113], visible=False) # 다크 포탈 폭발
        set_effect(triggerIds=[7114], visible=False) # 다크 포탈 폭발
        set_effect(triggerIds=[7115], visible=False) # 다크 포탈 폭발
        set_effect(triggerIds=[7116], visible=False) # 다크 포탈 폭발
        set_effect(triggerIds=[7301], visible=False) # 다크 포탈 생성음
        set_effect(triggerIds=[7302], visible=False) # 다크 포탈 생성음
        set_effect(triggerIds=[7303], visible=False) # 다크 포탈 생성음
        set_effect(triggerIds=[7304], visible=False) # 다크 포탈 생성음
        set_effect(triggerIds=[7305], visible=False) # 로봇 랜딩음
        set_effect(triggerIds=[7306], visible=False) # 데블린 워리어 등장음
        set_effect(triggerIds=[7307], visible=False) # 수리 음
        set_effect(triggerIds=[7308], visible=False) # 로봇 스파크 음
        set_effect(triggerIds=[7309], visible=False) # 로봇 움직임 음
        set_effect(triggerIds=[7310], visible=False) # 로봇 탑승 음
        set_effect(triggerIds=[7117], visible=False) # 감전
        set_actor(triggerId=4999, visible=False, initialSequence='Regen_A')
        set_actor(triggerId=4001, visible=False, initialSequence='Attack_02_H')
        set_actor(triggerId=4002, visible=False, initialSequence='Dead_Idle_A')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=52000067, portalId=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return ready()
        """
        <condition name="WaitTick" waitTick="3000" > 
                    <transition state="fadein"/>
            </condition>
        """


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[7005], visible=True) # mask_black
        set_cinematic_ui(type=9, script='$52000067_QD__MAIN__0$', arg3=False)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return start()


class start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7005], visible=False) # mask_black
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        remove_buff(boxId=702, skillId=99910070)
        create_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119], arg2=True) # 다크윈드
        create_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514], arg2=True) # 침략자
        create_monster(spawnIds=[551,552,553,554,555], arg2=True)
        create_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536], arg2=True)
        create_monster(spawnIds=[121,121,123], arg2=False) # 블랙윈드 대원
        create_monster(spawnIds=[752,753,754], arg2=False) # 보디가드
        move_user_path(patrolName='MS2PatrolData_1002')
        select_camera_path(pathIds=[8001,8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return portal_01()


class portal_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7301], visible=True) # 다크 포탈 생성음
        set_effect(triggerIds=[7010], visible=True) # 다크 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return portal_02()


class portal_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7302], visible=True) # 다크 포탈 생성음
        set_effect(triggerIds=[7016], visible=True) # 다크 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return portal_03()


class portal_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7303], visible=True) # 다크 포탈 생성음
        set_effect(triggerIds=[7013], visible=True) # 다크 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return portal_04()


class portal_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7304], visible=True) # 다크 포탈 생성음
        set_effect(triggerIds=[7012], visible=True) # 다크 포탈
        set_effect(triggerIds=[7014], visible=True) # 다크 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return portal_05()


class portal_05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7015], visible=True) # 다크 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return portal_06()


class portal_06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7011], visible=True) # 다크 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)
        move_npc(spawnId=201, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_03a()


class scene_03a(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__1$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03b()


class scene_03b(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1003')
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__2$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_03c()


class scene_03c(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2002')
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__3$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03c_02()


class scene_03c_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7305], visible=True) # 로봇 랜딩음

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return scene_03d()


class scene_03d(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000067_QD__MAIN__22$', arg4=2, arg5=0)
        move_user_path(patrolName='MS2PatrolData_1004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_actor(triggerId=4001, visible=True, initialSequence='Regen_A')
        set_effect(triggerIds=[7001], visible=True)
        set_time_scale(enable=True, startScale=1, endScale=0.1, duration=2, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return scene_05_a()


class scene_05_a(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Jump_Damg_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1400):
            return scene_05_b()


class scene_05_b(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_05_d()


class scene_05_d(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.1, endScale=1, duration=1, interpolator=2) # 1초 뒤 복원
        select_camera_path(pathIds=[8099,8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        set_time_scale(enable=False, startScale=1, endScale=1, duration=1, interpolator=0) # 종료
        select_camera_path(pathIds=[8005,8006], returnView=False)
        set_actor(triggerId=4001, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        set_time_scale(enable=False, startScale=0, endScale=0, duration=0, interpolator=0) # 1초 뒤 복원
        move_npc(spawnId=201, patrolName='MS2PatrolData_2003')
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__4$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006,8007], returnView=False)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__5$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_09()


class scene_09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__6$', arg4=3)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return fadeout()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        remove_buff(boxId=702, skillId=99910070)
        destroy_monster(spawnIds=[201])
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,123])
        destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514])
        destroy_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529,531,532,533,534,535,536,537,538,539])
        destroy_monster(spawnIds=[551,552,553,554,555,556,557,558,559])
        destroy_monster(spawnIds=[751,752,753,754,756,757,758,759,761,762])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Skip_2()


class Skip_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201])
        create_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119], arg2=True) # 다크윈드
        create_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514], arg2=True) # 침략자
        create_monster(spawnIds=[551,552,553,554,555], arg2=True)
        create_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536], arg2=True)
        create_monster(spawnIds=[121,121,123], arg2=False) # 블랙윈드 대원
        create_monster(spawnIds=[752,753,754], arg2=False) # 보디가드
        move_user_path(patrolName='MS2PatrolData_1002')
        select_camera_path(pathIds=[8001,8002], returnView=False)
        set_actor(triggerId=4001, visible=True, initialSequence='Regen_A')
        set_effect(triggerIds=[7001], visible=True)
        set_effect(triggerIds=[7010], visible=True) # 다크 포탈
        set_effect(triggerIds=[7011], visible=True) # 다크 포탈
        set_effect(triggerIds=[7012], visible=True) # 다크 포탈
        set_effect(triggerIds=[7013], visible=True) # 다크 포탈
        set_effect(triggerIds=[7014], visible=True) # 다크 포탈
        set_effect(triggerIds=[7015], visible=True) # 다크 포탈
        set_effect(triggerIds=[7016], visible=True) # 다크 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2002')
        set_effect(triggerIds=[7005], visible=True) # mask_black
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return fadein()


class fadein(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2003')
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25200671, textId=25200671)
        set_mesh(triggerIds=[6004,6005], visible=True, arg3=0, arg4=0, arg5=10) # 투명 벽
        set_conversation(type=1, spawnId=201, script='$52000067_QD__MAIN__7$', arg4=3, arg5=2)
        set_interact_object(triggerIds=[10001073], state=1)
        set_actor(triggerId=4001, visible=False, initialSequence='Regen_A')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[7005], visible=False) # mask_black

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001073], arg2=0):
            return play()


class play(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7310], visible=True) # 로봇 탑승 음
        hide_guide_summary(entityId=25200671)
        set_conversation(type=1, spawnId=201, script='$52000067_QD__MAIN__8$', arg4=3, arg5=0)
        set_mesh(triggerIds=[6001,6002,6003,6004,6005], visible=False, arg3=0, arg4=0, arg5=10) # 투명 벽
        set_interact_object(triggerIds=[10001073], state=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return GuideMission()
        if monster_dead(boxIds=[801,802,803,804,805,806,807]):
            return boss_event()


class GuideMission(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52000067_QD__MAIN__9$', arg3='3000')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[801,802,803,804,805,806,807]):
            return boss_event()


class boss_event(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[7005], visible=True) # mask_black

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return boss_event_02()


class boss_event_02(state.State):
    def on_enter(self):
        move_user(mapId=52000067, portalId=2)
        set_effect(triggerIds=[7005], visible=False) # mask_black
        select_camera_path(pathIds=[8008,8009], returnView=False)
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,123])
        destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514])
        destroy_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529,531,532,533,534,535,536,537,538,539])
        destroy_monster(spawnIds=[551,552,553,554,555,556,557,558,559])
        destroy_monster(spawnIds=[801,802,803,804,805,806,807])
        # <action name="몬스터소멸시킨다" arg1="851,852,853,854,855,856,857,858,859,861,862,863,864,865,866,867" />
        destroy_monster(spawnIds=[751,752,753,754,756,757,758,759,761,762])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return boss_event_03()


class boss_event_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7306], visible=True) # 데블린 워리어 등장음
        create_monster(spawnIds=[999], arg2=True, arg3=5000)
        set_scene_skip(state=Skip_3, arg2='nextState')
        # <action name="액터를설정한다" arg1="4999" arg2="0" arg3="Regen_A" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return boss_event_04()


class boss_event_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010,8011], returnView=False)
        set_npc_emotion_sequence(spawnId=999, sequenceName='AttackReady_A')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return boss_event_05()


class Skip_3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return boss_event_05()


class boss_event_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8012], returnView=False)
        set_effect(triggerIds=[7005], visible=True) # mask_black

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return boss_event_06()


class boss_event_06(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[7005], visible=False) # mask_black

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return boss_event_07()


class boss_event_07(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[999]):
            return ending_ready()


class ending_ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ending()


class ending(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_4, arg2='exit')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[7005], visible=True) # mask_black

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ending_02()


class ending_02(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[6300,6301,6302,6303,6304,6305,6306,6307,6308,6309,6310], arg2=False)
        set_visible_breakable_object(triggerIds=[6311,6312,6313,6314,6315,6316,6317,6318,6319,6320,6321], arg2=False)
        set_visible_breakable_object(triggerIds=[6322,6323,6324,6325,6326,6327,6328,6329,6330,6331], arg2=False)
        remove_buff(boxId=702, skillId=99910070)
        set_cinematic_ui(type=9, script='$52000067_QD__MAIN__10$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ending_02_b()


class ending_02_b(state.State):
    def on_enter(self):
        create_monster(spawnIds=[851,852,853,854,855,856,857,858,859,860], arg2=True)
        create_monster(spawnIds=[861,862,863,864,865,866,867,868,869,870], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ending_03()


class ending_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7307], visible=True) # 수리 음
        set_conversation(type=1, spawnId=861, script='$52000067_QD__MAIN__11$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=853, script='$52000067_QD__MAIN__12$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=851, script='$52000067_QD__MAIN__13$', arg4=3, arg5=3)
        set_conversation(type=1, spawnId=861, script='$52000067_QD__MAIN__14$', arg4=3, arg5=4)
        set_conversation(type=1, spawnId=862, script='$52000067_QD__MAIN__15$', arg4=3, arg5=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8014,8015], returnView=False)
        set_effect(triggerIds=[7005], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return ending_04()


class ending_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7117], visible=True) # 감전 이펙트
        move_npc(spawnId=201, patrolName='MS2PatrolData_2003')
        move_user(mapId=52000067, portalId=3)
        set_actor(triggerId=4002, visible=True, initialSequence='Dead_Idle_A')
        set_effect(triggerIds=[7005], visible=True) # mask_black

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ending_05()


class ending_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8016,8017], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ending_06()


class ending_06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7308], visible=True) # 로봇 스파크 음
        set_effect(triggerIds=[7005], visible=False) # mask_black

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ending_07()


class ending_07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__16$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ending_08()


class ending_08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__17$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ending_09()


class ending_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8018], returnView=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ending_09_b()


class ending_09_b(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ending_10()


class ending_10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__18$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ending_11()


class ending_11(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2005')
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__19$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ending_12()


class ending_12(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__20$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ending_12_b()


class ending_12_b(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ending_13()


class ending_13(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ending_14()


class ending_14(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8019], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ending_15()


class ending_15(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001897, script='$52000067_QD__MAIN__21$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ending_16()


class ending_16(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8020], returnView=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_1006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return ending_17()


class ending_17(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7309], visible=True) # 로봇 움직임 음
        set_actor(triggerId=4002, visible=True, initialSequence='Dead_Damg_A')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ending_18()


class Skip_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_achievement(triggerId=702, type='trigger', achieve='CityWarfareClear')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end02()


class ending_18(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7005], visible=True) # mask_black
        set_achievement(triggerId=702, type='trigger', achieve='CityWarfareClear')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end01()


class end01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        play_scene_movie(fileName='Aftermath_Madria.swf')
        set_scene_skip(state=end02, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return end02()


class end02(state.State):
    def on_enter(self):
        move_user(mapId=52000055, portalId=1)


