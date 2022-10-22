""" trigger/52100303_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066], visible=False)
        set_mesh(triggerIds=[4002,4003,4004], visible=False)
        set_mesh(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025,5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039,5040,5041,5042,5043,5044,5045,5046,5047,5048,5049,5050,5051,5052,5053,5054,5055,5056,5057,5058,5059,5060,5061,5062,5063,5064,5065,5066,5067,5068,5069,5070,5071,5072,5073,5074,5075,5076,5077,5078,5079,5080,5081,5082,5083,5084,5085,5086,5087,5088,5089,5090,5091,5092,5093,5094,5095,5096,5097,5098,5099,5100,5101,5102,5103,5104,5105,5106,5107,5108,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5121,5122,5123,5124,5125,5126,5127,5128,5129,5130,5131,5132], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 티마이온등장()


class 티마이온등장(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$52100303_QD__MAIN__0$', duration=3000)
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            set_achievement(type='trigger', achieve='KillTimaion')
            destroy_monster(spawnIds=[111])
            return 종료대기()


class 종료대기(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004715, illust='Eone_normal', script='$52100303_QD__MAIN__1$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)


