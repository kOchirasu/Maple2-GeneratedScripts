""" trigger/63000074_cs/63000074_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        set_mesh(triggerIds=[4001], visible=True, arg3=0, arg4=0, arg5=0) # 루돌프켜기
        set_mesh(triggerIds=[4002], visible=True, arg3=0, arg4=0, arg5=0) # 화분켜기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[30000370], questStates=[2]):
            return moveto63000072()
        if quest_user_detected(boxIds=[9000], questIds=[30000370], questStates=[1]):
            return Diary_ready()
        if not quest_user_detected(boxIds=[9000], questIds=[30000370], questStates=[1]):
            return scene_fin()


class Diary_ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불끄기
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Diary_set()


class Diary_set(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        set_mesh(triggerIds=[4001], visible=False, arg3=0, arg4=0, arg5=0) # 루돌프끄기
        set_mesh(triggerIds=[4002], visible=False, arg3=0, arg4=0, arg5=0) # 화분끄기
        move_user(mapId=63000074, portalId=10)
        select_camera(triggerId=8000, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Diary_start()


class Diary_start(state.State):
    def on_enter(self):
        set_scene_skip(state=sceneskip_1, arg2='exit') # setsceneskip 1 set
        set_cinematic_ui(type=9, script='$63000074_CS__63000074_MAIN__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Evelyn_monologue_00()


class Evelyn_monologue_00(state.State):
    def on_enter(self):
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Evelyn_monologue_01()


class Evelyn_monologue_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004354, msg='$63000074_CS__63000074_MAIN__1$', duration=4000, illustId='Evelyn_normal', align='center') # 아~ 정말. 맘에 드는 게 하나도 없어.\n어릴 때가 편했는데… 그렇지, 보?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Evelyn_monologue_02()


class Evelyn_monologue_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기
        select_camera_path(pathIds=[8000], returnView=False)
        add_cinematic_talk(npcId=11004354, msg='$63000074_CS__63000074_MAIN__2$', duration=4000, illustId='Evelyn_sad', align='right') # …휴. 내가 이상해졌나 봐.\n어린애일 때 찾던 요정 이름이나 부르고.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Evelyn_monologue_03()


class Evelyn_monologue_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        add_cinematic_talk(npcId=11004354, msg='$63000074_CS__63000074_MAIN__3$', duration=5000, illustId='Evelyn_sad', align='right') # 하지만… 쓸쓸한걸.\n너라도 있으면, 크리스마스가 슬프진 않을 텐데.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Evelyn_monologue_04()


class Evelyn_monologue_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)
        add_cinematic_talk(npcId=11004354, msg='$63000074_CS__63000074_MAIN__4$', duration=3500) # …그만 자야겠다.
        move_npc(spawnId=101, patrolName='MS2PatrolData')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return bobos_ready()


class bobos_ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return bobos_01()


class bobos_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$63000074_CS__63000074_MAIN__5$') # 슬프면 안 돼, $npcName:11004345$…\n그런 건 싫어.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return bobos_02()


class bobos_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$63000074_CS__63000074_MAIN__6$') # $npcName:11004345$ &lt;FONT color='#ffd200'&gt;소원…&lt;/FONT&gt; 들어줄게.\n\n그럼 $npcName:11004345$, 행복해지고\n나는… &lt;FONT color='#ffd200'&gt;루돌프&lt;/FONT&gt;가 될 수 있다.
        set_mesh(triggerIds=[4001], visible=True, arg3=0, arg4=0, arg5=0) # 루돌프켜기
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return rednose_01()


class rednose_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        select_camera_path(pathIds=[8003], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return rednose_02()


class rednose_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return rednose_03()


class sceneskip_1(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return rednose_03()


class rednose_03(state.State):
    def on_enter(self):
        set_achievement(triggerId=9000, type='trigger', achieve='LonelyEvelyn')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return moveto63000072()


class moveto63000072(state.State):
    def on_enter(self):
        move_user(mapId=63000072, portalId=11)


class moveto63000072_2(state.State):
    def on_enter(self):
        move_user(mapId=63000072, portalId=11)


class scene_fin(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


