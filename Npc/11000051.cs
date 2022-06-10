using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000051: Ruki
/// </summary>
public class _11000051 : NpcScript {
    internal _11000051(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610000333$;$script:0831180610000334$
        // Id = 1;
        // TODO: RandomPick 10;20;30;40;50;60;70;80;90;100;110;120
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000332$ 
                // - ... 
                return true;
            case 1:
                // $script:0831180610000333$ 
                // - Ugh. This place makes me so uncomfortable.  Hmm... Your eyes... I can see you're a kindred spirit... How would you like to join us and walk among the shadows? 
                // $script:0831180610000334$ functionID=1 
                // - Happiness, anger, sadness, forgiveness—emotions are just baggage that gets in the way. Your enemies don't deserve your mercy.  
                return true;
            case 10:
                // $script:0831180610000335$ 
                // - Ugh. This place makes me so uncomfortable.  Hmm... Your eyes... I can see you're a kindred spirit...  You would probably feel at home among the shadows, but you're still too weak to join us.  
                switch (selection) {
                    // $script:0831180610000336$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000337$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180610000338$ 
                // - My kind is more comfortable in the shadows than in the light. In my line of work, standing around out in the open can get you killed.  
                return true;
            case 12:
                // $script:0831180610000339$ 
                // - Watching $npc:11000043[gender:1]$ over there trying to peddle her philosophy to anybody who makes eye contact... She's all about "doing good deeds and helping the weak." Hah. It makes me wanna hurl. 
                // $script:0831180610000340$ 
                // - She's too soft. You help the somebody who can't take care of themselves once, and they'll become reliant on you. Unless they learn how to fend for themselves, they'll never survive in this world. And maybe they don't deserve to. 
                return true;
            case 13:
                // $script:0607163510001546$ 
                // - You're the famed Gray Wolf. Look, let me give you some advice: watch your back. 
                switch (selection) {
                    // $script:0607163510001547$
                    // - Is that a threat?
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:0607163510001548$ 
                // - Think of it as a professional courtesy. Your name has been off and on our hit list for some time now. 
                switch (selection) {
                    // $script:0607163510001549$
                    // - Are you going to come after me, then?
                    case 0:
                        Id = 15;
                        return false;
                }
                return true;
            case 15:
                // $script:0607163510001550$ 
                // - Not me, no. I'm not foolish enough to tangle with the Gray Wolf. By the way, I never thought you'd come out of the shadows. That's a fascinating development. 
                switch (selection) {
                    // $script:0607181410001559$
                    // - Let's talk about something else.
                    case 0:
                        Id = 110;
                        return false;
                }
                return true;
            case 16:
                // $script:0806014810001673$ 
                // - What, do you want to hire me? 
                switch (selection) {
                    // $script:0806014810001674$
                    // - Can I hire you?
                    case 0:
                        Id = 17;
                        return false;
                }
                return true;
            case 17:
                // $script:0806014810001675$ 
                // - That depends. There are many things I need to consider, such as how much money you can afford. 
                // $script:0806014810001676$ 
                // - You can't hire me for just any sum.
Whom do you want me to take care of, anyway? What's the <font color="#ffd200">name</font>? 
                switch (selection) {
                    // $script:0806014810001677$
                    // - $npcName:11001559[gender:0]$.
                    case 0:
                        Id = 18;
                        return false;
                }
                return true;
            case 18:
                // $script:0806014810001678$ 
                // - ...I'm going to pretend that I didn't hear that. He's one of the greats. 
                switch (selection) {
                    // $script:0806014810001679$
                    // - Change the subject.
                    case 0:
                        Id = 120;
                        return false;
                }
                return true;
            case 20:
                // $script:0831180610000341$ 
                // - Ah, a fellow walker of the shadows. If you've made it this far, you should know there's no point helping those who can't help themselves. But you're not weak, are you? Well then, ask me your question. 
                switch (selection) {
                    // $script:0831180610000342$
                    // - What should I do now?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180610000345$ 
                // - If you want to survive in the shadows, you need to blend in $npc:11000004[gender:0]$ has some equipment that should work for you. Gear up, and never let them see you coming. 
                // $script:0831180610000346$ 
                // - Stay alive long enough, and eventually you'll reach a new level.
That's when you get to learn new skills.
To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> and open the <font color="#ffd200">Skill window</font>. 
                return true;
            case 22:
                // $script:0831180610000347$ 
                // - When you're ready to <font color="#ffd200">upgrade a skill</font>, just press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve.  
                // $script:0831180610000348$ 
                // - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$. 
                return true;
            case 23:
                // $script:0831180610000349$ 
                // - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>.  
                // $script:0831180610000350$ 
                // - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities. 
                // $script:0831180610000351$ 
                // - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently. 
                // $script:0831180610000352$ 
                // - And as for $itemPlural:40100022$... You're too weak to be worrying about those. 
                return true;
            case 30:
                // $script:0831180610000353$ 
                // - This place makes me uncomfortable. Hmm, you're a Knight...? I suppose that's not a bad choice. 
                switch (selection) {
                    // $script:0831180610000354$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000355$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 40:
                // $script:0831180610000356$ 
                // - This place makes me uncomfortable. Hmm, you're a Berserker...? I suppose that's not a bad choice. 
                switch (selection) {
                    // $script:0831180610000357$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000358$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 50:
                // $script:0831180610000359$ 
                // - This place makes me uncomfortable. Hmm, you're a Wizard...? I suppose that's not a bad choice. 
                switch (selection) {
                    // $script:0831180610000360$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000361$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 60:
                // $script:0831180610000362$ 
                // - This place makes me uncomfortable. Hmm, you're a Priest...? I suppose that's not a bad choice.  
                switch (selection) {
                    // $script:0831180610000363$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000364$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 70:
                // $script:0831180610000365$ 
                // - This place makes me uncomfortable. Hmm, you're an Archer...? I suppose that's not a bad choice. 
                switch (selection) {
                    // $script:0831180610000366$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000367$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 80:
                // $script:0831180610000368$ 
                // - This place makes me uncomfortable. Hmm, you're a Heavy Gunner...? I suppose that's not a bad choice. 
                switch (selection) {
                    // $script:0831180610000369$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000370$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 90:
                // $script:0831180610000371$ 
                // - This place makes me uncomfortable. Hmm, you're a Thief...? I suppose that's not a bad choice. 
                switch (selection) {
                    // $script:0831180610000372$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000373$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 100:
                // $script:1216124310001340$ 
                // - This place makes me uncomfortable. Hmm, you're a Runeblade...? I suppose that's not a bad choice. 
                switch (selection) {
                    // $script:1216124310001341$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:1216124310001342$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 110:
                // $script:0607163510001551$ 
                // - This place is making me uncomfortable. I mean, it's interesting, but it's not what I like. 
                switch (selection) {
                    // $script:0607163510001552$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0607163510001553$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                    // $script:0607163510001554$
                    // - Let's change the subject.
                    case 2:
                        Id = 13;
                        return false;
                }
                return true;
            case 120:
                // $script:0806014810001680$ 
                // - This place is making me uncomfortable. I mean, it's interesting, but it's not what I like. 
                switch (selection) {
                    // $script:0806014810001681$
                    // - What's making you so uncomfortable?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0806014810001682$
                    // - Is there something wrong?
                    case 1:
                        Id = 12;
                        return false;
                    // $script:0806020710001684$
                    // - Talk to $npcName:11000051[gender:1]$ about a different subject.
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
