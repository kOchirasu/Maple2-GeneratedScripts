""" trigger/52000133_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,111,112])
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001599], questStates=[3]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001599], questStates=[2]):
            return 예민한아노스()
        if quest_user_detected(boxIds=[9000], questIds=[50001599], questStates=[1]):
            return 예민한아노스()
        if quest_user_detected(boxIds=[9000], questIds=[50001598], questStates=[3]):
            return 예민한아노스()
        if quest_user_detected(boxIds=[9000], questIds=[50001598], questStates=[2]):
            return 예민한아노스_연출준비()
        """
        <condition name="퀘스트유저를감지하면" arg1="9000" arg2="50001598" arg3="1"> 
                <transition state="예민한아노스"/>
            </condition>
        """
        if quest_user_detected(boxIds=[9000], questIds=[50001584], questStates=[2]):
            return 케이틀린첫만남()
        if quest_user_detected(boxIds=[9000], questIds=[50001584], questStates=[1]):
            return 케이틀린첫만남()
        if quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[3]):
            return 케이틀린첫만남()
        if quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[2]):
            return 케이틀린첫만남()
        if quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[1]):
            return 케이틀린첫만남()
        if quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[3]):
            return 케이틀린첫만남()
        if quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[2]):
            return 케이틀린첫만남_연출시작()
        if quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[1]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[3]):
            return 빈집()


class 케이틀린첫만남(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101])
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 케이틀린첫만남_연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        create_monster(spawnIds=[101])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000133, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 전경스케치01()


class 전경스케치01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전경스케치02()


class 전경스케치02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__0$', duration=2000, align='left')
        set_scene_skip(state=케이틀린첫만남_스킵완료, arg2='nextState') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전경스케치03()


class 전경스케치03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        move_user_path(patrolName='MS2PatrolData_PC01')
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전경스케치04()


class 전경스케치04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        add_cinematic_talk(npcId=11003254, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__1$', duration=3000, align='center')
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전경스케치05()


class 전경스케치05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        add_balloon_talk(spawnId=101, msg='$52000133_QD__MAIN__2$', duration=3000, delayTick=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Bore_A', duration=3000)
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전경스케치06()


class 전경스케치06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        move_user_path(patrolName='MS2PatrolData_PC02')
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전경스케치07()


class 전경스케치07(state.State):
    def on_enter(self):
        show_caption(type='NameCaption', title='$52000133_QD__MAIN__3$', desc='$52000133_QD__MAIN__4$', align='centerRight', offsetRateX=-0.05, offsetRateY=0.15, duration=10000, scale=2)
        set_npc_emotion_loop(spawnId=101, sequenceName='Bore_B', duration=4000)
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class 케이틀린첫만남_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        move_user(mapId=52000133, portalId=12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 예민한아노스(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111,113])
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 예민한아노스_연출준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000133, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 예민한아노스_연출시작()


class 예민한아노스_연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8100], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 케이틀린대사01()


class 케이틀린대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8101], returnView=False)
        add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__5$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=111, sequenceName='Bore_A', duration=4600)
        move_user_path(patrolName='2_MS2PatrolData_PC01')
        set_scene_skip(state=예민한아노스_스킵완료, arg2='nextState') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사01()


class PC대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8120], returnView=False)
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__6$', duration=3000)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=2000)
        move_user_path(patrolName='2_MS2PatrolData_PC02')
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린대사02()


class 케이틀린대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__7$', duration=3000, align='right')
        move_npc(spawnId=111, patrolName='2_MS2PatrolData_Katelyn01')
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사02()


class PC대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__8$', duration=3000, align='right')
        move_user_path(patrolName='2_MS2PatrolData_PC03')
        set_pc_emotion_loop(sequenceName='Talk_A', duration=2000)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린대사03()


class 케이틀린대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8110], returnView=False)
        create_monster(spawnIds=[112])
        add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__9$', duration=4000, align='right')
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=8200)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아노스걸어나옴()


class 아노스걸어나옴(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8140], returnView=False)
        add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__10$', duration=3000, align='left')
        move_npc(spawnId=112, patrolName='2_MS2PatrolData_Anos01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사01()


class 아노스대사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__11$', duration=3000, align='left')
        move_npc(spawnId=111, patrolName='2_MS2PatrolData_Katelyn02')
        set_npc_emotion_loop(spawnId=112, sequenceName='Talk_A', duration=3600)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사03()


class PC대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__12$', align='center', duration=3000)
        set_pc_emotion_loop(sequenceName='Emotion_Hello_A', duration=2000)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사02()


class 아노스대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__13$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=112, sequenceName='ChatUp_A', duration=7000)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사04()


class PC대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8131], returnView=False)
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__14$', duration=3000, align='right')
        set_pc_emotion_sequence(sequenceNames=['Emotion_Surprise_A'])
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사03()


class 아노스대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__15$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=112, sequenceName='Bore_A', duration=8100)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린대사04()


class 케이틀린대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8132], returnView=False)
        add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__16$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=12000)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사04()


class 아노스대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__17$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=112, sequenceName='Bore_B', duration=9500)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사05()


class 아노스대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8133], returnView=False)
        add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__18$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=112, sequenceName='Talk_A', duration=6300)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린대사05()


class 케이틀린대사05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__19$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=111, sequenceName='Bore_B', duration=7900)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린대사06()


class 케이틀린대사06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__20$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=6800)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사06()


class 아노스대사06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8140], returnView=False)
        add_cinematic_talk(npcId=11003259, illustId='Anos_serious', msg='$52000133_QD__MAIN__21$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=112, sequenceName='Bore_A', duration=5800)
        # <action name="스킵을설정한다" arg1="예민한아노스_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사07()


class 아노스대사07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8140], returnView=False)
        add_cinematic_talk(npcId=11003259, illustId='Anos_serious', msg='$52000133_QD__MAIN__22$', duration=3000, align='left')
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class 예민한아노스_스킵완료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[113])
        destroy_monster(spawnIds=[112])
        move_user(mapId=52000133, portalId=13)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 빈집(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


