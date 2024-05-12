""" trigger/02000532_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3000,3001], visible=True)
        self.set_mesh(triggerIds=[3002,3003], visible=True)
        self.set_mesh(triggerIds=[3004], visible=True)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_effect(triggerIds=[7006], visible=False)
        self.set_effect(triggerIds=[7007], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # Missing State: State
        self.set_scene_skip()
        self.create_monster(spawnIds=[216,101,102,103,104,105,106,107,108,109,111,112,113], animationEffect=True)
        self.create_monster(spawnIds=[110,111], animationEffect=True)
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_8000')
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_8001')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3000,3001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=목표, action='nextState')
        self.select_camera_path(pathIds=[604,603], returnView=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='$02000532_BF__MAIN__0$', desc='$02000532_BF__MAIN__1$', align='centerRight', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 목표(self.ctx)


class 목표(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.lock_my_pc(isLock=False)
        self.reset_camera(interpolationTime=1)
        self.set_event_ui(type=1, arg2='$02000532_BF__MAIN__2$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 문들어가기(self.ctx)


class 문들어가기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$02000532_BF__MAIN__3$', arg3='3000')
        self.set_effect(triggerIds=[7006], visible=True)
        self.set_effect(triggerIds=[7007], visible=True)
        self.create_monster(spawnIds=[408], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[408], arg2=False):
            return 문이열림(self.ctx)


class 문이열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3004], visible=False)
        self.add_balloon_talk(spawnId=112, msg='$02000532_BF__MAIN__4$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=112, msg='$02000532_BF__MAIN__5$', duration=3500, delayTick=3500)
        self.add_balloon_talk(spawnId=102, msg='$02000532_BF__MAIN__6$', duration=3500, delayTick=500)
        self.add_balloon_talk(spawnId=113, msg='$02000532_BF__MAIN__7$', duration=3500, delayTick=900)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=10000)
        self.set_npc_emotion_loop(spawnId=113, sequenceName='Sit_Down_A', duration=10000)
        self.set_npc_emotion_loop(spawnId=112, sequenceName='Talk_A', duration=10000)
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_mesh(triggerIds=[3000,3001], visible=False)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702], jobCode=0):
            return 경계하기(self.ctx)


class 경계하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.lock_my_pc(isLock=True)
        self.set_scene_skip(state=흑성회의반격, action='nextState')
        self.add_balloon_talk(spawnId=104, msg='$02000532_BF__MAIN__8$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=105, msg='$02000532_BF__MAIN__9$', duration=3500, delayTick=2500)
        self.add_balloon_talk(spawnId=103, msg='$02000532_BF__MAIN__10$', duration=3500, delayTick=2800)
        self.set_effect(triggerIds=[7006], visible=False)
        self.set_effect(triggerIds=[7007], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6500):
            return 통신을받은제이부하(self.ctx)


class 통신을받은제이부하(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[602], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 통신을받은제이부하2(self.ctx)


class 통신을받은제이부하2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=205, msg='$02000532_BF__MAIN__11$', duration=3500, delayTick=500)
        self.add_balloon_talk(spawnId=300, msg='$02000532_BF__MAIN__12$', duration=3500, delayTick=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 불안한제이(self.ctx)


class 불안한제이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 불안한제이2(self.ctx)


class 불안한제이2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000532_BF__MAIN__13$')
        self.add_balloon_talk(spawnId=205, msg='$02000532_BF__MAIN__14$', duration=3500, delayTick=4100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 흑성회의반격(self.ctx)


class 흑성회의반격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(triggerIds=[3002,3003], visible=False)
        self.lock_my_pc(isLock=False)
        self.reset_camera(interpolationTime=1)
        self.set_event_ui(type=1, arg2='$02000532_BF__MAIN__15$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 흑성회의반격2(self.ctx)


class 흑성회의반격2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,110,111,112,113])
        self.create_monster(spawnIds=[401,402,403,404,412,405], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 흑성회의반격22(self.ctx)


class 흑성회의반격22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=21450001, illust='Mafia1_normal', duration=3000, script='$02000532_BF__MAIN__16$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 골목체크(self.ctx)


class 골목체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=3000, script='$02000532_BF__MAIN__17$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[705], jobCode=0):
            return 길목에서나오는몬스터(self.ctx)


class 길목에서나오는몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[108,109])
        self.create_monster(spawnIds=[406,407,409,410,411], animationEffect=True)
        self.add_balloon_talk(spawnId=409, msg='$02000532_BF__MAIN__18$', duration=3500, delayTick=1500)
        self.add_balloon_talk(spawnId=410, msg='$02000532_BF__MAIN__19$', duration=3500, delayTick=1500)
        self.add_balloon_talk(spawnId=407, msg='$02000532_BF__MAIN__20$', duration=3500, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[401,402,403,404,405,406,407,409,410,411,412]):
            return 차생성2(self.ctx)


class 차생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=3000, script='$02000532_BF__MAIN__21$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 엘리베이터안내(self.ctx)


class 엘리베이터안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000532_BF__MAIN__22$', arg3='3000')
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)


initial_state = idle
