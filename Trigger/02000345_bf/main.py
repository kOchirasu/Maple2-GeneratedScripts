""" trigger/02000345_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

#  플레이어 감지 
#  60002 : 모든 영역 
class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2001,2002], visible=True, arg3=1, arg4=1)
        remove_buff(boxId=60002, skillId=99910040)
        remove_buff(boxId=60002, skillId=70000106)
        create_monster(spawnIds=[102], arg2=True) # 촬영 감독
        set_mesh(triggerIds=[6010], visible=True) # 벽 생성
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=False) # 길 차단

    def on_tick(self) -> state.State:
        if count_users(boxId=60001, boxId=1):
            return CheckUserCount()
        if wait_tick(waitTick=5000):
            return start_game_01()


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
        move_random_user(mapId=2000345, portalId=99, triggerId=702, count=1)
        move_random_user(mapId=2000345, portalId=98, triggerId=60005, count=1)
        move_random_user(mapId=2000345, portalId=97, triggerId=60005, count=1)
        move_random_user(mapId=2000345, portalId=96, triggerId=60005, count=1)
        select_camera_path(pathIds=[8801,8802], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_01()


class start_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8802,8803], returnView=False)
        set_conversation(type=1, spawnId=102, script='$02000345_BF__MAIN__0$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__1$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000345_BF__MAIN__2$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__3$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000345_BF__MAIN__4$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__5$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_04()


class start_04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000345_BF__MAIN__6$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__7$', arg4=3)

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
        set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__8$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_07()


class start_07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__9$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_game()


class start_game(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera_path(pathIds=[8808], returnView=True)
        show_count_ui(text='$02000345_BF__MAIN__10$', stage=0, count=3)
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_game_01()


class start_game_01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000345_BF__MAIN__11$', arg3='3000')
        create_monster(spawnIds=[189], arg2=True, arg3=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_game_02()


class start_game_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8809,8810], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_game_02_b()


class start_game_02_b(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=189, script='$02000345_BF__MAIN__12$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001890, script='$02000345_BF__MAIN__13$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_game_03()


class start_game_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=189, script='$02000345_BF__MAIN__14$', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=11001890, script='$02000345_BF__MAIN__15$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_game_04()


class start_game_04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=189, script='$02000345_BF__MAIN__16$', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=11001890, script='$02000345_BF__MAIN__17$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return start_game_05()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera_path(pathIds=[8808], returnView=True)


class start_game_05(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000345_BF__MAIN__18$', arg3='3000')
        create_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210], arg2=True, arg3=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,206,207,208,209,210]):
            return start_game_06()


class start_game_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301,302,303,304,305,306,307], arg2=True, arg3=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[301,302,303,304,305,306,307]):
            return start_game_07()


class start_game_07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401,402,403,404,405,406], arg2=True, arg3=0)


class 대기_01(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        set_interact_object(triggerIds=[10000791], state=0) # 보상 상태 (없음)
        set_mesh(triggerIds=[6001,6010], visible=True) # 벽 생성
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=False) # 길 차단
        set_ladder(triggerIds=[9001], visible=False, animationEffect=False, animationDelay=0) # 사다리 가려
        set_ladder(triggerIds=[9002], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[9003], visible=False, animationEffect=False, animationDelay=0)

    def on_tick(self) -> state.State:
        if count_users(boxId=60001, boxId=1):
            return 대기_02()


class 대기_02(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기_03()


class 대기_03(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=60001, boxId=1):
            return 오브젝티브_01()


class 오브젝티브_01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000345_BF__MAIN1__2$', arg3='10000')
        set_timer(timerId='10', seconds=10, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 오브젝티브_02()


class 오브젝티브_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001,8002], returnView=True)
        create_monster(spawnIds=[101], arg2=True) # 보스 등장
        set_cinematic_ui(type=1)
        # <action name="유저를이동시킨다" arg1="02000345" arg2="3"/>
        set_cinematic_ui(type=3, script='$02000345_BF__MAIN1__0$') # 오브젝티브
        set_timer(timerId='5', seconds=5, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 시작_01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


#    플레이어 감지하면 1초 대기 
class 시작_01(state.State):
    def on_enter(self):
        show_count_ui(text='$02000345_BF__MAIN1__3$', stage=0, count=3)
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 시작_02()


class 시작_02(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[9001], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        set_ladder(triggerIds=[9002], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        set_ladder(triggerIds=[9003], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 클리어()


class 클리어(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (on)
        set_event_ui(type=7, arg2='$02000345_BF__MAIN1__1$', arg3='3000')
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=True, arg4=0, arg5=10) # 길 생성
        set_mesh(triggerIds=[6010], visible=False, arg4=0, arg5=0) # 벽 삭제
        set_interact_object(triggerIds=[10000791], state=1) # 보상 상태 (없음)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 클리어_02()


class 클리어_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=110, textId=40009) # 포탈 이용하세요


