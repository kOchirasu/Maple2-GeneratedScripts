using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000041: Rekk
/// </summary>
public class _11000041 : NpcScript {
    internal _11000041(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610000063$;$script:0831180610000064$
        // Id = 1;
        // TODO: RandomPick 10;20;30;40;50;60;70;80;90;100;110;120
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000062$ 
                // - Do you want to become a true warrior? 
                return true;
            case 1:
                // $script:0831180610000063$ 
                // - Argh, this place is so boring, it's driving me crazy! If it weren't for the War Chief's order, I would be cracking skulls on Vayar Mountain and having a blast! Hey, you look pretty tough. How are you in a fight? 
                // $script:0831180610000064$ functionID=1 
                // - With a greatsword in our hands, we're fearless in battle. We can be overzealous sometimes, but that's inevitable when you've got our passion for fighting. So, how'd you like to swear fealty to the War Chief and walk the path of the Berserker? 
                return true;
            case 10:
                // $script:0831180610000065$ 
                // - Argh, this place is so boring, it's driving me crazy! If it weren't for the War Chief's order, I would be cracking skulls on Vayar Mountain and having a blast! Hey, you look pretty tough. How are you in a fight? 
                switch (selection) {
                    // $script:0831180610000066$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000067$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180610000068$ 
                // - We wouldn't be able to survive the sunbaked steppes of $map:02000051$ if it weren't for our War Chief. He's a great warrior and greater leader. Our trust in him is unwavering. 
                // $script:0831180610000069$ 
                // - If you want to meet him, then go to $map:02000051$'s western plateau. But first, you'll have to get approval from his son and our vice chief, $npc:11000009[gender:0]$. 
                // $script:0831180610000070$ 
                // - Oh, and when you see him, just be yourself and be honest. He can tell instantly when you're hiding something. 
                return true;
            case 12:
                // $script:0831180610000071$ 
                // - You must not get around much if you haven't heard of Vayar Mountain. It's south of $map:02000051$. We named it after the giant golems that lurk inside. 
                // $script:0831180610000072$ 
                // - The golems, or Vayars, were created by the ancients to protect their sanctum. That was centuries ago, and the ancients are long gone. But the Vayars remain, protecting the mountain from any adventurers brave or foolish enough to enter. 
                // $script:0831180610000073$ 
                // - Speaking of which, I've heard rumors that someone evaded the 
Vayars' detection and snuck into the mountain. What was their name? I can't remember... 
                return true;
            case 20:
                // $script:0831180610000074$ 
                // - Sometimes in the heat of battle, I achieve inhuman feats simply because, in my rage, I forget fear and all my weaknesses. I wouldn't count that as a blessing, though... Some things are worth forgetting, but you must never forget who you are. Now, was there something you wanted to ask me? 
                switch (selection) {
                    // $script:0831180610000075$
                    // - What should I do now?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180610000078$ 
                // - First, arm yourself to the teeth. $npc:11000004[gender:0]$ is a merchant of fine equipment, and probably has some great Berserker equipment for sale. Gear up and head out to battle! 
                // $script:0831180610000079$ 
                // - Crush all the foes who stand before you, and you will soon grow to new levels. Then you will find yourself ready to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>. 
                return true;
            case 22:
                // $script:0831180610000080$ 
                // - Want to <font color="#ffd200">upgrade a skill</font>? Press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve.  
                // $script:0831180610000081$ 
                // - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$. 
                return true;
            case 23:
                // $script:0831180610000082$ 
                // - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>.  
                // $script:0831180610000083$ 
                // - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities. 
                // $script:0831180610000084$ 
                // - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently. 
                // $script:0831180610000085$ 
                // - There's also $itemPlural:40100022$, but I don't think you're ready for those just yet. 
                return true;
            case 30:
                // $script:0831180610000086$ 
                // - You've really chosen to become a Knight? I don't know what you'll accomplish waving a dinky sword like that around, but good luck surviving. 
                switch (selection) {
                    // $script:0831180610000087$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000088$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 40:
                // $script:0831180610000089$ 
                // - You've really chosen to become a Knight? I don't really see how shouting gibberish from musty old tomes is going to keep you alive in battle, but I won't tell you how to live what's left of your life. 
                switch (selection) {
                    // $script:0831180610000090$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000091$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 50:
                // $script:0831180610000092$ 
                // - A priest? You've chosen to be a Priest? A fat lot of good prayer is going to do you against a horde of charging Koborcs. 
                switch (selection) {
                    // $script:0831180610000093$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000094$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 60:
                // $script:0831180610000095$ 
                // - You've really chosen to become an Archer? Striking down hapless foes from a distance is great, until your quiver runs dry. When the enemy comes bearing down on you, you'll wish you'd gone with a blade. 
                switch (selection) {
                    // $script:0831180610000096$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000097$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 70:
                // $script:0831180610000098$ 
                // - You've chosen to become a Heavy Gunner, of all things? Guns are a crutch of the cowardly. A true warrior faces their opponent head on. Don't look to me when that cannon jams in the heat of battle. 
                switch (selection) {
                    // $script:0831180610000099$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000100$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 80:
                // $script:0831180610000101$ 
                // - You've chosen to become a Thief? Throwing your only weapons at the enemy seems like a foolhardy strategy, but who am I to stand in the way of a someone with a deathwish? 
                switch (selection) {
                    // $script:0831180610000102$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000103$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 90:
                // $script:0831180610000104$ 
                // - You've chosen to become an Assassin? Skulking around in the shadows, hoping to strike without being seen... There's no honor in that. 
                switch (selection) {
                    // $script:0831180610000105$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000106$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 100:
                // $script:1216124310001322$ 
                // - You've chosen to become a Runeblade? To split one's focus between two completely different arts in the midst of battle seems like a reckless strategy. Perhaps you'll prove me wrong by not dying. 
                switch (selection) {
                    // $script:1216124310001323$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:1216124310001324$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 110:
                // $script:0607163510001501$ 
                // - I sense your fighting spirit is akin to the rage that fuels us Berserkers. A fire that burns within the soul and cannot be quenched! Some advice from one warrior to another: never let your anger get the better of you on the battlefield, or you might wind up dead. 
                switch (selection) {
                    // $script:0607163510001502$
                    // - Tell me about the War Chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0607163510001503$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 120:
                // $script:0806014810001598$ 
                // - The rage that fuels us Berserkers is a hot and roiling one that scorches the soul. And I can see it's just not in you. You're just like everyone else... you'll never know what it feels like to be truly alive. 
                switch (selection) {
                    // $script:0806014810001599$
                    // - Tell me about the war chief.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0806014810001600$
                    // - Tell me about Vayar Mountain.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
