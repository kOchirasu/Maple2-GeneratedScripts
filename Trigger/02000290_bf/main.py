""" trigger/02000290_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_actor(triggerId=3000, visible=True, initialSequence='Closed')
        set_actor(triggerId=3010, visible=True, initialSequence='Closed')
        set_actor(triggerId=3020, visible=True, initialSequence='Closed')
        set_actor(triggerId=3040, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002,3003,3004,3005,3006,3007,3008], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3011], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3012,3013,3014,3015,3016], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3021], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3041], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[5000], visible=False) # GuideUI
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1003])
        destroy_monster(spawnIds=[1004])
        destroy_monster(spawnIds=[2001])
        destroy_monster(spawnIds=[2002])
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=9991, isEnable=False)
        enable_spawn_point_pc(spawnId=9992, isEnable=False)

    def on_tick(self) -> state.State:
        if check_user():
            return 로딩딜레이()


class 로딩딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[802,800], returnView=False)
        set_skip(state=CameraWalk01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CameraWalk01()

state.DungeonStart = DungeonStart


class CameraWalk01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[800,802], returnView=True)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        set_event_ui(type=1, arg2='$02000290_BF__MAIN__4$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리거01시작()


#  첫 번째 문 열림 
class 트리거01시작(state.State):
    def on_enter(self):
        set_actor(triggerId=3000, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리거01진행()


class 트리거01진행(state.State):
    def on_enter(self):
        set_actor(triggerId=3000, visible=False, initialSequence='Opened')
        set_mesh(triggerIds=[3002,3003,3004,3005,3006,3007,3008], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001]):
            return 트리거02시작()
        if wait_tick(waitTick=7000):
            return 트리거02시작()


#  두 번째 문 열림 
class 트리거02시작(state.State):
    def on_enter(self):
        set_actor(triggerId=3010, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3011], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리거02진행()


class 트리거02진행(state.State):
    def on_enter(self):
        set_actor(triggerId=3010, visible=False, initialSequence='Opened')
        set_mesh(triggerIds=[3012,3013,3014,3015,3016], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1002,1003]):
            return 트리거03시작()
        if wait_tick(waitTick=10000):
            return 트리거03시작()


#  세 번째 문 열림 
class 트리거03시작(state.State):
    def on_enter(self):
        set_actor(triggerId=3020, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3021], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리거03진행()


class 트리거03진행(state.State):
    def on_enter(self):
        set_actor(triggerId=3020, visible=False, initialSequence='Opened')
        set_mesh(triggerIds=[3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1004]):
            return 트리거04시작()
        if wait_tick(waitTick=7000):
            return 트리거04시작()


class 트리거04시작(state.State):
    def on_enter(self):
        set_actor(triggerId=3040, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3041], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리거04진행()


class 트리거04진행(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002902)
        set_actor(triggerId=3040, visible=False, initialSequence='Opened')
        set_mesh(triggerIds=[3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


