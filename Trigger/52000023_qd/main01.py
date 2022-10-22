""" trigger/52000023_qd/main01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 종이문서 발견 사운드 이펙트
        set_effect(triggerIds=[6001], visible=False) # Ishura Voice 00001274
        set_effect(triggerIds=[6002], visible=False) # Ishura Voice 00001275
        set_effect(triggerIds=[6003], visible=False) # Ishura Voice 00001276
        set_effect(triggerIds=[6004], visible=False) # Ishura Voice 00001277
        set_effect(triggerIds=[6005], visible=False) # Ishura Voice 00001278
        set_effect(triggerIds=[6006], visible=False) # Ishura Voice 00001279
        set_effect(triggerIds=[6007], visible=False) # Ishura Voice 00001280
        set_effect(triggerIds=[6008], visible=False) # Ishura Voice 00001281
        set_effect(triggerIds=[6009], visible=False) # Ishura Voice 00001282
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8100], visible=False)
        set_agent(triggerIds=[8101], visible=False)
        set_agent(triggerIds=[8102], visible=False)
        set_agent(triggerIds=[8103], visible=False)
        set_agent(triggerIds=[8104], visible=False)
        set_agent(triggerIds=[8105], visible=False)
        set_agent(triggerIds=[8106], visible=False)
        set_agent(triggerIds=[8107], visible=False)
        set_agent(triggerIds=[8108], visible=False)
        set_agent(triggerIds=[8109], visible=False)
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000617], state=0)
        set_interact_object(triggerIds=[10000618], state=0)
        set_interact_object(triggerIds=[10000619], state=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[20002230], questStates=[1]):
            return 연출준비()


class 연출준비(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8100], visible=True)
        set_agent(triggerIds=[8101], visible=True)
        set_agent(triggerIds=[8102], visible=True)
        set_agent(triggerIds=[8103], visible=True)
        set_agent(triggerIds=[8104], visible=True)
        set_agent(triggerIds=[8105], visible=True)
        set_agent(triggerIds=[8106], visible=True)
        set_agent(triggerIds=[8107], visible=True)
        set_agent(triggerIds=[8108], visible=True)
        set_agent(triggerIds=[8109], visible=True)
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 유저이동01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 유저이동01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저이동02()


class 유저이동02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_100')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 유저이동03()


class 유저이동03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투준비01()


class 전투준비01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True) # Ishura Voice 00001274
        set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__0$', arg4=6, arg5=0) # 음성코드 	00001274
        set_skip(state=전투준비02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 전투준비02()

    def on_exit(self):
        remove_cinematic_talk()


class 전투준비02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=False) # Ishura Voice 00001274
        set_effect(triggerIds=[6002], visible=True) # Ishura Voice 00001275
        set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__1$', arg4=4, arg5=0) # 음성코드 	00001275
        set_skip(state=전투시작)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        remove_cinematic_talk()


class 전투시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=603, enable=False)
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8100], visible=False)
        set_agent(triggerIds=[8101], visible=False)
        set_agent(triggerIds=[8102], visible=False)
        set_agent(triggerIds=[8103], visible=False)
        set_agent(triggerIds=[8104], visible=False)
        set_agent(triggerIds=[8105], visible=False)
        set_agent(triggerIds=[8106], visible=False)
        set_agent(triggerIds=[8107], visible=False)
        set_agent(triggerIds=[8108], visible=False)
        set_agent(triggerIds=[8109], visible=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901,902,903,904,905,906,907,908,909,910]):
            return 대화준비01()


class 대화준비01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=False) # Ishura Voice 00001275
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대화준비02()


class 대화준비02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_200')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 대화준비03()


class 대화준비03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이슈라대화01()


class 이슈라대화01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=True) # Ishura Voice 00001276
        set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__2$', arg4=8, arg5=0) # 음성코드 	00001276
        set_skip(state=이슈라대화02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 이슈라대화02()

    def on_exit(self):
        remove_cinematic_talk()


class 이슈라대화02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=False) # Ishura Voice 00001276
        set_effect(triggerIds=[6004], visible=True) # Ishura Voice 00001277
        set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__3$', arg4=8, arg5=0) # 음성코드 	00001277
        set_skip(state=이슈라대화03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 이슈라대화03()

    def on_exit(self):
        remove_cinematic_talk()


class 이슈라대화03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6004], visible=False) # Ishura Voice 00001277
        set_effect(triggerIds=[6005], visible=True) # Ishura Voice 00001278
        set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__4$', arg4=7, arg5=0) # 음성코드 	00001278
        set_skip(state=이슈라대화04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 이슈라대화04()

    def on_exit(self):
        remove_cinematic_talk()


class 이슈라대화04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6005], visible=False) # Ishura Voice 00001278
        set_effect(triggerIds=[6006], visible=True) # Ishura Voice 00001279
        set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__5$', arg4=6, arg5=0) # 음성코드 	00001279
        set_skip(state=수색준비)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 수색준비()

    def on_exit(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 수색준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6006], visible=False) # Ishura Voice 00001279
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)
        set_interact_object(triggerIds=[10000617], state=1)
        set_interact_object(triggerIds=[10000618], state=1)
        set_interact_object(triggerIds=[10000619], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 수색시작()


class 수색시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=25200231, textId=25200231)
        move_npc(spawnId=103, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000617], arg2=0):
            return 수색종료01()

    def on_exit(self):
        set_effect(triggerIds=[5001], visible=True) # 종이문서 발견 사운드 이펙트
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0)


class 수색종료01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000618], state=0)
        set_interact_object(triggerIds=[10000619], state=0)
        hide_guide_summary(entityId=25200231)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 수색종료02()


class 수색종료02(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_104')
        set_effect(triggerIds=[6007], visible=True) # Ishura Voice 00001280
        set_conversation(type=1, spawnId=103, script='$52000023_QD__MAIN01__6$', arg4=3, arg5=0) # 음성코드 	00001280

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 정리준비01()


class 정리준비01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        select_camera(triggerId=604, enable=True)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9003, spawnIds=[103]):
            return 정리준비02()


class 정리준비02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6007], visible=False) # Ishura Voice 00001280

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리대화01()


class 정리대화01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6008], visible=True) # Ishura Voice 00001281
        set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__7$', arg4=9, arg5=0) # 음성코드 	00001281
        set_skip(state=정리대화02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 정리대화02()

    def on_exit(self):
        remove_cinematic_talk()


class 정리대화02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6008], visible=False) # Ishura Voice 00001281
        set_effect(triggerIds=[6009], visible=True) # Ishura Voice 00001282
        set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__8$', arg4=5, arg5=0) # 음성코드 	00001282
        set_skip(state=퇴장준비)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 퇴장준비()

    def on_exit(self):
        remove_cinematic_talk()


class 퇴장준비(state.State):
    def on_enter(self):
        select_camera(triggerId=604, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 퇴장중()


class 퇴장중(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='MeetAgain_Ishura')
        move_npc(spawnId=103, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9004, spawnIds=[103]):
            return 퇴장완료()

    def on_exit(self):
        destroy_monster(spawnIds=[103])


class 퇴장완료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6009], visible=False) # Ishura Voice 00001282


