""" trigger/52010017_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[401], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[402], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[403], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[404], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[405], visible=False, animationEffect=False, animationDelay=0)
        create_monster(spawnIds=[1001], arg2=False)
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3003], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3004], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3005], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3006], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3007], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3008], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[102], questIds=[10002851], questStates=[1]):
            create_monster(spawnIds=[1002], arg2=False)
            create_monster(spawnIds=[1003], arg2=False)
            create_monster(spawnIds=[1004], arg2=False)
            create_monster(spawnIds=[2001], arg2=True)
            return 카메라연출01()


class 카메라연출01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 미카대사01()


class 미카대사01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])
        create_monster(spawnIds=[1005], arg2=False)
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005')
        set_ladder(triggerIds=[401], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[402], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[403], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[404], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[405], visible=True, animationEffect=True, animationDelay=0)
        set_conversation(type=2, spawnId=11001285, script='$52010017_QD__MAIN__0$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 체크포인트01()


class 체크포인트01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            create_monster(spawnIds=[2002], arg2=True)
            return 카메라연출02()


class 카메라연출02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 미카대사02()


class 미카대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010017_QD__MAIN__1$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            select_camera(triggerId=302, enable=False)
            return 체크포인트02()


class 체크포인트02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_A')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_A')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            return 미키이동01()


class 미키이동01(state.State):
    def on_enter(self):
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_A2')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[1005]):
            return 오브젝트01()


class 오브젝트01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)
            return 카메라연출03()


class 카메라연출03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 타라대사01()


class 타라대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001218, script='$52010017_QD__MAIN__2$', arg4=2)
        select_camera(triggerId=303, enable=True)
        create_monster(spawnIds=[2003], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 체크포인트03()


class 체크포인트03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=303, enable=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_B')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_B')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_B')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_B')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2003]):
            return 미키이동02()


class 미키이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_B2')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=104, spawnIds=[1005]):
            return 오브젝트02()


class 오브젝트02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_mesh(triggerIds=[3003], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3004], visible=True, arg3=0, arg4=0, arg5=0)
            return 카메라연출04()


class 카메라연출04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 둔바대사01()


class 둔바대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=304, enable=True)
        set_conversation(type=2, spawnId=11001217, script='$52010017_QD__MAIN__3$', arg4=2)
        create_monster(spawnIds=[2004], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 체크포인트04()


class 체크포인트04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=304, enable=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_C')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_C')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_C')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_C')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2004]):
            return 미키이동03()


class 미키이동03(state.State):
    def on_enter(self):
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_C2')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=105, spawnIds=[1005]):
            return 오브젝트03()


class 오브젝트03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_mesh(triggerIds=[3005], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3006], visible=True, arg3=0, arg4=0, arg5=0)
            return 카메라연출05()


class 카메라연출05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 스타츠대사01()


class 스타츠대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=True)
        set_conversation(type=2, spawnId=11001292, script='$52010017_QD__MAIN__4$', arg4=2)
        create_monster(spawnIds=[2005], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 체크포인트05()


class 체크포인트05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=305, enable=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_D')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_D')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_D')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_D')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2005]):
            return 미키이동04()


class 미키이동04(state.State):
    def on_enter(self):
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_D2')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=106, spawnIds=[1005]):
            return 오브젝트04()


class 오브젝트04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_mesh(triggerIds=[3007], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3008], visible=True, arg3=0, arg4=0, arg5=0)
            return 카메라연출06()


class 카메라연출06(state.State):
    def on_enter(self):
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_D3')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 미카대사03()


class 미카대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010017_QD__MAIN__5$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 미카대사04()


class 미카대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010017_QD__MAIN__6$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 이동대기()


class 이동대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=110, type='trigger', achieve='Getalllamestone')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            move_user(mapId=2010034, portalId=3, boxId=110)
            return 종료()


class 종료(state.State):
    pass


