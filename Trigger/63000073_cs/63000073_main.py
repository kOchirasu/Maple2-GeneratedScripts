""" trigger/63000073_cs/63000073_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.create_monster(spawnIds=[106], animationEffect=True)
        self.create_monster(spawnIds=[107], animationEffect=True)
        self.create_monster(spawnIds=[108], animationEffect=True)
        self.create_monster(spawnIds=[109], animationEffect=True)
        self.create_monster(spawnIds=[110], animationEffect=True)
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.create_monster(spawnIds=[115], animationEffect=True)
        self.create_monster(spawnIds=[116], animationEffect=True)
        self.create_monster(spawnIds=[117], animationEffect=True)
        self.set_ladder(triggerIds=[6001], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[6002], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[6003], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[6004], visible=False, animationEffect=False)
        self.set_mesh(triggerIds=[4001], visible=True)
        self.set_mesh(triggerIds=[4002], visible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[30000372], questStates=[3]):
            return 전투만(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000372], questStates=[2]):
            return 퀘완료가능재입장(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000372], questStates=[1]):
            return 잠시대기_01(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 전투만(self.ctx)


class 전투만(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[115]):
            return 종료(self.ctx)

    def on_exit(self):
        self.set_ladder(triggerIds=[6001], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6002], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6003], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6004], visible=True, animationEffect=True)


class 잠시대기_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[121], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스퇴장_01(self.ctx)


class 보보스퇴장_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=보보스퇴장_03, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스퇴장_02(self.ctx)


class 보보스퇴장_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_2001')
        self.add_balloon_talk(spawnId=121, msg='$63000073_CS__63000073_MAIN__0$', duration=2500, delayTick=1000) # 책 틈에서 지내게 해줬으니, 소원 들어준 거야…

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보보스퇴장_03(self.ctx)


class 보보스퇴장_03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스퇴장_04(self.ctx)

    def on_exit(self):
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[121])


class 보보스퇴장_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=26300731, textId=26300731)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[115]):
            return 사다리등장_01(self.ctx)


class 사다리등장_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=26300731)
        self.set_ladder(triggerIds=[6001], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6002], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6003], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6004], visible=True, animationEffect=True)
        self.show_guide_summary(entityId=26300733, textId=26300733)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001385], stateValue=0):
            return 트렁크오픈_01(self.ctx)


class 트렁크오픈_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=26300733)
        self.create_monster(spawnIds=[122], animationEffect=False)
        self.set_mesh(triggerIds=[4001], visible=False)
        self.set_mesh(triggerIds=[4002], visible=True)
        self.show_guide_summary(entityId=26300732, textId=26300732)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[30000372], questStates=[2]):
            return 트렁크오픈_02(self.ctx)


class 퀘완료가능재입장(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[122], animationEffect=False)
        self.set_mesh(triggerIds=[4001], visible=False)
        self.set_mesh(triggerIds=[4002], visible=True)
        self.set_ladder(triggerIds=[6001], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6002], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6003], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[6004], visible=True, animationEffect=True)
        self.move_user(mapId=63000073, portalId=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 트렁크오픈_02(self.ctx)


class 트렁크오픈_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.hide_guide_summary(entityId=26300732)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 트렁크오픈_03(self.ctx)


class 트렁크오픈_03(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2002')
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트렁크오픈_04(self.ctx)


class 트렁크오픈_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=에이든퇴장_01, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에이든대화_01(self.ctx)


class 에이든대화_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_npc_emotion_sequence(spawnId=122, sequenceName='Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에이든대화_02(self.ctx)


class 에이든대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004359, msg='$63000073_CS__63000073_MAIN__1$', duration=2500, align='right', illustId='0') # 아… 머리야.\n이게 어떻게 된 일이지

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에이든대화_03(self.ctx)


class 에이든대화_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에이든대화_04(self.ctx)


class 에이든대화_04(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=2500)
        self.add_cinematic_talk(npcId=0, msg='$63000073_CS__63000073_MAIN__2$', duration=2500, align='right') # $npcName:11004359$이지?

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에이든대화_05(self.ctx)


class 에이든대화_05(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=2500)
        self.add_cinematic_talk(npcId=0, msg='$63000073_CS__63000073_MAIN__3$', duration=4500, align='right') # 네 동생, $npcName:11004354$$pp:가,이$ 마을에서 널 기다리고 있어.\n마을에서 같이 부모님을 찾아보자고 하는데.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에이든대화_06(self.ctx)


class 에이든대화_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에이든대화_07(self.ctx)


class 에이든대화_07(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=3500)
        self.add_cinematic_talk(npcId=11004359, msg='$63000073_CS__63000073_MAIN__4$', duration=3500, align='right', illustId='0') # …뭐라고?\n그럼… 나만 당한 게 아닌 건가?

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에이든대화_08(self.ctx)


class 에이든대화_08(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=4500)
        self.add_cinematic_talk(npcId=11004359, msg='$63000073_CS__63000073_MAIN__5$', duration=4500, align='right', illustId='0') # 어서 $npcName:11004354$$pp:를,을$ 만나봐야겠군.\n먼저 출발할게, 마을에서 보자.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에이든퇴장_01(self.ctx)


class 에이든퇴장_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[122])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 준비
