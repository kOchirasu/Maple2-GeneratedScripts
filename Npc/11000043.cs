using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000043: Trini
/// </summary>
public class _11000043 : NpcScript {
    internal _11000043(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610000150$;$script:0831180610000151$
        // Id = 1;
        // TODO: RandomPick 10;20;30;40;50;60;70;80;90;100;110;120
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000149$ 
                // - How may I help you?
                return true;
            case 1:
                // $script:0831180610000150$ 
                // - The recent earthquake has struck fear into the hearts of many. We restore the people's hope by spreading the goddess's teachings. Would you join us on our holy mission? You seem more than qualified to serve the goddess.
                // $script:0831180610000151$ functionID=1 
                // - Illuminate this world with your good heart and unshakable faith.
                //   The goddess awaits with open arms all who you will shepherd into the light.
                return true;
            case 10:
                // $script:0831180610000152$ 
                // - The recent earthquake has struck fear into the hearts of many. We restore the people's hope by spreading the goddess's teachings. Would you join us on our holy mission? 
                switch (selection) {
                    // $script:0831180610000153$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000154$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180610000155$ 
                // - The road between $map:02000062$ and $map:02000001$ bore the brunt of the earthquake's damage. Fortunately, the road was nearly deserted when the shaking began.
                // $script:0831180610000156$ 
                // - I know that many are disappointed about the court's cancellation, but I think the can all agree that our current focus should be on supporting one another, and dealing with the damage of the quake.
                return true;
            case 12:
                // $script:0831180610000157$ 
                // - Oh, what a silly question! She's the empress, of course. $npc:11000075[gender:1]$ was surely just as disappointed about the court as everyone else, but her safety is paramount to Maple World.
                // $script:0831180610000158$ 
                // - If you're here for an audience with the Empress, you might as well go home. She's too busy these days governing the realm. Since the incident, the people have relied on her strong leadership more than ever.
                return true;
            case 13:
                // $script:0607163510001511$ 
                // - $MyPCName$, do you believe in... the Light?
                switch (selection) {
                    // $script:0607163510001512$
                    // - I only believe in what I can see.
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:0607163510001513$ 
                // - The Light shines on everyone, regardless of their belief or lack of belief.
                switch (selection) {
                    // $script:0607163510001514$
                    // - What's the Light ever done for the poor of $map:02000100$?
                    case 0:
                        Id = 15;
                        return false;
                }
                return true;
            case 15:
                // $script:0607163510001515$ 
                // - I believe the ordeals we experience throughout life are ultimately blessings in disguise, arranged by the Light. Hardship happens for a reason. I shall pray for you and everyone else. May the Light's blessing be with you wherever you go.
                switch (selection) {
                    // $script:0607163510001516$
                    // - Let's talk about something else.
                    case 0:
                        Id = 110;
                        return false;
                }
                return true;
            case 16:
                // $script:0806014810001620$ 
                // - $MyPCName$, do you believe in... the Light?
                switch (selection) {
                    // $script:0806014810001621$
                    // - What do you mean by "the light"?
                    case 0:
                        Id = 17;
                        return false;
                }
                return true;
            case 17:
                // $script:0806014810001622$ 
                // - The Light <font color="#ffd200">shines on everyone</font>, regardless of their belief or lack of belief.
                //   It <font color="#ffd200">guides</font> you through the darkness, keeping you from wandering astray.
                switch (selection) {
                    // $script:0806014810001623$
                    // - No light has ever guided me.
                    case 0:
                        Id = 18;
                        return false;
                }
                return true;
            case 18:
                // $script:0806014810001624$ 
                // - You just haven't noticed it. I can see it all around you, though it is rather dim.
                // $script:0806014810001625$ 
                // - You may not realize it, but that warm light is guiding you along your path.
                //   <font color="#909090">(You think <i>that's</i> a rich presumption. Doesn't this person know that this light has nothing to do with you? Your guide is the Lone Spirit and the Master's teachings.)</font>
                switch (selection) {
                    // $script:0806014810001626$
                    // - Change the subject.
                    case 0:
                        Id = 120;
                        return false;
                }
                return true;
            case 20:
                // $script:0831180610000159$ 
                // - Don't forget, you're now an agent of the Empress and, by extension, an agent of the goddess. It is your duty to perform good deeds and help the weak. Now, do you have any questions?
                switch (selection) {
                    // $script:0831180610000160$
                    // - What should I do now?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180610000163$ 
                // - To help the weak and needy, you yourself must be strong. $npc:11000004[gender:0]$ is a merchant of fine equipment, and probably has some excellent Priest gear for sale. Once you're properly equipped, you should venture forth and enact the will of the goddess.
                // $script:0831180610000164$ 
                // - In your service to the goddess, you'll inevitably reach new levels. When this happens you'll be able to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
                return true;
            case 22:
                // $script:0831180610000165$ 
                // - Press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
                // $script:0831180610000166$ 
                // - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
                return true;
            case 23:
                // $script:0831180610000167$ 
                // - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>.
                // $script:0831180610000168$ 
                // - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
                // $script:0831180610000169$ 
                // - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently.
                // $script:0831180610000170$ 
                // - $itemPlural:40100022$, you are dangerous, and must be handled with care.
                return true;
            case 30:
                // $script:0831180610000171$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Knight. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0831180610000172$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000173$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 40:
                // $script:0831180610000174$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Berserker. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0831180610000175$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000176$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 50:
                // $script:0831180610000177$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Wizard. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0831180610000178$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000179$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 60:
                // $script:0831180610000180$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Archer. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0831180610000181$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000182$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 70:
                // $script:0831180610000183$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Heavy Gunner. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0831180610000184$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000185$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 80:
                // $script:0831180610000186$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Thief. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0831180610000187$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000188$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 90:
                // $script:0831180610000189$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Assassin. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0831180610000190$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000191$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 100:
                // $script:1216124310001328$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Runeblade. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:1216124310001329$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:1216124310001330$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 110:
                // $script:0607163510001517$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen your path. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0607163510001518$
                    // - Did the earthquake cause a lot of damage?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0607163510001519$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                    // $script:0607163510001520$
                    // - Let's change the subject.
                    case 2:
                        Id = 13;
                        return false;
                }
                return true;
            case 120:
                // $script:0806014810001627$ 
                // - I'm afraid you cannot join the priesthood, as you've already chosen your path. Nonetheless, I pray for your prosperity.
                switch (selection) {
                    // $script:0806014810001628$
                    // - How bad was the quake?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0806014810001629$
                    // - Who is $npc:11000075[gender:1]$?
                    case 1:
                        Id = 12;
                        return false;
                    // $script:0806014810001630$
                    // - Talk to $npcName:11000043[gender:1]$ about a different subject.
                    case 2:
                        Id = 16;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
