""" trigger/52000026_qd/seperategroup_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=False) # TriaAttack
        set_effect(triggerIds=[5000], visible=False) # LeftDoorOpen
        set_effect(triggerIds=[5001], visible=False) # LeftDoorClose
        set_effect(triggerIds=[5002], visible=False) # RightDoorOpen
        set_effect(triggerIds=[5003], visible=False) # RightDoorClose
        set_effect(triggerIds=[5004], visible=False) # blastjump
        set_effect(triggerIds=[6001], visible=False) # Asimov Voice 00000553 / everytime
        set_effect(triggerIds=[6002], visible=False) # Asimov Voice 00001338 / everytime
        set_effect(triggerIds=[6003], visible=False) # Asimov Voice 00001339 / everytime
        set_effect(triggerIds=[6004], visible=False) # Asimov Voice 00001340 / everytime
        set_effect(triggerIds=[6005], visible=False) # Asimov Voice 00001341 / in case RuneBlader, Berserker, Priest, Wizard
        set_effect(triggerIds=[6006], visible=False) # Asimov Voice 00001342 / in case RuneBlader, Wizard
        set_effect(triggerIds=[6007], visible=False) # Asimov Voice 00000561 / in case Berserker
        set_effect(triggerIds=[6101], visible=False) # Ishura Voice 00001291 / only RB
        set_effect(triggerIds=[6102], visible=False) # Ishura Voice 00001292 / everytime
        set_effect(triggerIds=[6103], visible=False) # Ishura Voice 00001293 / only RB
        set_effect(triggerIds=[6104], visible=False) # Ishura Voice 00001155 / in case Assassin, Berserker, Heavygunner, Knight, Priest, Ranger, Thief, Wizard
        set_effect(triggerIds=[6105], visible=False) # Ishura Voice 00001159 / in case Assassin, Berserker, Heavygunner, Knight, Priest, Ranger, Thief, Wizard

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[20002241], questStates=[1], jobCode=90):
            return 연출준비01()


class 연출준비01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=3000, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출준비02()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출준비02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저이동01()


class 유저이동01(state.State):
    def on_enter(self):
        select_camera(triggerId=3001, enable=True)
        move_user_path(patrolName='MS2PatrolData_2000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 차입장01_1()


class 차입장01_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,201], arg2=True)
        set_effect(triggerIds=[5000], visible=True) # LeftDoorOpen
        move_user_path(patrolName='MS2PatrolData_2001')
        select_camera(triggerId=3002, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차입장02_1()


class 차입장02_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # LeftDoorClose
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        select_camera_path(pathIds=[3003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차입장03_1()


class 차입장03_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000601, script='$52000026_QD__SEPERATEGROUP_01__0$', arg4=4, arg5=0)
        set_skip(state=차입장01_2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차입장01_2()


class 차입장01_2(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[5002], visible=True) # RightDoorOpen
        select_camera(triggerId=3100, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차입장02_2()


class 차입장02_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301], arg2=True)
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        move_user_path(patrolName='MS2PatrolData_2002')
        set_effect(triggerIds=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차입장03_2()


class 차입장03_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=True)
        move_npc(spawnId=401, patrolName='MS2PatrolData_401')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차입장04_2()


class 차입장04_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6101], visible=True) # Ishura Voice 00001291
        set_conversation(type=2, spawnId=11001244, script='$52000026_QD__SEPERATEGROUP_01__1$', arg4=6, arg5=0) # 음성 코드 00001291
        set_skip(state=차입장05_2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 차입장05_2()


class 차입장05_2(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[6101], visible=False) # Ishura Voice 00001291
        move_npc(spawnId=301, patrolName='MS2PatrolData_302')
        move_npc(spawnId=401, patrolName='MS2PatrolData_402')
        move_user_path(patrolName='MS2PatrolData_2003')
        select_camera(triggerId=3101, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차입장01_3()


class 차입장01_3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # RightDoorOpen
        create_monster(spawnIds=[501], arg2=True)
        move_npc(spawnId=501, patrolName='MS2PatrolData_501')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차입장02_3()


class 차입장02_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[601], arg2=True)
        move_npc(spawnId=601, patrolName='MS2PatrolData_601')
        set_effect(triggerIds=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차입장03_3()


class 차입장03_3(state.State):
    def on_enter(self):
        select_camera(triggerId=3102, enable=True)
        set_effect(triggerIds=[6001], visible=True) # Asimov Voice 00000553
        set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_01__2$', arg4=7, arg5=0) # 음성 코드 00000553
        set_skip(state=차입장01_4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 차입장01_4()


class 차입장01_4(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[6001], visible=False) # Asimov Voice 00000553
        select_camera(triggerId=3200, enable=True)
        set_effect(triggerIds=[5002], visible=True) # RightDoorOpen

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차입장02_4()


class 차입장02_4(state.State):
    def on_enter(self):
        select_camera(triggerId=3210, enable=True)
        create_monster(spawnIds=[701], arg2=True)
        move_npc(spawnId=701, patrolName='MS2PatrolData_701')
        set_effect(triggerIds=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차입장03_4()


class 차입장03_4(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001581, script='$52000026_QD__SEPERATEGROUP_01__3$', arg4=4, arg5=0)
        set_skip(state=차입장04_4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차입장04_4()


class 차입장04_4(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=3201, enable=True)
        create_monster(spawnIds=[801], arg2=True)
        move_npc(spawnId=801, patrolName='MS2PatrolData_801')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차입장05_4()


class 차입장05_4(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000076, script='$52000026_QD__SEPERATEGROUP_01__4$', arg4=4, arg5=0)
        set_skip(state=차입장06_4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차입장06_4()


class 차입장06_4(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차입장01_5()


class 차입장01_5(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True) # blastjump

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차입장02_5()


class 차입장02_5(state.State):
    def on_enter(self):
        move_npc(spawnId=701, patrolName='MS2PatrolData_702')
        select_camera(triggerId=3300, enable=True)
        create_monster(spawnIds=[901], arg2=True)
        move_npc(spawnId=901, patrolName='MS2PatrolData_901')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차입장03_5()


class 차입장03_5(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001583, script='$52000026_QD__SEPERATEGROUP_01__5$', arg4=3, arg5=0)
        set_skip(state=차입장04_5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차입장04_5()


class 차입장04_5(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=3301, enable=True)
        create_monster(spawnIds=[1001], arg2=True)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차입장05_5()


class 차입장05_5(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001584, script='$52000026_QD__SEPERATEGROUP_01__6$', arg4=4, arg5=0)
        set_skip(state=차입장06_5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차입장06_5()


class 차입장06_5(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=3302, enable=True)
        create_monster(spawnIds=[1101], arg2=True)
        move_npc(spawnId=1101, patrolName='MS2PatrolData_1101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차입장07_5()


class 차입장07_5(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000015, script='$52000026_QD__SEPERATEGROUP_01__7$', arg4=3, arg5=0)
        set_skip(state=차입장08_5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차입장08_5()


class 차입장08_5(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[5002], visible=True) # RightDoorOpen
        select_camera(triggerId=3303, enable=True)
        create_monster(spawnIds=[1201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차입장09_5()


class 차입장09_5(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True) # RightDoorClose
        move_npc(spawnId=1201, patrolName='MS2PatrolData_1201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 차입장10_5()


class 차입장10_5(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001586, script='$52000026_QD__SEPERATEGROUP_01__8$', arg4=3, arg5=0)
        set_skip(state=차입장11_5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차입장11_5()


class 차입장11_5(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=3304, enable=True)
        move_npc(spawnId=801, patrolName='MS2PatrolData_802')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차입장12_5()


class 차입장12_5(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000076, script='$52000026_QD__SEPERATEGROUP_01__9$', arg4=3, arg5=0)
        set_skip(state=입장완료01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 입장완료01()


class 입장완료01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_sound(triggerId=10000, arg2=True) # TriaAttack
        select_camera_path(pathIds=[3400,3401,3402,3403], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정렬01()


class 정렬01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True) # Asimov Voice 00001338
        set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_01__10$', arg4=5, arg5=0) # 음성 코드 00001338
        set_skip(state=정렬02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 정렬02()


class 정렬02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        move_npc(spawnId=501, patrolName='MS2PatrolData_502')
        move_npc(spawnId=601, patrolName='MS2PatrolData_602')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정렬03()


class 정렬03(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1002')
        move_npc(spawnId=1201, patrolName='MS2PatrolData_1202')
        move_npc(spawnId=901, patrolName='MS2PatrolData_902')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정렬04()


class 정렬04(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2004')
        move_npc(spawnId=301, patrolName='MS2PatrolData_303')
        move_npc(spawnId=401, patrolName='MS2PatrolData_403')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정렬05()


class 정렬05(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        move_npc(spawnId=201, patrolName='MS2PatrolData_203')
        move_npc(spawnId=1101, patrolName='MS2PatrolData_1102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정렬06()


class 정렬06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=False) # Asimov Voice 00001338
        move_npc(spawnId=701, patrolName='MS2PatrolData_703')
        move_npc(spawnId=801, patrolName='MS2PatrolData_803')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 본론01()


class 본론01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=True) # Asimov Voice 00001339
        set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_01__11$', arg4=10, arg5=0) # 음성 코드 00001339
        set_skip(state=본론02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 본론02()


class 본론02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 본론03()


class 본론03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=False) # Asimov Voice 00001339
        set_effect(triggerIds=[6004], visible=True) # Asimov Voice 00001340
        set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_01__12$', arg4=6, arg5=0) # 음성 코드 00001340
        set_skip(state=본론04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 본론04()


class 본론04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[6004], visible=False) # Asimov Voice 00001340
        select_camera(triggerId=3500, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 본론05()


class 본론05(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='MS2PatrolData_304')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 본론06()


class 본론06(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2005')
        move_npc(spawnId=401, patrolName='MS2PatrolData_404')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 본론07()


class 본론07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6102], visible=True) # Ishura Voice 00001292
        set_conversation(type=2, spawnId=11001244, script='$52000026_QD__SEPERATEGROUP_01__13$', arg4=5, arg5=0) # 음성 코드 00001292
        set_skip(state=영상01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 영상01()


class 영상01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_effect(triggerIds=[6102], visible=False) # Ishura Voice 00001292

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 영상02()


class 영상02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Royal_IshuraRemember.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상03()


class 영상03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 영상04()


class 영상04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정리01()


class 정리01(state.State):
    def on_enter(self):
        select_camera(triggerId=3600, enable=True)
        set_effect(triggerIds=[6103], visible=True) # Ishura Voice 00001293
        set_conversation(type=2, spawnId=11001244, script='$52000026_QD__SEPERATEGROUP_01__14$', arg4=8, arg5=0) # 음성 코드 00001293
        set_skip(state=정리02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 정리02()


class 정리02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[6103], visible=False) # Ishura Voice 00001293

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 반대01()


class 반대01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000076, script='$52000026_QD__SEPERATEGROUP_01__15$', arg4=4, arg5=0)
        set_skip(state=반대02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 반대02()


class 반대02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=3601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 반대03()


class 반대03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001586, script='$52000026_QD__SEPERATEGROUP_01__16$', arg4=4, arg5=0)
        set_skip(state=반대04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 반대04()


class 반대04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        move_npc(spawnId=1201, patrolName='MS2PatrolData_1203')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 반대05()


class 반대05(state.State):
    def on_enter(self):
        select_camera(triggerId=3602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 반대06()


class 반대06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001584, script='$52000026_QD__SEPERATEGROUP_01__17$', arg4=4, arg5=0)
        set_skip(state=반대07)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 반대07()


class 반대07(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1003')
        select_camera(triggerId=3603, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 반대08()


class 반대08(state.State):
    def on_enter(self):
        select_camera(triggerId=3604, enable=True)
        set_conversation(type=2, spawnId=11000015, script='$52000026_QD__SEPERATEGROUP_01__18$', arg4=4, arg5=0)
        set_skip(state=반대09)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 반대09()


class 반대09(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        destroy_monster(spawnIds=[1201,1001])
        move_npc(spawnId=1101, patrolName='MS2PatrolData_1103')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 반대10()


class 반대10(state.State):
    def on_enter(self):
        move_npc(spawnId=901, patrolName='MS2PatrolData_903')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 요약01()


class 요약01(state.State):
    def on_enter(self):
        select_camera(triggerId=3700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 요약02()


class 요약02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1101,901])
        set_conversation(type=2, spawnId=11000601, script='$52000026_QD__SEPERATEGROUP_01__19$', arg4=3, arg5=0)
        set_skip(state=요약03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 요약03()


class 요약03(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 요약04()


class 요약04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000601, script='$52000026_QD__SEPERATEGROUP_01__20$', arg4=4, arg5=0)
        set_skip(state=요약05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 요약05()


class 요약05(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=3800, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 요약06()


class 요약06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6005], visible=True) # Asimov Voice 00001341
        set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_01__21$', arg4=9, arg5=0) # 음성 코드 00001341
        set_skip(state=요약07)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 요약07()


class 요약07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6005], visible=False) # Asimov Voice 00001341
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 요약08()


class 요약08(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6006], visible=True) # Asimov Voice 00001342
        set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_01__22$', arg4=4, arg5=0) # 음성 코드 00001342
        set_skip(state=연출종료01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료01()


class 연출종료01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[6006], visible=False) # Asimov Voice 00001342
        select_camera(triggerId=3801, enable=True)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출종료02()


class 연출종료02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=3801, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 업적발생()


class 업적발생(state.State):
    def on_enter(self):
        set_achievement(triggerId=9001, type='trigger', achieve='SeperateGroup')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 강제퇴장()


class 강제퇴장(state.State):
    def on_enter(self):
        move_user(mapId=2000001, portalId=17, boxId=9001)

    def on_exit(self):
        set_sound(triggerId=10000, arg2=False) # TriaAttack


