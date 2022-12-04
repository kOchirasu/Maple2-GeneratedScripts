""" trigger/02000536_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[501,502,504,505,506,507,508,509,510,511], animationEffect=False)
        self.set_interact_object(triggerIds=[10003147], state=0)
        self.set_mesh(triggerIds=[9999], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip()
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=전투시작, action='nextState')
        self.select_camera_path(pathIds=[7000,7003], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='$02000536_BF__MAIN__0$', desc='$02000536_BF__MAIN__1$', align='centerRight', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 하렌인사(self.ctx)


class 하렌인사(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7003,7001], returnView=False)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Bore_A', duration=5000)
        self.add_cinematic_talk(npcId=23300001, msg='$02000536_BF__MAIN__2$', align='center', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 하렌인사2(self.ctx)


class 하렌인사2(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_01_E,Attack_01_B')
        self.add_cinematic_talk(npcId=23300001, msg='$02000536_BF__MAIN__3$', align='center', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.set_event_ui(type=1, arg2='$02000536_BF__MAIN__4$', arg3='3000')
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.destroy_monster(spawnIds=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=70, spawnId=101, isRelative=True):
            return 메이드군단을스폰(self.ctx)


class 메이드군단을스폰(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302,303,304], animationEffect=False)
        self.side_npc_talk(npcId=23300001, illust='Haren_serious', duration=4000, script='$02000536_BF__MAIN__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=101, isRelative=True):
            return 메이드군단을스폰2(self.ctx)


class 메이드군단을스폰2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401,402,403,404], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=30, spawnId=101, isRelative=True):
            return 몬스터사망체크(self.ctx)


class 몬스터사망체크(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23300001, illust='Haren_serious', duration=4000, script='$02000536_BF__MAIN__6$')
        self.create_monster(spawnIds=[201,202,203,204], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 던전클리어(self.ctx)


class 던전클리어(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23300001, illust='Haren_serious', duration=3000, script='$02000536_BF__MAIN__8$')
        self.set_mesh(triggerIds=[9999], visible=False)
        self.destroy_monster(spawnIds=[-1])
        self.dungeon_clear() # 보스 잡히고 던전 클리어 선언 먼저

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 트리거완료(self.ctx)


class 트리거완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1]) # 보스가 순삭 될 경우 트리거 타이밍이 어긋나서 소환몹 제거 안될 수 있기 때문에 혹시 몰라 최종 마지막에 몬스터 제거 명령 설정함
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 보스가 순삭될 경우 던전 클리어 선언되기 전에 포털로 나갈 우려가 있으므로 포털 오픈은 던전 클리어 이후 시점으로


initial_state = idle
