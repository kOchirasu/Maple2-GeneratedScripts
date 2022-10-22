""" trigger/02000348_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

#  플레이어 감지 
#  60002 : 모든 영역 
class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=34808, key='cage_01', value=0)
        set_user_value(triggerId=34805, key='cage_02', value=0)
        set_user_value(triggerId=34806, key='cage_03', value=0)
        set_user_value(triggerId=34807, key='cage_04', value=0)
        set_mesh(triggerIds=[2001,2002], visible=True, arg3=1, arg4=1)
        remove_buff(boxId=60002, skillId=99910040)
        remove_buff(boxId=60002, skillId=70000106)
        create_monster(spawnIds=[102], arg2=True) # 촬영 감독
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        set_interact_object(triggerIds=[10000789], state=0) # 보상 상태 (없음)
        set_mesh(triggerIds=[6010], visible=True) # 벽 생성
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=False) # 길 차단

    def on_tick(self) -> state.State:
        if count_users(boxId=60001, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return touchfield()

state.DungeonStart = DungeonStart


class touchfield(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2001,2002], visible=False, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_random_user(mapId=2000348, portalId=99, triggerId=702, count=1)
        move_random_user(mapId=2000348, portalId=98, triggerId=60005, count=1)
        move_random_user(mapId=2000348, portalId=97, triggerId=60005, count=1)
        move_random_user(mapId=2000348, portalId=96, triggerId=60005, count=1)
        select_camera_path(pathIds=[8801,8802], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_01()


class start_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8802,8803], returnView=False)
        set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__0$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__1$', arg4=3)
        set_skip(state=start_game)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__2$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__3$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__4$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__5$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_04()


class start_04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__6$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__7$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_05()


class start_05(state.State):
    def on_enter(self):
        add_buff(boxIds=[702], skillId=70000106, level=1) # 카메라 스크린을 걸어준다.
        select_camera_path(pathIds=[8804,8805,8806,8807], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_06()


class start_06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__8$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_07()


class start_07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__9$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_game()


class start_game(state.State):
    def on_enter(self):
        add_buff(boxIds=[702], skillId=70000106, level=1) # 카메라 스크린을 걸어준다.
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera_path(pathIds=[8808], returnView=True)
        show_count_ui(text='$02000348_BF__MAIN__10$', stage=0, count=3)
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_game_01()


class start_game_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003446, textId=20003446, duration=5000)
        set_event_ui(type=1, arg2='$02000348_BF__MAIN__11$', arg3='3000')
        create_monster(spawnIds=[201,202,203,204,211,212,213,214], arg2=True)
        set_user_value(triggerId=34808, key='cage_01', value=1)
        set_user_value(triggerId=34805, key='cage_02', value=1)
        set_user_value(triggerId=34806, key='cage_03', value=1)
        set_user_value(triggerId=34807, key='cage_04', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[211,212,213,214]):
            return start_game_02()


class start_game_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_game_03()


class start_game_03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003442, textId=20003442, duration=5000)
        create_monster(spawnIds=[231,232], arg2=True)
        set_event_ui(type=1, arg2='$02000348_BF__MAIN__12$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_game_03_a()


class start_game_03_a(state.State):
    def on_enter(self):
        create_monster(spawnIds=[233,234], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[231,232,233,234]):
            return start_game_03_b()


class start_game_03_b(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8811,8810], returnView=True)
        set_event_ui(type=1, arg2='$02000348_BF__MAIN__13$', arg3='3000')
        set_effect(triggerIds=[7001], visible=True)
        set_skill(triggerIds=[7702], isEnable=True)
        set_skill(triggerIds=[7703], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start_game_05()


class start_game_05(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000348_BF__MAIN__14$', arg3='3000')
        create_monster(spawnIds=[101,205,206,207,208], arg2=True) # 촬영 감독

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return start_game_06()

    def on_exit(self):
        destroy_monster(spawnIds=[205,206,207,208])


class start_game_06(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 클리어()


class 클리어(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        remove_buff(boxId=60002, skillId=99910040)
        remove_buff(boxId=60002, skillId=70000106)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (on)
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=True, arg4=0, arg5=10) # 길 생성
        set_mesh(triggerIds=[6010], visible=False, arg4=0, arg5=0) # 벽 삭제
        set_interact_object(triggerIds=[10000789], state=1) # 보상 상태 (없음)
        set_timer(timerId='5', seconds=5)
        select_camera_path(pathIds=[8801,8803], returnView=False)
        set_skip(state=클리어_03)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 클리어_02()


class 클리어_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__15$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__16$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 클리어_03()


class 클리어_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__17$', arg4=2, arg5=0)
        move_npc(spawnId=102, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 클리어_04()

    def on_exit(self):
        destroy_monster(spawnIds=[102])


class 클리어_04(state.State):
    def on_enter(self):
        dungeon_variable(varId=1, value=1) # 1번 던전 클리어 처리
        show_guide_summary(entityId=110, textId=40009) # 포탈 이용하세요
        select_camera_path(pathIds=[8808], returnView=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


