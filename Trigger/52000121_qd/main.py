""" trigger/52000121_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[121,122,123,124,125,126,127,128,129,130,131], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001563], questStates=[1]):
            return 연출준비()
        if quest_user_detected(boxIds=[9000], questIds=[50001563], questStates=[2]):
            return 최종맵이동()


class 연출준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103,104], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 위기상황00()


class 위기상황00(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8000], returnView=False)
        set_scene_skip(state=전투직전_스킵완료, arg2='nextState') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return 위기상황01()


class 위기상황01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 위기상황02()


class 위기상황02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 위기상황03()


class 위기상황03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 위기상황04()


class 위기상황04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 대치상황시작()


class 대치상황시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 오스칼대사01()


class 오스칼대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003309, script='$52000121_QD__MAIN__0$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_B', duration=4000)
        set_skip(state=오스칼대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 투르카대사01()


class 오스칼대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 투르카대사01()


class 투르카대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__1$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Bore_B', duration=4000)
        set_skip(state=투르카대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 마노비치대사01()


class 투르카대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 마노비치대사01()


class 마노비치대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022], returnView=False)
        set_conversation(type=2, spawnId=11003308, script='$52000121_QD__MAIN__2$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)
        set_skip(state=마노비치대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카대사02()


class 마노비치대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 투르카대사02()


class 투르카대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8023], returnView=False)
        set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__3$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_skip(state=투르카대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카대사03()


class 투르카대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 투르카대사03()


class 투르카대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__4$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_skip(state=투르카대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오스칼대사02()


class 투르카대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 오스칼대사02()


class 오스칼대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8021], returnView=False)
        set_conversation(type=2, spawnId=11003309, script='$52000121_QD__MAIN__5$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Attack_Idle_A', duration=4000)
        set_skip(state=오스칼대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카대사04()


class 오스칼대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 투르카대사04()


class 투르카대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8023], returnView=False)
        set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__6$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        set_skip(state=투르카대사04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아르마노열폭준비()


class 투르카대사04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아르마노열폭준비()


class 아르마노열폭준비(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8025], returnView=False)
        face_emotion(spawnId=104, emotionName='Angry')
        # <action name="SetNpcEmotionLoop" arg1="104" arg2="Talk_A" arg3="1000"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아르마노열폭시작()


class 아르마노열폭시작(state.State):
    def on_enter(self):
        face_emotion(spawnId=104, emotionName='Angry')
        add_cinematic_talk(npcId=11003364, msg='$52000121_QD__MAIN__7$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아르마노달려()


class 아르마노달려(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8024], returnView=False)
        move_npc(spawnId=104, patrolName='MS2PatrolData_104_run')
        # <action name="NPC를이동시킨다" arg1="101" arg2="MS2PatrolData_101_Attack" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카공격00()


class 투르카공격00(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8030], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101_Attack')
        add_cinematic_talk(npcId=11003362, msg='$52000121_QD__MAIN__8$', duration=1000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카공격01()


class 투르카공격01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8031], returnView=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_02_B')
        set_npc_emotion_loop(spawnId=104, sequenceName='Run_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마노비치대사02()


class 마노비치대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Attack_Idle_A', duration=3000)
        add_cinematic_talk(npcId=11003308, msg='$52000121_QD__MAIN__9$', duration=1500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리셋대기01()


class 리셋대기01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,104])
        create_monster(spawnIds=[105,106], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 리셋대기02()


class 리셋대기02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8040], returnView=False)
        set_npc_emotion_loop(spawnId=105, sequenceName='Down_Idle_A', duration=30000)
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 잠시후()


class 잠시후(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8041], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 불효자멘붕()


class 불효자멘붕(state.State):
    def on_enter(self):
        face_emotion(spawnId=106, emotionName='Cry')
        add_cinematic_talk(npcId=11003364, msg='$52000121_QD__MAIN__10$', duration=1500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 오스칼멘붕()


class 오스칼멘붕(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=103, sequenceName='Stun_A', duration=3000)
        add_cinematic_talk(npcId=11003309, illustId='Oskhal_normal', msg='$52000121_QD__MAIN__11$', duration=2000, align='left')
        set_skip(state=오스칼멘붕_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 투르카대사05()


class 오스칼멘붕_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 투르카대사05()


class 투르카대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8035], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101_disappear_01')
        set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__12$', arg4=4, arg5=0)
        set_skip(state=투르카대사05_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PC등장대기()


class 투르카대사05_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PC등장대기()


class PC등장대기(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8036], returnView=False)
        move_user(mapId=52000121, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 투르카대사06()


class 투르카대사06(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_101_disappear_02')
        set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__13$', arg4=3, arg5=0)
        # <action name="스킵을설정한다" arg1="투르카대사06_skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC등장()


class PC등장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8034], returnView=False)
        move_user_path(patrolName='MS2PatrolData_PC_Run')
        move_npc(spawnId=101, patrolName='MS2PatrolData_101_disappear_04')
        set_conversation(type=1, spawnId=0, script='$52000121_QD__MAIN__14$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 투르카대사07()


class 투르카대사07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8036], returnView=False)
        # <action name="NPC를이동시킨다" arg1="101" arg2="MS2PatrolData_101_disappear_02" />
        set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__15$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카대사08()


class 투르카대사08(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_101_disappear_03')
        set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__16$', arg4=2, arg5=0)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 몬스터등장00()


class 몬스터등장00(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=True)
        destroy_monster(spawnIds=[101])
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터등장01()


class 몬스터등장01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8037], returnView=False)
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[110], arg2=True)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터등장02()


class 몬스터등장02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8038], returnView=False)
        create_monster(spawnIds=[108], arg2=True)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터등장03()


class 몬스터등장03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8039], returnView=False)
        create_monster(spawnIds=[112], arg2=True)
        set_skip()
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투대기01()


class 전투직전_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        select_camera_path(pathIds=[8036], returnView=False)
        destroy_monster(spawnIds=[101,102,103,104,105,106,108])
        create_monster(spawnIds=[105,106], arg2=False)
        create_monster(spawnIds=[108,110,111,112], arg2=True)
        move_user(mapId=52000121, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투대기01()


class 전투대기01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        # <action name="AddCinematicTalk" npcID="29000251" illustID="Oskhal_normal" msg="$52000121_QD__MAIN__17$" duration="2000" align="left" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투준비01()


class 전투준비01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[110,111,112]):
            return 전투시작02()


class 전투시작02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113,114,115], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[113,114,115]):
            return 전투끝()


class 전투끝(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8040], returnView=False)
        set_achievement(triggerId=9000, type='trigger', achieve='ManovichMobKill')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 암전02()


class 암전02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return npc교체01()


class npc교체01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[108])
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아빠와아들대기()


class 아빠와아들대기(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8040], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=마노비치리타이어_스킵완료, arg2='exit') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마노비치대사03()


class 마노비치대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__18$', arg4=2, arg5=0)
        set_skip(state=마노비치대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아르마노대사01()


class 마노비치대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아르마노대사01()


class 아르마노대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8042], returnView=False)
        set_conversation(type=2, spawnId=11003364, script='$52000121_QD__MAIN__19$', arg4=3, arg5=0)
        set_skip(state=아르마노대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아르마노대사02()


class 아르마노대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아르마노대사02()


class 아르마노대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003364, script='$52000121_QD__MAIN__20$', arg4=3, arg5=0)
        set_skip(state=아르마노대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마노비치대사04()


class 아르마노대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 마노비치대사04()


class 마노비치대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8041], returnView=False)
        set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__21$', arg4=3, arg5=0)
        set_skip(state=마노비치대사04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마노비치대사05()


class 마노비치대사04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 마노비치대사05()


class 마노비치대사05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__22$', arg4=3, arg5=0)
        set_skip(state=마노비치대사05_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마노비치대사06()


class 마노비치대사05_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 마노비치대사06()


class 마노비치대사06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8046], returnView=False)
        set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__23$', arg4=3, arg5=0)
        set_skip(state=마노비치대사06_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마노비치대사07()


class 마노비치대사06_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 마노비치대사07()


class 마노비치대사07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8043], returnView=False)
        set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__24$', arg4=2, arg5=0)
        set_npc_emotion_sequence(spawnId=105, sequenceName='Event_02_A')
        set_skip(state=마노비치대사07_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마노비치대사08()


class 마노비치대사07_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 마노비치대사08()


class 마노비치대사08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8047], returnView=False)
        set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__25$', arg4=2, arg5=0)
        # <action name="SetNpcEmotionSequence" arg1="105" arg2="Event_03_A"/>
        set_npc_emotion_loop(spawnId=105, sequenceName='Event_03_A', duration=10000)
        set_skip(state=마노비치대사08_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마노비치죽음()


class 마노비치대사08_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 마노비치죽음()


class 마노비치죽음(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8044], returnView=False)
        set_npc_emotion_sequence(spawnId=105, sequenceName='Event_04_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 아르마노오열()


class 아르마노오열(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8050], returnView=False)
        add_cinematic_talk(npcId=11003364, msg='$52000121_QD__MAIN__26$', duration=4000, align='left')
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료()


class 마노비치리타이어_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[108])
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=9000, type='trigger', achieve='ManovichRetire')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 최종맵이동(state.State):
    def on_enter(self):
        move_user(mapId=2000072, portalId=1)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


