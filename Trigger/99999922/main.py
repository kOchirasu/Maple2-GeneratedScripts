""" trigger/99999922/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_sound(triggerId=99999, arg2=False)
        set_effect(triggerIds=[100000001], visible=False) # wall01 사라짐
        set_effect(triggerIds=[100000002], visible=False) # 다리 생성
        set_effect(triggerIds=[100000003], visible=False) # 다리 제거
        set_effect(triggerIds=[100000004], visible=False) # wall01 사라짐
        set_effect(triggerIds=[100000005], visible=False) # 다리 생성
        set_effect(triggerIds=[100000006], visible=False) # 다리 제거
        set_mesh(triggerIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1300,1301,1302,1303,1304,1305,1306,1307,1308], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1400], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1500], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[1000001,1000002,1000003,1000004,1000005,1000006], visible=False)
        set_agent(triggerIds=[1100001,1100002,1100003], visible=False)
        set_interact_object(triggerIds=[10000065], state=2)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1]):
            return 생성_1()


class 생성_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_1()


class 연출시작_1(state.State):
    def on_enter(self):
        select_camera(triggerId=2000001, enable=True)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대화_1()


class 대화_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=101, script='신입사원인가요?', arg4=5)
        set_skip(state=대화_1_스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대화_1_스킵()


class 대화_1_스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대화_2()


class 대화_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=101, script='반가워요.\n그럼 저를 따라와 보시겠어요??', arg4=3)
        set_skip(state=연출끝_1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대화_2_스킵()


class 대화_2_스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출끝_1()


class 연출끝_1(state.State):
    def on_enter(self):
        select_camera(triggerId=2000001, enable=False)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 돌사운드_1()

    def on_exit(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData0_101_1')
        set_mesh(triggerIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008], visible=False, arg3=2000, arg4=100, arg5=0)
        set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111], visible=True, arg3=5000, arg4=100, arg5=0)


class 돌사운드_1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='자경대장 오스칼과 함께 몬스터들을 처치하세요.', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다리사운드_1()

    def on_exit(self):
        set_effect(triggerIds=[100000001], visible=True) # wall01 사라짐


class 다리사운드_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 몬스터등장_1()

    def on_exit(self):
        set_effect(triggerIds=[100000002], visible=True) # 다리 생성


class 몬스터등장_1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1400], visible=False, arg3=1000, arg4=0, arg5=0)
        create_monster(spawnIds=[1001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저감지_2()


class 유저감지_2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2], jobCode=0):
            return 길막추가_1()


class 길막추가_1(state.State):
    def on_enter(self):
        set_agent(triggerIds=[1000001,1000002,1000003,1000004,1000005,1000006], visible=True)
        set_mesh(triggerIds=[1400], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return npc감지_1()


class npc감지_1(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 다리제거_1()


class 다리제거_1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111], visible=False, arg3=100, arg4=100, arg5=0)
        set_effect(triggerIds=[100000003], visible=True) # 다리 생성

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 몬스터사망_1()


class 몬스터사망_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001]):
            return 번째구역통로오픈3()

    def on_exit(self):
        set_event_ui(type=1, arg2='다리를 건너 마지막 몬스터를 처치하세요!', arg3='4000')


class 번째구역통로오픈3(state.State):
    def on_enter(self):
        set_agent(triggerIds=[1000001,1000002,1000003,1000004,1000005,1000006], visible=False)
        set_mesh(triggerIds=[1300,1301,1302,1303,1304,1305,1306,1307,1308], visible=False, arg3=2000, arg4=100, arg5=0)
        set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211], visible=True, arg3=4000, arg4=100, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 돌사운드_2()

    def on_exit(self):
        set_mesh(triggerIds=[1500], visible=False, arg3=5000, arg4=0, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData0_101_2')


class 돌사운드_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1800):
            return 다리사운드_2()

    def on_exit(self):
        set_effect(triggerIds=[100000004], visible=True) # wall01 사라짐


class 다리사운드_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1900):
            return 유저감지_3()

    def on_exit(self):
        set_effect(triggerIds=[100000005], visible=True) # 다리 생성


class 유저감지_3(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 길막추가_2()


class 길막추가_2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1500], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[1100001,1100002,1100003], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 다리제거_2()


class 다리제거_2(state.State):
    def on_enter(self):
        set_sound(triggerId=99999, arg2=True)
        create_monster(spawnIds=[1002], arg2=False)
        set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211], visible=False, arg3=100, arg4=100, arg5=0)
        set_effect(triggerIds=[100000006], visible=True) # 다리 제거

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 몬스터사망_2()


class 몬스터사망_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1002]):
            return 연출시작_2()


class 연출시작_2(state.State):
    def on_enter(self):
        set_sound(triggerId=99999, arg2=False)
        select_camera(triggerId=2000002, enable=True)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 레버생성_1()


class 레버생성_1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000065], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 대화_3()


class 대화_3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=101, script='저 스위치를 당겨야해요!', arg4=5)
        set_skip(state=대화_3_스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대화_3_스킵()


class 대화_3_스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출끝_2()


class 연출끝_2(state.State):
    def on_enter(self):
        select_camera(triggerId=2000002, enable=False)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 레버생성_1_완료()

    def on_exit(self):
        set_event_ui(type=1, arg2='생성된 스위치를 작동시키세요!', arg3='4000')


class 레버생성_1_완료(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000065], arg2=0):
            return 포탈생성()


class 포탈생성(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return NPC이동_2()


class NPC이동_2(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData0_101_3')
        set_conversation(type=1, spawnId=101, script='오예~끝났당~', arg4=3, arg5=7)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return npc감지_4()


class npc감지_4(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=4, spawnIds=[101]):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return None


