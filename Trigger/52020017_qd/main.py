""" trigger/52020017_qd/main.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200115], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)
        create_monster(spawnIds=[202], arg2=True)
        create_monster(spawnIds=[203], arg2=True)
        create_monster(spawnIds=[204], arg2=True)
        create_monster(spawnIds=[205], arg2=True)
        create_monster(spawnIds=[206], arg2=True)
        create_monster(spawnIds=[207], arg2=True)
        create_monster(spawnIds=[208], arg2=True)
        create_monster(spawnIds=[209], arg2=True)
        create_monster(spawnIds=[210], arg2=True)
        create_monster(spawnIds=[211], arg2=True)
        create_monster(spawnIds=[212], arg2=True)
        create_monster(spawnIds=[213], arg2=True)
        create_monster(spawnIds=[214], arg2=True)
        create_monster(spawnIds=[215], arg2=True)
        create_monster(spawnIds=[216], arg2=True)
        create_monster(spawnIds=[217], arg2=True)
        create_monster(spawnIds=[218], arg2=True)
        create_monster(spawnIds=[219], arg2=True)
        create_monster(spawnIds=[220], arg2=True)
        create_monster(spawnIds=[301], arg2=True)
        create_monster(spawnIds=[302], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[60200115], questStates=[1]):
            return Object_Off()


class Object_Off(state.State):
    def on_enter(self):
        set_ambient_light(primary=[0,0,0])
        create_monster(spawnIds=[101], arg2=True) # 엘레나
        set_effect(triggerIds=[5001], visible=True)
        set_interact_object(triggerIds=[10001282], state=0)
        add_balloon_talk(spawnId=0, msg='!', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Event_Start()


class Event_Start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003624, msg='아아…. 드디어 극의 주인공을 찾은 것 같네.', duration=2800, align='left')
        set_scene_skip(arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_A_01()


class Event_A_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        add_cinematic_talk(npcId=0, msg='!?', duration=1800, illustId='0', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_A_02()


class Event_A_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)
        add_cinematic_talk(npcId=11003624, msg='그래. 바로 너. 네가 주인공이야.', duration=2800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_A_03()


class Event_A_03(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=11003624, msg='참, 주인공 역할을 말해주지 않았구나.', duration=2800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_A_04()


class Event_A_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003624, msg='이 극의 주인공 역할은 말이야.', duration=1800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_A_05()


class Event_A_05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True)
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11003624, msg='여기서 죽는 거야.', duration=2800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_A_06()


class Event_A_06(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003624, msg='자, 그럼 극을 시작해볼까?', duration=2800, illustId='RobotMaidBrownHair_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_A_End()


class Event_A_Skip_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 엘레나

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_A_Skip_02()


class Event_A_Skip_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_A_End()


class Event_A_End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_ambient_light(primary=[1,1,1])
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_balloon_talk(spawnId=0, msg='!', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle_A_Ready()


class Battle_A_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle_A()


class Battle_A(state.State):
    def on_enter(self):
        change_monster(removeSpawnId=201, addSpawnId=601)
        change_monster(removeSpawnId=202, addSpawnId=602)
        change_monster(removeSpawnId=203, addSpawnId=603)
        change_monster(removeSpawnId=204, addSpawnId=604)
        change_monster(removeSpawnId=205, addSpawnId=605)
        change_monster(removeSpawnId=206, addSpawnId=606)
        change_monster(removeSpawnId=207, addSpawnId=607)
        change_monster(removeSpawnId=208, addSpawnId=608)
        change_monster(removeSpawnId=209, addSpawnId=609)
        change_monster(removeSpawnId=210, addSpawnId=610)
        change_monster(removeSpawnId=211, addSpawnId=611)
        change_monster(removeSpawnId=212, addSpawnId=612)
        change_monster(removeSpawnId=213, addSpawnId=613)
        change_monster(removeSpawnId=214, addSpawnId=614)
        change_monster(removeSpawnId=215, addSpawnId=615)
        change_monster(removeSpawnId=216, addSpawnId=616)
        change_monster(removeSpawnId=217, addSpawnId=617)
        change_monster(removeSpawnId=218, addSpawnId=618)
        change_monster(removeSpawnId=219, addSpawnId=619)
        change_monster(removeSpawnId=220, addSpawnId=620)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620]):
            return Battle_B_Ready()


class Battle_B_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle_B()


class Battle_B(state.State):
    def on_enter(self):
        change_monster(removeSpawnId=301, addSpawnId=701)
        change_monster(removeSpawnId=302, addSpawnId=702)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[701,702]):
            return Battle_End()


class Battle_End(state.State):
    def on_enter(self):
        set_ambient_light(primary=[1,1,1])
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        destroy_monster(spawnIds=[101])
        set_interact_object(triggerIds=[10001282], state=1)


