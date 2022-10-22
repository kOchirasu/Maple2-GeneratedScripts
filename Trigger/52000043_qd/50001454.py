""" trigger/52000043_qd/50001454.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[608], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[1]):
            destroy_monster(spawnIds=[1003,2003])
            return 시작조건()
        if quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[2]):
            destroy_monster(spawnIds=[1003,2003])
            return 종료()
        if quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[3]):
            destroy_monster(spawnIds=[1003,2003])
            return 종료()


class 시작조건(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003,2003], arg2=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001020], state=2)
        set_interact_object(triggerIds=[10001021], state=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=305, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003D')
        move_user_path(patrolName='MS2PatrolData_PCD')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 말퉁선대사01()


class 말퉁선대사01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1003, script='$52000043_QD__50001454__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC이동02()


class NPC이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003E')
        move_user_path(patrolName='MS2PatrolData_PCE')
        move_npc(spawnId=2003, patrolName='MS2PatrolData_2003D')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=105, spawnIds=[2003]):
            return 준타대사01()


class 준타대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__1$', arg4=4)
        set_skip(state=준타대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 틴차이대사01()


class 준타대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사01()


class 틴차이대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001454__2$', arg4=4)
        set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 준타대사02()


class 틴차이대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사02()


class 준타대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=True)
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__3$', arg4=4)
        set_skip(state=준타대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 준타대사03()


class 준타대사02스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사03()


class 준타대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__4$', arg4=5)
        set_skip(state=준타대사03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 틴차이대사02()


class 준타대사03스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사02()


class 틴차이대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[607], visible=True)
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001454__5$', arg4=3)
        set_skip(state=틴차이대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준타대사04()


class 틴차이대사02스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[607], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사04()


class 준타대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__6$', arg4=3)
        set_skip(state=준타대사04스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준타대사05()


class 준타대사04스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사05()


class 준타대사05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__7$', arg4=5)
        set_skip(state=준타대사05스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 준타대사06()


class 준타대사05스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사06()


class 준타대사06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__8$', arg4=5)
        set_skip(state=준타대사06스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 준타대사07()


class 준타대사06스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사07()


class 준타대사07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__9$', arg4=6)
        set_skip(state=준타대사07스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 준타대사08()


class 준타대사07스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사08()


class 준타대사08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__10$', arg4=3)
        set_skip(state=준타대사08스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 틴차이대사03()


class 준타대사08스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사03()


class 틴차이대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001454__26$', arg4=2)
        set_skip(state=틴차이대사03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 준타대사09()


class 틴차이대사03스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사09()


class 준타대사09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__11$', arg4=4)
        set_skip(state=준타대사09스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 준타대사10()


class 준타대사09스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사10()


class 준타대사10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__12$', arg4=4)
        set_skip(state=준타대사10스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 준타대사11()


class 준타대사10스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사11()


class 준타대사11(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__13$', arg4=4)
        set_skip(state=준타대사11스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 틴차이대사04()


class 준타대사11스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사04()


class 틴차이대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001454__14$', arg4=2)
        set_skip(state=틴차이대사04스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 준타대사12()


class 틴차이대사04스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사12()


class 준타대사12(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__15$', arg4=4)
        set_skip(state=준타대사12스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 준타대사13()


class 준타대사12스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사13()


class 준타대사13(state.State):
    def on_enter(self):
        set_effect(triggerIds=[608], visible=True)
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__16$', arg4=4)
        set_skip(state=준타대사13스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PC이동()


class 준타대사13스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[608], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PC이동()


class PC이동(state.State):
    def on_enter(self):
        select_camera(triggerId=306, enable=True)
        move_user_path(patrolName='MS2PatrolData_PCG')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 준타대사14()


class 준타대사14(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__17$', arg4=4)
        set_skip(state=준타대사14스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 틴차이대사05()


class 준타대사14스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사05()


class 틴차이대사05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001454__18$', arg4=2)
        set_skip(state=틴차이대사05스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 준타대사15()


class 틴차이대사05스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사15()


class 준타대사15(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__19$', arg4=6)
        set_skip(state=준타대사15스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 준타대사16()


class 준타대사15스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사16()


class 준타대사16(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__20$', arg4=3)
        set_skip(state=준타대사16스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준타대사17()


class 준타대사16스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사17()


class 준타대사17(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__21$', arg4=4)
        set_skip(state=준타대사17스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 틴차이대사06()


class 준타대사17스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사06()


class 틴차이대사06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001454__22$', arg4=3)
        set_skip(state=틴차이대사06스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준타대사18()


class 틴차이대사06스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사18()


class 준타대사18(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__23$', arg4=5)
        set_skip(state=준타대사18스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 준타대사19()


class 준타대사18스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사19()


class 준타대사19(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__24$', arg4=6)
        set_skip(state=준타대사19스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 준타대사20()


class 준타대사19스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사20()


class 준타대사20(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001454__25$', arg4=3)
        set_skip(state=준타대사20스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class 준타대사20스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='gdfight')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            move_user(mapId=2000039, portalId=10)
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            return 종료()


class 종료(state.State):
    pass


