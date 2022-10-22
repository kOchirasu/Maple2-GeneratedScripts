""" trigger/52000031_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3200], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101], jobCode=90):
            return 연출시작()
        if user_detected(boxIds=[101], jobCode=10):
            return 연출시작10()
        if user_detected(boxIds=[101], jobCode=1):
            return 연출시작10()
        if user_detected(boxIds=[101], jobCode=20):
            return 연출시작20()
        if user_detected(boxIds=[101], jobCode=30):
            return 연출시작30()
        if user_detected(boxIds=[101], jobCode=40):
            return 연출시작40()
        if user_detected(boxIds=[101], jobCode=50):
            return 연출시작50()
        if user_detected(boxIds=[101], jobCode=60):
            return 연출시작60()
        if user_detected(boxIds=[101], jobCode=70):
            return 연출시작50()
        if user_detected(boxIds=[101], jobCode=80):
            return 연출시작60()


class 연출시작(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001230, script='$52000031_QD__MAIN__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출시작10(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000076, script='$52000031_QD__MAIN__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출시작20(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001581, script='$52000031_QD__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출시작30(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[602], visible=True)
        set_conversation(type=2, spawnId=11000032, script='$52000031_QD__MAIN__3$', arg4=5, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출시작40(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001578, script='$52000031_QD__MAIN__4$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출시작50(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000015, script='$52000031_QD__MAIN__5$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출시작60(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001583, script='$52000031_QD__MAIN__6$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출시작70(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001586, script='$52000031_QD__MAIN__7$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 연출시작80(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001584, script='$52000031_QD__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 전투시작(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=False)
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 차전투2()

    def on_exit(self):
        destroy_monster(spawnIds=[2002])


class 차전투2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003,2004], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2003]):
            return 렌듀비앙대사02()

    def on_exit(self):
        destroy_monster(spawnIds=[2004])
        select_camera(triggerId=302, enable=False)


class 렌듀비앙대사02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3200], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115], visible=True, arg3=0, arg4=100, arg5=1)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True, arg3=0, arg4=100, arg5=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001230, script='$52000031_QD__MAIN__9$', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=11001244, script='$52000031_QD__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 유페리아대사_기타음성1()


class 유페리아대사_기타음성1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)
        set_conversation(type=2, spawnId=11001564, script='$52000031_QD__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 이슈라외침01()


class 이슈라외침01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_conversation(type=2, spawnId=11001244, script='$52000031_QD__MAIN__12$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            move_user(mapId=52000032, portalId=0)
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 종료(state.State):
    pass

