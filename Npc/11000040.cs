using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000040: Rovey
/// </summary>
public class _11000040 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 10;20;30;40;50;60;70;80;90;100;110;120
    }

    // Select 0:
    // $script:0831180610000019$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610000020$
                // - Everyone wants to join the Royal Guard, but very few are actually qualified. It is imperative that Royal Guard members be strong in body and spirit, for we are the Empress's last line of defense. Hmm, I must admit, you do seem fairly strong. 
                return 1;
            case (1, 1):
                // functionID=1 
                // $script:0831180610000021$
                // - We're always looking for great swordsmen with the strength to protect the Empress and her palace. How'd you like to join the Royal Guard?
                return -1;
            case (10, 0):
                // $script:0831180610000022$
                // - In times like this, only we can protect Her Majesty and Minister $npcName:11000074[gender:0]$.  It's the most important job in the world. After you've grown a bit stronger, you should consider joining the Royal Guard.
                switch (selection) {
                    // $script:0831180610000023$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0831180610000024$
                    // - Who is $npc:11000074[gender:0]$?
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:0831180610000025$
                // - We royal guards protect the palace under the command of Minister $npcName:11000074[gender:0]$. Even though the much-awaited court was canceled because of the earthquake, there is no price too high when it comes to keeping the empress safe. We must honor our oath to protect her from anything, or anyone, that would do her harm.
                return -1;
            case (12, 0):
                // $script:0831180610000026$
                // - Don't tell me you've never heard of Minister $npcName:11000074[gender:0]$? 
                return 12;
            case (12, 1):
                // $script:0831180610000027$
                // - Hmm. I knew people had traveled far and wide to attend the royal court, but you must have come from <i>very</i> far away to be so ignorant of the recent happenings in $map:02000001$. 
                return 12;
            case (12, 2):
                // $script:0831180610000028$
                // - I'm quite busy at the moment, but I'm sure there are plenty of people in $map:02000001$ who would be happy to educate you.
                return -1;
            case (20, 0):
                // $script:1128171910001801$
                // - Remember, no longer are you some aimless adventure wandering the land, but rather a proud Knight and defender of the realm! Now, are there any questions you'd like answered?
                switch (selection) {
                    // $script:1128171910001802$
                    // - What should I do now?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180610000033$
                // - As it stands, you're too weak to fend for yourself, let alone protect the Empress.  $npc:11000004[gender:0]$ is a merchant of fine equipment, and probably has some excellent Knight gear for sale. Go get suited up, and commence your training beyond the walls of $map:02000001$!
                return 21;
            case (21, 1):
                // $script:0831180610000034$
                // - As you train, you'll ascend to new levels, and become ready to learn new skills. To see the skills you can learn, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
                return -1;
            case (22, 0):
                // $script:0831180610000035$
                // - Want to <font color="#ffd200">upgrade a skill</font>? Press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
                return 22;
            case (22, 1):
                // $script:0831180610000036$
                // - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
                return -1;
            case (23, 0):
                // $script:0831180610000037$
                // - <font color="#ffd200">Upgrading skills</font> requires Crystals. 
                return 23;
            case (23, 1):
                // $script:0831180610000038$
                // - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
                return 23;
            case (23, 2):
                // $script:0831180610000039$
                // - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently.
                return 23;
            case (23, 3):
                // $script:0831180610000040$
                // - As for $itemPlural:40100022$, I don't think you're quite ready.
                return -1;
            case (30, 0):
                // $script:0831180610000041$
                // - You passed up your opportunity to join the Royal Guard to become a... Berserker? Well, I hope you don't regret your decision. 
                switch (selection) {
                    // $script:0831180610000042$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0831180610000043$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (40, 0):
                // $script:0831180610000044$
                // - You passed up your opportunity to join the Royal Guard to become a... Wizard? Well, I hope you don't regret your decision. 
                switch (selection) {
                    // $script:0831180610000045$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0831180610000046$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (50, 0):
                // $script:0831180610000047$
                // - You passed up your opportunity to join the Royal Guard to become a... Priest? I suppose they have their own role to play on the battlefield. Well, I hope you don't regret your decision. 
                switch (selection) {
                    // $script:0831180610000048$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0831180610000049$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (60, 0):
                // $script:0831180610000050$
                // - You passed up your opportunity to join the Royal Guard to become an... Archer? Well, I hope you don't regret your decision. 
                switch (selection) {
                    // $script:0831180610000051$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0831180610000052$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (70, 0):
                // $script:0831180610000053$
                // - You passed up your opportunity to join the Royal Guard to become a... Heavy Gunner? Well, I hope you don't regret your decision. 
                switch (selection) {
                    // $script:0831180610000054$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0831180610000055$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (80, 0):
                // $script:0831180610000056$
                // - You passed up your opportunity to join the Royal Guard to become a... Thief? What a dishonorable profession. Perhaps you weren't cut out for the job in the first place. 
                switch (selection) {
                    // $script:0831180610000057$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0831180610000058$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (90, 0):
                // $script:0831180610000059$
                // - You passed up your opportunity to join the Royal Guard to become an... Assassin? You'd better not be conducting any business in our fair city unless you want to spend the rest of your life rotting in the dungeon. 
                switch (selection) {
                    // $script:0831180610000060$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0831180610000061$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (100, 0):
                // $script:1216124310001319$
                // - If I'm not mistaken, you're a Runeblade—a warrior versed both in swordplay and runic magic. I'm skeptical on whether you can really master both, but it's noble of you to try. In any case, you're quite far from home. Did you have any questions I can answer?
                switch (selection) {
                    // $script:1216124310001320$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:1216124310001321$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (110, 0):
                // $script:0607163510001498$
                // - Ah, yes, I've heard of you. Your methods are a bit unrefined, but you have a sense of determination paralleled by only the greatest Knights. It's too bad, we could use someone like you in the Royal Guard.
                switch (selection) {
                    // $script:0607163510001499$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0607163510001500$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
            case (120, 0):
                // $script:0806014810001595$
                // - I'm sorry, but I don't believe you possess the necessary qualifications to join the Royal Guard. The job requires great stores of both fortitude and determination, and it's my assessment that you possess neither.
                switch (selection) {
                    // $script:0806014810001596$
                    // - Tell me about the Royal Guard.
                    case 0:
                        return 11;
                    // $script:0806014810001597$
                    // - Who is $npc:11000074[gender:0]$? 
                    case 1:
                        return 12;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.Next,
            (12, 2) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Next,
            (21, 1) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Next,
            (22, 1) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Next,
            (23, 1) => NpcTalkButton.Next,
            (23, 2) => NpcTalkButton.Next,
            (23, 3) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.SelectableDistractor,
            (80, 0) => NpcTalkButton.SelectableDistractor,
            (90, 0) => NpcTalkButton.SelectableDistractor,
            (100, 0) => NpcTalkButton.SelectableDistractor,
            (110, 0) => NpcTalkButton.SelectableDistractor,
            (120, 0) => NpcTalkButton.SelectableDistractor,
            (1, 0) => NpcTalkButton.Next,
            (1, 1) => NpcTalkButton.ChangeJob,
            _ => NpcTalkButton.None,
        };
    }
}
