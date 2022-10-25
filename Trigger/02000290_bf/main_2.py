""" trigger/02000290_bf/main_2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[905], visible=True)
        self.set_agent(triggerIds=[906], visible=True)
        self.set_agent(triggerIds=[907], visible=True)
        self.set_agent(triggerIds=[908], visible=True)
        self.set_ladder(triggerIds=[531], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[532], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[533], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[534], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[535], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[536], visible=False, animationEffect=False)
        self.set_mesh(triggerIds=[3089], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3108], visible=True, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=3110, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3111], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3112,3113,3114,3115,3116,3117], visible=True, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=3120, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3121], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[5101], visible=False) # LadderAppear
        self.destroy_monster(spawnIds=[1011])
        self.destroy_monster(spawnIds=[1012])
        self.destroy_monster(spawnIds=[1013])
        self.destroy_monster(spawnIds=[1014])
        self.destroy_monster(spawnIds=[1015])
        self.destroy_monster(spawnIds=[1016])
        self.destroy_monster(spawnIds=[1017])
        self.destroy_monster(spawnIds=[1018])
        self.destroy_monster(spawnIds=[1019])
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[6003], visible=False)
        self.set_effect(triggerIds=[6004], visible=False)
        self.set_effect(triggerIds=[6005], visible=False)
        self.set_effect(triggerIds=[6006], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 준비(self.ctx)


class 준비(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.create_monster(spawnIds=[2002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 사다리생성(self.ctx)


class 사다리생성(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # GuideUI
        self.show_guide_summary(entityId=20002903, textId=20002903)
        self.set_effect(triggerIds=[5101], visible=True) # LadderAppear
        self.set_ladder(triggerIds=[531], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[532], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[533], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[534], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[535], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[536], visible=True, animationEffect=True)
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=9991, isEnable=True)
        self.enable_spawn_point_pc(spawnId=9992, isEnable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.hide_guide_summary(entityId=20002903)
            return 트리거09시작(self.ctx)


class 트리거09시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1011], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1011]):
            return 트리거10시작(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 트리거10시작(self.ctx)


class 트리거10시작(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[905], visible=False)
        self.set_agent(triggerIds=[906], visible=False)
        self.set_mesh(triggerIds=[3089], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=True, arg3=0, delay=200, scale=2)
        self.create_monster(spawnIds=[1012], animationEffect=False)
        self.create_monster(spawnIds=[1013], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1012,1013]):
            return 트리거11시작(self.ctx)
        if self.wait_tick(waitTick=12000):
            return 트리거11시작(self.ctx)


class 트리거11시작(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[907], visible=False)
        self.set_agent(triggerIds=[908], visible=False)
        self.set_mesh(triggerIds=[3108], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True, arg3=0, delay=200, scale=2)
        self.create_monster(spawnIds=[1014], animationEffect=False)
        self.create_monster(spawnIds=[1015], animationEffect=False)
        self.create_monster(spawnIds=[1016], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1014,1015,1016]):
            return 트리거12시작(self.ctx)
        if self.wait_tick(waitTick=15000):
            return 트리거12시작(self.ctx)


class 트리거12시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3110, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3111], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1017], animationEffect=False)
        self.create_monster(spawnIds=[1018], animationEffect=False)
        self.create_monster(spawnIds=[1019], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리거12진행(self.ctx)


class 트리거12진행(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3110, visible=False, initialSequence='Opened')
        self.set_mesh(triggerIds=[3112,3113,3114,3115,3116,3117], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1017,1018,1019]):
            return 트리거13시작(self.ctx)
        if self.wait_tick(waitTick=15000):
            return 트리거13시작(self.ctx)


class 트리거13시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3120, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3121], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리거13진행(self.ctx)


class 트리거13진행(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3120, visible=False, initialSequence='Opened')
        self.set_mesh(triggerIds=[3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132], visible=False, arg3=0, delay=200, scale=2)
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=9991, isEnable=False)
        self.enable_spawn_point_pc(spawnId=9992, isEnable=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2002]):
            return 연출대기(self.ctx)


class 연출대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=801, enable=True)
        self.set_timer(timerId='3', seconds=3)
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504], visible=False, arg3=0, delay=300, scale=3)
        self.set_skip(state=연출종료)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[801], returnView=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 공주구출(self.ctx)


class 공주구출(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=801, enable=False)
        self.set_effect(triggerIds=[5000], visible=True) # GuideUI
        self.show_guide_summary(entityId=20002904, textId=20002904)
        self.set_interact_object(triggerIds=[10000464], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000464], stateValue=0):
            self.hide_guide_summary(entityId=20002904)
            return 완료(self.ctx)


class 완료(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=7, arg2='$02000290_BF__MAIN_2__2$', arg3='3000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 포털생성(self.ctx)


class 포털생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[910])
        self.create_monster(spawnIds=[911])
        self.create_monster(spawnIds=[912])
        self.create_monster(spawnIds=[913])
        self.create_monster(spawnIds=[914])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPC이동01(self.ctx)


class NPC이동01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=910, patrolName='MS2PatrolData910')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPC이동02(self.ctx)


class NPC이동02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=911, patrolName='MS2PatrolData911')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPC이동03(self.ctx)


class NPC이동03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=912, patrolName='MS2PatrolData912')
        self.move_npc(spawnId=914, patrolName='MS2PatrolData914')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPC이동04(self.ctx)


class NPC이동04(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=913, patrolName='MS2PatrolData913')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPC대사01(self.ctx)


class NPC대사01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_conversation(type=1, spawnId=910, script='$02000290_BF__MAIN_2__4$', arg4=3)
            self.set_effect(triggerIds=[6003], visible=True)
            return NPC대사02(self.ctx)


class NPC대사02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_conversation(type=1, spawnId=911, script='$02000290_BF__MAIN_2__5$', arg4=3)
            self.set_effect(triggerIds=[6004], visible=True)
            return NPC대사03(self.ctx)


class NPC대사03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_conversation(type=1, spawnId=912, script='$02000290_BF__MAIN_2__6$', arg4=3)
            self.set_effect(triggerIds=[6005], visible=True)
            return NPC대사04(self.ctx)


class NPC대사04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_conversation(type=1, spawnId=913, script='$02000290_BF__MAIN_2__7$', arg4=3)
            self.set_effect(triggerIds=[6006], visible=True)
            self.hide_guide_summary(entityId=20002905)
            return 종료대기(self.ctx)


class 종료대기(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=99999, type='trigger', achieve='ClearYomiprincess') # ClearYomiprincess 퀘스트
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
