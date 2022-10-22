""" trigger/52000135_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102])
        set_mesh(triggerIds=[3000,3001], visible=False) # 아이노 크리스탈 on/off 컨트롤
        set_mesh_animation(triggerIds=[3000], visible=False) # 아이노 크리스탈 on/off 컨트롤
        set_interact_object(triggerIds=[10001175], state=1) # 아이노 크리스탈
        set_effect(triggerIds=[3010,3011,3012], visible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[1]):
            return 연출이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[3]):
            return 연출이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[2]):
            return 연출이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[1]):
            return 연출대기()


class 연출이후(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 연출대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000135, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아노스대사01()


class 아노스대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_01')
        add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__0$', duration=4000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=8500)
        set_scene_skip(state=오브젝트조사전_스킵완료, arg2='nextState') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아노스대사02()


class 아노스대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__1$', duration=4000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=6800)
        set_skip(state=아노스대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아노스대사03()


class 아노스대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아노스대사03()


class 아노스대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=True)
        add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__2$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='ChatUp_A', duration=5400)
        move_user_path(patrolName='MS2PatrolData_PC_03')
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오브젝트조사()


class 오브젝트조사전_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        move_user(mapId=52000135, portalId=10) # 퀘스트 시작 위치로 pc 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 오브젝트조사()


class 오브젝트조사(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001175], arg2=0):
            return 오브젝트반응이후()


class 오브젝트반응이후(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003,8004], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_mesh(triggerIds=[3000], visible=True) # 아이노 크리스탈 on
        set_mesh_animation(triggerIds=[3000], visible=True) # 아이노 크리스탈 on
        set_effect(triggerIds=[3011], visible=True)
        set_interact_object(triggerIds=[10001175], state=2)
        move_user_path(patrolName='MS2PatrolData_PC_0301')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아노스대사04()


class 아노스대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__3$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=7000)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0201')
        set_scene_skip(state=오브젝트조사후_스킵완료, arg2='nextState') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사05()


class 아노스대사05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__4$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=8300)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0202')
        set_skip(state=아노스대사05_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사06()


class 아노스대사05_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아노스대사06()


class 아노스대사06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__5$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=6500)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0203')
        set_skip(state=아노스대사06_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사07()


class 아노스대사06_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아노스대사07()


class 아노스대사07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__6$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=101, sequenceName='Chatup_A', duration=7900)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0204')
        set_skip(state=아노스대사07_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크리스탈끄기()


class 아노스대사07_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 크리스탈끄기()


class 크리스탈끄기(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0205')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 크리스탈꺼짐()


class 크리스탈꺼짐(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)
        set_mesh(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        set_mesh(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        set_mesh_animation(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        set_effect(triggerIds=[3011], visible=False)
        set_effect(triggerIds=[3012], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아노스대사08()


class 아노스대사08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__7$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=11000)
        set_effect(triggerIds=[3012], visible=False)
        set_skip(state=아노스대사08_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아시모프대사01()


class 아노스대사08_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아시모프대사01()


class 아시모프대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        add_cinematic_talk(npcId=11003250, illustId='0', msg='$52000135_QD__MAIN__8$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=5100)
        set_skip(state=아시모프대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사09()


class 아시모프대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아노스대사09()


class 아노스대사09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__9$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3800)
        move_user_path(patrolName='MS2PatrolData_PC_0302')
        set_skip(state=아노스대사09_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC크리스탈접근()


class 아노스대사09_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PC크리스탈접근()


class PC크리스탈접근(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000135_QD__MAIN__10$', duration=2000, align='right')
        set_pc_emotion_loop(sequenceName='Object_React_H', duration=1500)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=2000)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크리스탈켜짐()


class 크리스탈켜짐(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8011], returnView=False)
        set_mesh(triggerIds=[3001], visible=False) # 아이노 크리스탈 off-on
        set_mesh_animation(triggerIds=[3001], visible=False) # 아이노 크리스탈 off-on
        set_mesh(triggerIds=[3000], visible=True) # 아이노 크리스탈 off-on
        set_mesh_animation(triggerIds=[3000], visible=True) # 아이노 크리스탈 off-on
        set_effect(triggerIds=[3010], visible=True)
        add_balloon_talk(spawnId=0, msg='$52000135_QD__MAIN__11$', duration=3000, delayTick=1000)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Surprise_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마법사들접근()


class 마법사들접근(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8012], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_Asimov_05')
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_04')
        set_effect(triggerIds=[3011], visible=True)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Think_A'])
        add_balloon_talk(spawnId=101, msg='$52000135_QD__MAIN__12$', duration=2000, delayTick=100)
        add_balloon_talk(spawnId=102, msg='$52000135_QD__MAIN__13$', duration=2000, delayTick=500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아노스대사10()


class 아노스대사10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__14$', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3400)
        set_skip(state=아노스대사10_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사()


class 아노스대사10_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PC대사()


class PC대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000135_QD__MAIN__15$', duration=3000)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_06')
        set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크리스탈다시꺼짐()


class 크리스탈다시꺼짐(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_mesh(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        set_mesh_animation(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        set_mesh(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        set_mesh_animation(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        set_effect(triggerIds=[3010,3011], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아노스대사11()


class 아노스대사11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__16$', duration=5000, align='right')
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_07')
        set_skip(state=아노스대사11_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 아시모프대사02()


class 아노스대사11_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아시모프대사02()


class 아시모프대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        add_cinematic_talk(npcId=11003250, illustId='Asimov_normal', msg='$52000135_QD__MAIN__17$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=8600)
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class 오브젝트조사후_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        move_npc(spawnId=102, patrolName='MS2PatrolData_Asimov_05') # 아시모프 이동. 굳이 안 해도 될 것 같음
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_07') # 아노스 이동. 굳이 안 해도 될 것 같음
        set_mesh(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        set_mesh_animation(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        set_mesh(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        set_mesh_animation(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        set_effect(triggerIds=[3010,3011], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        set_achievement(triggerId=9000, type='trigger', achieve='Studyindarkness')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


