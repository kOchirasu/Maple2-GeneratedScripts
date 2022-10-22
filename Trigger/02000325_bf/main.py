""" trigger/02000325_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10000739], state=2)
        set_interact_object(triggerIds=[10000740], state=2)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[611], visible=False)
        set_effect(triggerIds=[612], visible=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000752], state=0)
        set_interact_object(triggerIds=[13000009], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=True, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$02000325_BF__MAIN__0$', arg3='4000', arg4='0')
            return 어나운스02()

state.DungeonStart = DungeonStart


class 어나운스02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            set_event_ui(type=1, arg2='$02000325_BF__MAIN__1$', arg3='3500', arg4='0')
            return 어나운스03()


class 어나운스03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            set_event_ui(type=1, arg2='$02000325_BF__MAIN__2$', arg3='3500', arg4='0')
            return 라운드반응체크1()


class 라운드반응체크1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000752], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000752], arg2=0):
            set_effect(triggerIds=[601], visible=True)
            return 라운드카운트딜레이1()


class 라운드카운트딜레이1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 라운드카운트1()


class 라운드카운트1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[611], visible=True)
        set_effect(triggerIds=[612], visible=True)
        set_interact_object(triggerIds=[10000739], state=1)
        set_interact_object(triggerIds=[10000740], state=1)
        set_event_ui(type=0, arg2='1,3')
        show_count_ui(text='$02000325_BF__MAIN__3$', stage=1, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 라운드1()


class 라운드1(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return 소환3001()
        if random_condition(rate=5):
            return 소환3002()
        if random_condition(rate=5):
            return 소환3003()
        if random_condition(rate=5):
            return 소환3004()
        if random_condition(rate=5):
            return 소환3005()
        if random_condition(rate=5):
            return 소환3006()
        if random_condition(rate=5):
            return 소환3007()
        if random_condition(rate=5):
            return 소환3008()
        if random_condition(rate=5):
            return 소환3009()
        if random_condition(rate=5):
            return 소환3010()
        if random_condition(rate=5):
            return 소환3011()
        if random_condition(rate=5):
            return 소환3012()
        if random_condition(rate=5):
            return 소환3013()
        if random_condition(rate=5):
            return 소환3014()
        if random_condition(rate=5):
            return 소환3015()
        if random_condition(rate=5):
            return 소환3016()
        if random_condition(rate=5):
            return 소환3017()
        if random_condition(rate=5):
            return 소환3018()
        if random_condition(rate=5):
            return 소환3019()
        if random_condition(rate=5):
            return 소환3020()


class 소환3001(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)
        create_monster(spawnIds=[3001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3001]):
            return 라운드대기2()


class 소환3002(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002], arg2=False)
        create_monster(spawnIds=[3002], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3002]):
            return 라운드대기2()


class 소환3003(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003], arg2=False)
        create_monster(spawnIds=[3003], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3003]):
            return 라운드대기2()


class 소환3004(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2004], arg2=False)
        create_monster(spawnIds=[3004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3004]):
            return 라운드대기2()


class 소환3005(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2005], arg2=False)
        create_monster(spawnIds=[3005], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3005]):
            return 라운드대기2()


class 소환3006(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2006], arg2=False)
        create_monster(spawnIds=[3006], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3006]):
            return 라운드대기2()


class 소환3007(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2007], arg2=False)
        create_monster(spawnIds=[3007], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3007]):
            return 라운드대기2()


class 소환3008(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2008], arg2=False)
        create_monster(spawnIds=[3008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3008]):
            return 라운드대기2()


class 소환3009(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2009], arg2=False)
        create_monster(spawnIds=[3009], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3009]):
            return 라운드대기2()


class 소환3010(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2010], arg2=False)
        create_monster(spawnIds=[3010], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3010]):
            return 라운드대기2()


class 소환3011(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2011], arg2=False)
        create_monster(spawnIds=[3011], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3011]):
            return 라운드대기2()


class 소환3012(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2012], arg2=False)
        create_monster(spawnIds=[3012], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3012]):
            return 라운드대기2()


class 소환3013(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2013], arg2=False)
        create_monster(spawnIds=[3013], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3013]):
            return 라운드대기2()


class 소환3014(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2014], arg2=False)
        create_monster(spawnIds=[3014], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3014]):
            return 라운드대기2()


class 소환3015(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2015], arg2=False)
        create_monster(spawnIds=[3015], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3015]):
            return 라운드대기2()


class 소환3016(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2016], arg2=False)
        create_monster(spawnIds=[3016], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3016]):
            return 라운드대기2()


class 소환3017(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2017], arg2=False)
        create_monster(spawnIds=[3017], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3017]):
            return 라운드대기2()


class 소환3018(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2018], arg2=False)
        create_monster(spawnIds=[3018], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3018]):
            return 라운드대기2()


class 소환3019(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2019], arg2=False)
        create_monster(spawnIds=[3019], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3019]):
            return 라운드대기2()


class 소환3020(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2020], arg2=False)
        create_monster(spawnIds=[3020], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3020]):
            return 라운드대기2()


class 라운드대기2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000739], state=2)
        set_interact_object(triggerIds=[10000740], state=2)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[611], visible=False)
        set_effect(triggerIds=[612], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 어나운스04()


class 어나운스04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$02000325_BF__MAIN__4$', arg3='3500', arg4='0')
            return 라운드반응체크2()


class 라운드반응체크2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000752], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000752], arg2=0):
            set_effect(triggerIds=[601], visible=True)
            return 어나운스04_2()


class 어나운스04_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000325_BF__MAIN__5$', arg3='3500', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 라운드카운트2()


class 라운드카운트2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[612], visible=True)
        set_interact_object(triggerIds=[10000740], state=1)
        set_event_ui(type=0, arg2='2,3')
        show_count_ui(text='$02000325_BF__MAIN__6$', stage=2, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 라운드2()


class 라운드2(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return 소환체크3001()
        if random_condition(rate=5):
            return 소환체크3002()
        if random_condition(rate=5):
            return 소환체크3003()
        if random_condition(rate=5):
            return 소환체크3004()
        if random_condition(rate=5):
            return 소환체크3005()
        if random_condition(rate=5):
            return 소환체크3006()
        if random_condition(rate=5):
            return 소환체크3007()
        if random_condition(rate=5):
            return 소환체크3008()
        if random_condition(rate=5):
            return 소환체크3009()
        if random_condition(rate=5):
            return 소환체크3010()
        if random_condition(rate=5):
            return 소환체크3011()
        if random_condition(rate=5):
            return 소환체크3012()
        if random_condition(rate=5):
            return 소환체크3013()
        if random_condition(rate=5):
            return 소환체크3014()
        if random_condition(rate=5):
            return 소환체크3015()
        if random_condition(rate=5):
            return 소환체크3016()
        if random_condition(rate=5):
            return 소환체크3017()
        if random_condition(rate=5):
            return 소환체크3018()
        if random_condition(rate=5):
            return 소환체크3019()
        if random_condition(rate=5):
            return 소환체크3020()


class 소환체크3001(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2001]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2001]):
            return 소환2_3001()


class 소환체크3002(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2002]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2002]):
            return 소환2_3002()


class 소환체크3003(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2003]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2003]):
            return 소환2_3003()


class 소환체크3004(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2004]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2004]):
            return 소환2_3004()


class 소환체크3005(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2005]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2005]):
            return 소환2_3005()


class 소환체크3006(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2006]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2006]):
            return 소환2_3006()


class 소환체크3007(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2007]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2007]):
            return 소환2_3007()


class 소환체크3008(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2008]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2008]):
            return 소환2_3008()


class 소환체크3009(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2009]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2009]):
            return 소환2_3009()


class 소환체크3010(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2010]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2010]):
            return 소환2_3010()


class 소환체크3011(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2011]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2011]):
            return 소환2_3011()


class 소환체크3012(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2012]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2012]):
            return 소환2_3012()


class 소환체크3013(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2013]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2013]):
            return 소환2_3013()


class 소환체크3014(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2014]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2014]):
            return 소환2_3014()


class 소환체크3015(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2015]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2015]):
            return 소환2_3015()


class 소환체크3016(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2016]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2016]):
            return 소환2_3016()


class 소환체크3017(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2017]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2017]):
            return 소환2_3017()


class 소환체크3018(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2018]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2018]):
            return 소환2_3018()


class 소환체크3019(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2019]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2019]):
            return 소환2_3019()


class 소환체크3020(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2020]):
            return 라운드2()
        if not npc_detected(boxId=199, spawnIds=[2020]):
            return 소환2_3020()


class 소환2_3001(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)
        create_monster(spawnIds=[3001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3001]):
            return 라운드대기3()


class 소환2_3002(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002], arg2=False)
        create_monster(spawnIds=[3002], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3002]):
            return 라운드대기3()


class 소환2_3003(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003], arg2=False)
        create_monster(spawnIds=[3003], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3003]):
            return 라운드대기3()


class 소환2_3004(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2004], arg2=False)
        create_monster(spawnIds=[3004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3004]):
            return 라운드대기3()


class 소환2_3005(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2005], arg2=False)
        create_monster(spawnIds=[3005], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3005]):
            return 라운드대기3()


class 소환2_3006(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2006], arg2=False)
        create_monster(spawnIds=[3006], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3006]):
            return 라운드대기3()


class 소환2_3007(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2007], arg2=False)
        create_monster(spawnIds=[3007], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3007]):
            return 라운드대기3()


class 소환2_3008(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2008], arg2=False)
        create_monster(spawnIds=[3008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3008]):
            return 라운드대기3()


class 소환2_3009(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2009], arg2=False)
        create_monster(spawnIds=[3009], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3009]):
            return 라운드대기3()


class 소환2_3010(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2010], arg2=False)
        create_monster(spawnIds=[3010], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3010]):
            return 라운드대기3()


class 소환2_3011(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2011], arg2=False)
        create_monster(spawnIds=[3011], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3011]):
            return 라운드대기3()


class 소환2_3012(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2012], arg2=False)
        create_monster(spawnIds=[3012], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3012]):
            return 라운드대기3()


class 소환2_3013(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2013], arg2=False)
        create_monster(spawnIds=[3013], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3013]):
            return 라운드대기3()


class 소환2_3014(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2014], arg2=False)
        create_monster(spawnIds=[3014], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3014]):
            return 라운드대기3()


class 소환2_3015(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2015], arg2=False)
        create_monster(spawnIds=[3015], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3015]):
            return 라운드대기3()


class 소환2_3016(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2016], arg2=False)
        create_monster(spawnIds=[3016], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3016]):
            return 라운드대기3()


class 소환2_3017(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2017], arg2=False)
        create_monster(spawnIds=[3017], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3017]):
            return 라운드대기3()


class 소환2_3018(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2018], arg2=False)
        create_monster(spawnIds=[3018], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3018]):
            return 라운드대기3()


class 소환2_3019(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2019], arg2=False)
        create_monster(spawnIds=[3019], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3019]):
            return 라운드대기3()


class 소환2_3020(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2020], arg2=False)
        create_monster(spawnIds=[3020], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3020]):
            return 라운드대기3()


class 라운드대기3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[612], visible=False)
        set_interact_object(triggerIds=[10000740], state=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 어나운스05()


class 어나운스05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$02000325_BF__MAIN__7$', arg3='3500', arg4='0')
            return 라운드반응체크3()


class 라운드반응체크3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000752], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000752], arg2=0):
            set_effect(triggerIds=[601], visible=True)
            return 라운드카운트3()


class 라운드카운트3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[612], visible=False) # action name="메쉬를설정한다" arg1="3000-3022" arg2="0" arg3="0" arg4="200" arg5="2" /
        set_event_ui(type=0, arg2='3,3')
        show_count_ui(text='$02000325_BF__MAIN__9$', stage=3, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 라운드3()


class 라운드3(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return 소환체크2_3001()
        if random_condition(rate=5):
            return 소환체크2_3002()
        if random_condition(rate=5):
            return 소환체크2_3003()
        if random_condition(rate=5):
            return 소환체크2_3004()
        if random_condition(rate=5):
            return 소환체크2_3005()
        if random_condition(rate=5):
            return 소환체크2_3006()
        if random_condition(rate=5):
            return 소환체크2_3007()
        if random_condition(rate=5):
            return 소환체크2_3008()
        if random_condition(rate=5):
            return 소환체크2_3009()
        if random_condition(rate=5):
            return 소환체크2_3010()
        if random_condition(rate=5):
            return 소환체크2_3011()
        if random_condition(rate=5):
            return 소환체크2_3012()
        if random_condition(rate=5):
            return 소환체크2_3013()
        if random_condition(rate=5):
            return 소환체크2_3014()
        if random_condition(rate=5):
            return 소환체크2_3015()
        if random_condition(rate=5):
            return 소환체크2_3016()
        if random_condition(rate=5):
            return 소환체크2_3017()
        if random_condition(rate=5):
            return 소환체크2_3018()
        if random_condition(rate=5):
            return 소환체크2_3019()
        if random_condition(rate=5):
            return 소환체크2_3020()


class 소환체크2_3001(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2001]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2001]):
            return 소환3_3001()


class 소환체크2_3002(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2002]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2002]):
            return 소환3_3002()


class 소환체크2_3003(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2003]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2003]):
            return 소환3_3003()


class 소환체크2_3004(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2004]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2004]):
            return 소환3_3004()


class 소환체크2_3005(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2005]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2005]):
            return 소환3_3005()


class 소환체크2_3006(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2006]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2006]):
            return 소환3_3006()


class 소환체크2_3007(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2007]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2007]):
            return 소환3_3007()


class 소환체크2_3008(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2008]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2008]):
            return 소환3_3008()


class 소환체크2_3009(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2009]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2009]):
            return 소환3_3009()


class 소환체크2_3010(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2010]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2010]):
            return 소환3_3010()


class 소환체크2_3011(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2011]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2011]):
            return 소환3_3011()


class 소환체크2_3012(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2012]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2012]):
            return 소환3_3012()


class 소환체크2_3013(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2013]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2013]):
            return 소환3_3013()


class 소환체크2_3014(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2014]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2014]):
            return 소환3_3014()


class 소환체크2_3015(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2015]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2015]):
            return 소환3_3015()


class 소환체크2_3016(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2016]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2016]):
            return 소환3_3016()


class 소환체크2_3017(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2017]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2017]):
            return 소환3_3017()


class 소환체크2_3018(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2018]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2018]):
            return 소환3_3018()


class 소환체크2_3019(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2019]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2019]):
            return 소환3_3019()


class 소환체크2_3020(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=199, spawnIds=[2020]):
            return 라운드3()
        if not npc_detected(boxId=199, spawnIds=[2020]):
            return 소환3_3020()


class 소환3_3001(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)
        create_monster(spawnIds=[3001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3001]):
            return 미션성공()


class 소환3_3002(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002], arg2=False)
        create_monster(spawnIds=[3002], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3002]):
            return 미션성공()


class 소환3_3003(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003], arg2=False)
        create_monster(spawnIds=[3003], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3003]):
            return 미션성공()


class 소환3_3004(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2004], arg2=False)
        create_monster(spawnIds=[3004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3004]):
            return 미션성공()


class 소환3_3005(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2005], arg2=False)
        create_monster(spawnIds=[3005], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3005]):
            return 미션성공()


class 소환3_3006(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2006], arg2=False)
        create_monster(spawnIds=[3006], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3006]):
            return 미션성공()


class 소환3_3007(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2007], arg2=False)
        create_monster(spawnIds=[3007], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3007]):
            return 미션성공()


class 소환3_3008(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2008], arg2=False)
        create_monster(spawnIds=[3008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3008]):
            return 미션성공()


class 소환3_3009(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2009], arg2=False)
        create_monster(spawnIds=[3009], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3009]):
            return 미션성공()


class 소환3_3010(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2010], arg2=False)
        create_monster(spawnIds=[3010], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3010]):
            return 미션성공()


class 소환3_3011(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2011], arg2=False)
        create_monster(spawnIds=[3011], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3011]):
            return 미션성공()


class 소환3_3012(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2012], arg2=False)
        create_monster(spawnIds=[3012], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3012]):
            return 미션성공()


class 소환3_3013(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2013], arg2=False)
        create_monster(spawnIds=[3013], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3013]):
            return 미션성공()


class 소환3_3014(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2014], arg2=False)
        create_monster(spawnIds=[3014], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3014]):
            return 미션성공()


class 소환3_3015(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2015], arg2=False)
        create_monster(spawnIds=[3015], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3015]):
            return 미션성공()


class 소환3_3016(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2016], arg2=False)
        create_monster(spawnIds=[3016], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3016]):
            return 미션성공()


class 소환3_3017(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2017], arg2=False)
        create_monster(spawnIds=[3017], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3017]):
            return 미션성공()


class 소환3_3018(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2018], arg2=False)
        create_monster(spawnIds=[3018], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3018]):
            return 미션성공()


class 소환3_3019(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2019], arg2=False)
        create_monster(spawnIds=[3019], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3019]):
            return 미션성공()


class 소환3_3020(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2020], arg2=False)
        create_monster(spawnIds=[3020], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3020]):
            return 미션성공()


class 미션성공(state.State):
    def on_enter(self):
        set_achievement(triggerId=102, type='trigger', achieve='BraveRace')
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=True, arg3=0, arg4=200, arg5=2)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[612], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 라운드보상3()


class 라운드보상3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 포털생성()


class 포털생성(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            set_event_ui(type=0, arg2='0,0')
            dungeon_clear()
            return 종료()


class 종료(state.State):
    pass


