""" trigger/52000029_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,2001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 구르는천둥대사01()


class 구르는천둥대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001581, script='$52000029_QD__MAIN__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 유페리아대사01()


class 유페리아대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[608], visible=True)
        set_conversation(type=2, spawnId=11001564, script='$52000029_QD__MAIN__1$', arg4=2, arg5=0)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        select_camera(triggerId=3022, enable=True)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001_A')
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPC이동2()


class NPC이동2(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_A')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPC이동3()


class NPC이동3(state.State):
    def on_enter(self):
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1006_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 카메라이동()


class 카메라이동(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이펙트연출()


class 이펙트연출(state.State):
    def on_enter(self):
        add_buff(boxIds=[2001], skillId=71000003, level=1, arg4=True, arg5=False)
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이슈라이동01()


class 이슈라이동01(state.State):
    def on_enter(self):
        select_camera(triggerId=304, enable=True)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 이슈라대사01()


class 이슈라대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_conversation(type=2, spawnId=11001244, script='$52000029_QD__MAIN__2$', arg4=2, arg5=0) # 음성 코드 00001296

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 홀슈타트방향전환()


class 홀슈타트방향전환(state.State):
    def on_enter(self):
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 홀슈타트대사01()


class 홀슈타트대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=True)
        set_conversation(type=2, spawnId=11001231, script='$52000029_QD__MAIN__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 홀슈타트도망()


class 홀슈타트도망(state.State):
    def on_enter(self):
        select_camera(triggerId=3055, enable=True)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001_B')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이슈라추격()


class 이슈라추격(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1002,1004,1005,1006])
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)
        create_monster(spawnIds=[1009], arg2=False)
        create_monster(spawnIds=[1010], arg2=False)
        create_monster(spawnIds=[1011], arg2=False)
        create_monster(spawnIds=[1101], arg2=False)
        create_monster(spawnIds=[1102], arg2=False)
        create_monster(spawnIds=[1104], arg2=False)
        create_monster(spawnIds=[1105], arg2=False)
        create_monster(spawnIds=[1106], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NPC집결()


class NPC집결(state.State):
    def on_enter(self):
        select_camera(triggerId=306, enable=True)
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007_B')
        move_npc(spawnId=1008, patrolName='MS2PatrolData_1008_B')
        move_npc(spawnId=1009, patrolName='MS2PatrolData_1009_B')
        move_npc(spawnId=1010, patrolName='MS2PatrolData_1010_B')
        move_npc(spawnId=1011, patrolName='MS2PatrolData_1011_B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 렌듀비앙대사01()


class 렌듀비앙대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001230, script='$52000029_QD__MAIN__4$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사01()


class 아노스대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=307, enable=True)
        set_effect(triggerIds=[607], visible=True)
        set_conversation(type=2, spawnId=11000032, script='$52000029_QD__MAIN__5$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 제나대사01()


class 제나대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001583, script='$52000029_QD__MAIN__6$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 유페리아대사02()


class 유페리아대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[609], visible=True)
        set_conversation(type=2, spawnId=11001564, script='$52000029_QD__MAIN__7$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 이슈라대사02()


class 이슈라대사02(state.State):
    def on_enter(self):
        select_camera(triggerId=308, enable=True)
        set_effect(triggerIds=[603], visible=True)
        set_conversation(type=2, spawnId=11001244, script='$52000029_QD__MAIN__8$', arg4=2, arg5=0) # 음성 코드 00001297

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이슈라대사03()


class 이슈라대사03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        set_conversation(type=2, spawnId=11001244, script='$52000029_QD__MAIN__9$', arg4=11, arg5=0) # 음성 코드 00001298

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11500):
            return 이슈라대사04()


class 이슈라대사04(state.State):
    def on_enter(self):
        select_camera(triggerId=306, enable=True)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_D')
        set_effect(triggerIds=[605], visible=True)
        set_conversation(type=2, spawnId=11001244, script='$52000029_QD__MAIN__10$', arg4=6, arg5=0) # 음성 코드 00001299

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 렌듀비앙대사02()


class 렌듀비앙대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001230, script='$52000029_QD__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 렌듀비앙이동()


class 렌듀비앙이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007_C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 렌듀비앙캐스팅()


class 렌듀비앙캐스팅(state.State):
    def on_enter(self):
        add_buff(boxIds=[1007], skillId=71000004, level=1, arg4=True, arg5=False)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_C')
        select_camera(triggerId=309, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이슈라대사05()


class 이슈라대사05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=True)
        set_conversation(type=2, spawnId=11001244, script='$52000029_QD__MAIN__12$', arg4=3, arg5=0) # 음성 코드 00001300

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=52000030, portalId=0)
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 종료(state.State):
    pass


