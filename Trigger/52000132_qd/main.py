""" trigger/52000132_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102])
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001599], questStates=[3]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001584], questStates=[2]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001584], questStates=[1]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[3]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[2]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[1]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[3]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[2]):
            return 아이들과만남_연출대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[1]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[3]):
            return 빈집()


class 아이들과만남_연출대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000132, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아이들과만남_연출시작()


class 아이들과만남_연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user_path(patrolName='MS2PatrolData_PC00')
        set_scene_skip(state=아이들과인사_스킵완료, arg2='exit') # setsceneskip set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리안인사01()


class 리안인사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__0$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=102, sequenceName='Bore_B', duration=4000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메린인사01()


class 메린인사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__1$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Bore_B', duration=6000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC인사01()


class PC인사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000132_QD__MAIN__2$', duration=3000, align='right')
        set_pc_emotion_loop(sequenceName='Talk_A', duration=3000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 리안대사01()


class 리안대사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__3$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메린대사01()


class 메린대사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__4$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Bore_C', duration=7000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 리안대사02()


class 리안대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__5$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=102, sequenceName='Bore_A', duration=3000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사02()


class PC대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000132_QD__MAIN__6$', duration=3000, align='right')
        set_pc_emotion_loop(sequenceName='Talk_A', duration=1000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 리안대사03()


class 리안대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__7$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=6000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메린대사02()


class 메린대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__8$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4500)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아이들이동01()


class 아이들이동01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        # <action name="유저를경로이동시킨다" arg1="MS2PatrolData_PC01"/>
        move_npc(spawnId=101, patrolName='MS2PatrolData_boy01')
        move_npc(spawnId=102, patrolName='MS2PatrolData_girl01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 유저이동01()


class 유저이동01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 리안대사04()


class 리안대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__9$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=7000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메린대사03()


class 메린대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__10$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=13000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 리안대사05()


class 리안대사05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__11$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4300)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아이들이동02()


class 아이들이동02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        # <action name="유저를경로이동시킨다" arg1="MS2PatrolData_PC01"/>
        move_npc(spawnId=101, patrolName='MS2PatrolData_boy02')
        move_npc(spawnId=102, patrolName='MS2PatrolData_girl02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 유저이동02()


class 유저이동02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 메린대사04()


class 메린대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__12$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=8900)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메린대사05()


class 메린대사05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__13$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4700)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사03()


class PC대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000132_QD__MAIN__14$', duration=3000, align='right')
        set_pc_emotion_loop(sequenceName='Talk_A', duration=2000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 리안대사06()


class 리안대사06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__15$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3200)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메린대사06()


class 메린대사06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__16$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=2000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아이들이동03()


class 아이들이동03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        # <action name="유저를경로이동시킨다" arg1="MS2PatrolData_PC01"/>
        move_npc(spawnId=101, patrolName='MS2PatrolData_boy03')
        move_npc(spawnId=102, patrolName='MS2PatrolData_girl03')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 유저이동03()


class 유저이동03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC03')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 메린대사07()


class 메린대사07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__17$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=7400)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 리안대사07()


class 리안대사07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__18$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3700)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메린대사08()


class 메린대사08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__19$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=2000)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아이들이동04()


class 아이들이동04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_boy04')
        move_npc(spawnId=102, patrolName='MS2PatrolData_girl04')
        move_user_path(patrolName='MS2PatrolData_PC04')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리안대사08()


class 리안대사08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006], returnView=False)
        add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__20$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3200)
        set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메린대사09()


class 메린대사09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__21$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아이들달림()


class 아이들달림(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_boy_run')
        move_npc(spawnId=102, patrolName='MS2PatrolData_girl_run')
        move_user_path(patrolName='MS2PatrolData_PC05')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아이들과인사()


class 아이들과인사(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC06')
        set_pc_emotion_sequence(sequenceNames=['Hello_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 방정리()


class 방정리(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        destroy_monster(spawnIds=[101,102])
        move_user_path(patrolName='MS2PatrolData_PC06')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저맵이동_연출종료()


class 유저맵이동_연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        destroy_monster(spawnIds=[101,102])
        move_user(mapId=52000132, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 빈집(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 아이들과인사_스킵완료(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=3)
        destroy_monster(spawnIds=[101,102])
        move_user(mapId=52000132, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=3)
        move_user(mapId=52000133, portalId=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


