""" trigger/52000063_qd/90000640.xml """
from common import *
import state


class 시작대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[1001,1002], arg2=False)
        create_monster(spawnIds=[1101,1102,1103,1104,1105], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 퀘스트분기()


class 퀘스트분기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000640], questStates=[2]):
            return 완료가능90000640()
        if not quest_user_detected(boxIds=[199], questIds=[90000640], questStates=[2]):
            return 연출시작()


class 완료가능90000640(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1002])
        create_monster(spawnIds=[1003,1004], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000640], questStates=[3]):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 연출시작(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)
        set_conversation(type=2, spawnId=11000168, script='$52000063_QD__90000640__0$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return K대사02()


class K대사02(state.State):
    def on_enter(self):
        move_npc(spawnId=1104, patrolName='MS2PatrolData_1104A')
        set_conversation(type=2, spawnId=11000168, script='$52000063_QD__90000640__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 마칸대사01()


class 마칸대사01(state.State):
    def on_enter(self):
        move_npc(spawnId=1101, patrolName='MS2PatrolData_1101A')
        move_npc(spawnId=1102, patrolName='MS2PatrolData_1102A')
        move_npc(spawnId=1103, patrolName='MS2PatrolData_1103A')
        move_npc(spawnId=1105, patrolName='MS2PatrolData_1105A')
        set_conversation(type=2, spawnId=11001872, script='$52000063_QD__90000640__2$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마칸대사02()


class 마칸대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001872, script='$52000063_QD__90000640__3$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=302, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 진행중90000640()


class 진행중90000640(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[90000640], questStates=[1]):
            move_user(mapId=52000063, portalId=1)
            return 차연출시작2()


class 차연출시작2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=303, enable=True)
        set_conversation(type=2, spawnId=11000168, script='$52000063_QD__90000640__4$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return K대사03()


class K대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=304, enable=True)
        set_conversation(type=2, spawnId=11000168, script='$52000063_QD__90000640__5$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3101], visible=True, arg3=0, arg4=0, arg5=0)
        destroy_monster(spawnIds=[1001,1002])
        select_camera(triggerId=304, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2) # action name="이벤트UI를설정한다" arg1="0" arg2="0,0" /
        show_count_ui(text='$52000063_QD__90000640__6$', stage=1, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 경기시작()


class 경기시작(state.State):
    def on_enter(self):
        set_user_value(triggerId=99999102, key='gameStart', value=1)
        set_user_value(triggerId=99999103, key='gameStart', value=1)
        set_user_value(triggerId=99999104, key='gameStart', value=1)
        create_item(spawnIds=[9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025])
        move_npc(spawnId=1101, patrolName='MS2PatrolData_1101R')
        move_npc(spawnId=1102, patrolName='MS2PatrolData_1102R')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPC2차이동()


class NPC2차이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1103, patrolName='MS2PatrolData_1103R')
        move_npc(spawnId=1104, patrolName='MS2PatrolData_1104R')
        move_npc(spawnId=1105, patrolName='MS2PatrolData_1105R')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 완료대기()


class 완료대기(state.State):
    def on_enter(self):
        create_item(spawnIds=[9026,9027,9028,9029])
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3101], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1003,1004], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 완료알림케이대사()


class 완료알림케이대사(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000168, script='$52000063_QD__90000640__7$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 완료()


class 완료(state.State):
    def on_enter(self):
        create_item(spawnIds=[9030,9031,9032,9033,9034,9035])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=199, type='trigger', achieve='ArrivedSupercar')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000640], questStates=[3]):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 종료(state.State):
    pass


