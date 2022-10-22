""" trigger/02000290_bf/main_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[905], visible=True)
        set_agent(triggerIds=[906], visible=True)
        set_agent(triggerIds=[907], visible=True)
        set_agent(triggerIds=[908], visible=True)
        set_ladder(triggerIds=[531], visible=False, animationEffect=False)
        set_ladder(triggerIds=[532], visible=False, animationEffect=False)
        set_ladder(triggerIds=[533], visible=False, animationEffect=False)
        set_ladder(triggerIds=[534], visible=False, animationEffect=False)
        set_ladder(triggerIds=[535], visible=False, animationEffect=False)
        set_ladder(triggerIds=[536], visible=False, animationEffect=False)
        set_mesh(triggerIds=[3089], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3108], visible=True, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=3110, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3111], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3112,3113,3114,3115,3116,3117], visible=True, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=3120, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3121], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[5101], visible=False) # LadderAppear
        destroy_monster(spawnIds=[1011])
        destroy_monster(spawnIds=[1012])
        destroy_monster(spawnIds=[1013])
        destroy_monster(spawnIds=[1014])
        destroy_monster(spawnIds=[1015])
        destroy_monster(spawnIds=[1016])
        destroy_monster(spawnIds=[1017])
        destroy_monster(spawnIds=[1018])
        destroy_monster(spawnIds=[1019])
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[6003], visible=False)
        set_effect(triggerIds=[6004], visible=False)
        set_effect(triggerIds=[6005], visible=False)
        set_effect(triggerIds=[6006], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)
        create_monster(spawnIds=[2002], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 사다리생성()


class 사다리생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        show_guide_summary(entityId=20002903, textId=20002903)
        set_effect(triggerIds=[5101], visible=True) # LadderAppear
        set_ladder(triggerIds=[531], visible=True, animationEffect=True)
        set_ladder(triggerIds=[532], visible=True, animationEffect=True)
        set_ladder(triggerIds=[533], visible=True, animationEffect=True)
        set_ladder(triggerIds=[534], visible=True, animationEffect=True)
        set_ladder(triggerIds=[535], visible=True, animationEffect=True)
        set_ladder(triggerIds=[536], visible=True, animationEffect=True)
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=9991, isEnable=True)
        enable_spawn_point_pc(spawnId=9992, isEnable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            hide_guide_summary(entityId=20002903)
            return 트리거09시작()


class 트리거09시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1011], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1011]):
            return 트리거10시작()
        if wait_tick(waitTick=10000):
            return 트리거10시작()


class 트리거10시작(state.State):
    def on_enter(self):
        set_agent(triggerIds=[905], visible=False)
        set_agent(triggerIds=[906], visible=False)
        set_mesh(triggerIds=[3089], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=True, arg3=0, arg4=200, arg5=2)
        create_monster(spawnIds=[1012], arg2=False)
        create_monster(spawnIds=[1013], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1012,1013]):
            return 트리거11시작()
        if wait_tick(waitTick=12000):
            return 트리거11시작()


class 트리거11시작(state.State):
    def on_enter(self):
        set_agent(triggerIds=[907], visible=False)
        set_agent(triggerIds=[908], visible=False)
        set_mesh(triggerIds=[3108], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True, arg3=0, arg4=200, arg5=2)
        create_monster(spawnIds=[1014], arg2=False)
        create_monster(spawnIds=[1015], arg2=False)
        create_monster(spawnIds=[1016], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1014,1015,1016]):
            return 트리거12시작()
        if wait_tick(waitTick=15000):
            return 트리거12시작()


class 트리거12시작(state.State):
    def on_enter(self):
        set_actor(triggerId=3110, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3111], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1017], arg2=False)
        create_monster(spawnIds=[1018], arg2=False)
        create_monster(spawnIds=[1019], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리거12진행()


class 트리거12진행(state.State):
    def on_enter(self):
        set_actor(triggerId=3110, visible=False, initialSequence='Opened')
        set_mesh(triggerIds=[3112,3113,3114,3115,3116,3117], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1017,1018,1019]):
            return 트리거13시작()
        if wait_tick(waitTick=15000):
            return 트리거13시작()


class 트리거13시작(state.State):
    def on_enter(self):
        set_actor(triggerId=3120, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3121], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리거13진행()


class 트리거13진행(state.State):
    def on_enter(self):
        set_actor(triggerId=3120, visible=False, initialSequence='Opened')
        set_mesh(triggerIds=[3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132], visible=False, arg3=0, arg4=200, arg5=2)
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=9991, isEnable=False)
        enable_spawn_point_pc(spawnId=9992, isEnable=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            return 연출대기()


class 연출대기(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=801, enable=True)
        set_timer(timerId='3', seconds=3)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504], visible=False, arg3=0, arg4=300, arg5=3)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[801], returnView=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return 공주구출()


class 공주구출(state.State):
    def on_enter(self):
        select_camera(triggerId=801, enable=False)
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        show_guide_summary(entityId=20002904, textId=20002904)
        set_interact_object(triggerIds=[10000464], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000464], arg2=0):
            hide_guide_summary(entityId=20002904)
            return 완료()


class 완료(state.State):
    def on_enter(self):
        set_event_ui(type=7, arg2='$02000290_BF__MAIN_2__2$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[910])
        create_monster(spawnIds=[911])
        create_monster(spawnIds=[912])
        create_monster(spawnIds=[913])
        create_monster(spawnIds=[914])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC이동01()


class NPC이동01(state.State):
    def on_enter(self):
        move_npc(spawnId=910, patrolName='MS2PatrolData910')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC이동02()


class NPC이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=911, patrolName='MS2PatrolData911')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC이동03()


class NPC이동03(state.State):
    def on_enter(self):
        move_npc(spawnId=912, patrolName='MS2PatrolData912')
        move_npc(spawnId=914, patrolName='MS2PatrolData914')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC이동04()


class NPC이동04(state.State):
    def on_enter(self):
        move_npc(spawnId=913, patrolName='MS2PatrolData913')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC대사01()


class NPC대사01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_conversation(type=1, spawnId=910, script='$02000290_BF__MAIN_2__4$', arg4=3)
            set_effect(triggerIds=[6003], visible=True)
            return NPC대사02()


class NPC대사02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_conversation(type=1, spawnId=911, script='$02000290_BF__MAIN_2__5$', arg4=3)
            set_effect(triggerIds=[6004], visible=True)
            return NPC대사03()


class NPC대사03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_conversation(type=1, spawnId=912, script='$02000290_BF__MAIN_2__6$', arg4=3)
            set_effect(triggerIds=[6005], visible=True)
            return NPC대사04()


class NPC대사04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_conversation(type=1, spawnId=913, script='$02000290_BF__MAIN_2__7$', arg4=3)
            set_effect(triggerIds=[6006], visible=True)
            hide_guide_summary(entityId=20002905)
            return 종료대기()


class 종료대기(state.State):
    def on_enter(self):
        dungeon_clear()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_achievement(triggerId=99999, type='trigger', achieve='ClearYomiprincess') # ClearYomiprincess 퀘스트
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


