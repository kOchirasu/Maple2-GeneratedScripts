""" trigger/02010052_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[7001], visible=False)
        set_effect(triggerIds=[7002], visible=False)
        set_effect(triggerIds=[81004], visible=False)
        create_monster(spawnIds=[101,102,103,107,108,109,110,111,112], arg2=False) # 기본 배치 될 몬스터 등장
        create_monster(spawnIds=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417], arg2=False) # 기본 배치 될 몬스터 등장
        create_monster(spawnIds=[421,422,423], arg2=False) # 기본 배치 될 몬스터 등장
        create_monster(spawnIds=[431,432,433,434,435,436,437], arg2=False) # 기본 배치 될 몬스터 등장
        create_monster(spawnIds=[601,602,603,604,605,606,607,608,609,610,611,612,613], arg2=False) # 기본 배치 될 몬스터 등장
        set_timer(timerId='1', seconds=1, display=False)
        set_mesh(triggerIds=[75011,75012,75013], visible=True, arg3=1000, arg4=500, arg5=8) # 물 삭제
        set_mesh(triggerIds=[75001,75002,75003], visible=False, arg3=1000, arg4=500, arg5=8) # 물 삭제
        create_monster(spawnIds=[991], arg2=False) # 카나의 분신 991 (Battle_01)
        create_monster(spawnIds=[992], arg2=False) # 카나의 분신 992 (Battle_02)
        create_monster(spawnIds=[993], arg2=False) # 카나의 분신 993 (Battle_03)
        create_monster(spawnIds=[994], arg2=False) # 카나의 분신 994 (Battle_04)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Start_03()

state.DungeonStart = DungeonStart


class Start_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[80010,80011], returnView=True)
        set_mesh(triggerIds=[22201,22202,22203,22204,22205,22206,22207,22208,22209,22210,22211,22212,22213,22214,22215,22216,22217,22218,22219,22220,22221,22222,22223,22224,22225,22226,22227,22228,22229,22230,22231,22232,22233,22234,22235,22236,22237,22238,22239,22240,22241,22242,22243,22244,22245,22246,22247,22248,22249,22250,22251,22252,22253,22254,22255,22256,22257,22258,22259,22260,22261,22262,22263,22264,22265,22266,22267,22268,22269,22270,22271,22272,22273,22274,22275,22276,22277,22278,22279,22280,22281,22282,22283,22284,22285,22286,22287,22288,22289,22290,22291,22292,22293,22294,22295,22296,22297,22298,22299], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Start_04()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class Start_04(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02010052_BF__MAIN__6$', arg3='3000')
        # <action name="PlaySystemSoundInBox" arg2="System_ShowGuideSummary_01"/>

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=80001, enable=True)
        set_conversation(type=2, spawnId=21800073, script='$02010052_BF__MAIN__1$', arg4=3) # 카나 대사
        move_npc(spawnId=991, patrolName='MS2PatrolData_1001') # 카나의 분신 991 (이동)
        set_skip(state=Event_01_02)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_01_02()

    def on_exit(self):
        remove_cinematic_talk()


class Event_01_02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=21800073, script='$02010052_BF__MAIN__2$', arg4=3) # 카나 대사
        move_npc(spawnId=991, patrolName='MS2PatrolData_1002') # 카나의 분신 991 (이동)
        set_skip(state=Event_01_03)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_01_03()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)
        select_camera(triggerId=80001, enable=False)


class Event_01_03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요
        set_effect(triggerIds=[7901], visible=True) # 카나 사라짐
        destroy_monster(spawnIds=[991]) # 카나 사라짐

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=992, script='$02010052_BF__MAIN__3$', arg4=3) # 카나 말풍선 대사
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_02_02()


class Event_02_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요
        set_conversation(type=1, spawnId=992, script='$02010052_BF__MAIN__4$', arg4=3, arg5=0) # 카나 말풍선 대사
        move_npc(spawnId=992, patrolName='MS2PatrolData_1003') # 카나의 분신 992 (이동)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_02_03()


class Event_02_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[992])

    def on_tick(self) -> state.State:
        if count_users(boxId=705, boxId=1):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=80002, enable=True)
        set_conversation(type=2, spawnId=21800073, script='$02010052_BF__MAIN__5$', arg4=3) # 카나 대사
        move_npc(spawnId=993, patrolName='MS2PatrolData_1004') # 카나의 분신 993 (이동)
        set_skip(state=Event_03_02)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_03_02()

    def on_exit(self):
        remove_cinematic_talk() # 레터박스, 플레이어 조작 불가능 해제
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)
        select_camera(triggerId=80002, enable=False)


class Event_03_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요
        destroy_monster(spawnIds=[993]) # 카나 사라짐
        create_monster(spawnIds=[9999], arg2=True) # 공격 카나 생성


