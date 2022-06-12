using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001179: Aliyar
/// </summary>
public class _11001179 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:1014150507004104$
    // - Good day!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1014150507004107$
                // - <font color="#ffd200">Yalario!</font> 
                //   I love talking to new people and visiting new places. It's a pleasure to meet you.
                return 30;
            case (30, 1):
                // $script:1014154907004140$
                // - Ah, an adventurer! Know of any famous monsters around here? I may be a merchant, but I'm just as interested in fighting monsters as selling things. Hahaha!
                switch (selection) {
                    // $script:1014150507004108$
                    // - Yala-what-io?
                    case 0:
                        return 31;
                    // $script:1014150507004109$
                    // - That doesn't sound so great for business...
                    case 1:
                        return 32;
                    // $script:1014150507004110$
                    // - Where exactly are you from?
                    case 2:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:1014150507004111$
                // - Oh! Forgive me. Sometimes I forget that I am in <i>a foreign land</i>. Where I come from, 'Yalario' is the term we use when meeting someone for the first time. It means "<b>new friend</b>".
                return -1;
            case (32, 0):
                // $script:1014150507004112$
                // - Hahaha! Perhaps not. Truthfully, I am interested in both. Encountering new monsters inspires me to create new products! Mine is a dangerous business, ahahaha!
                return 32;
            case (32, 1):
                // $script:1014150507004113$
                // - I've sailed around the globe doing battle with all kinds of monsters. You'll find I am as shrewd a warrior as a merchant!
                switch (selection) {
                    // $script:1014150507004114$
                    // - You're not afraid of monsters?
                    case 0:
                        return 34;
                }
                return -1;
            case (33, 0):
                // $script:1014150507004115$
                // - Far, far across the sea. I haven't seen a single map here which includes my homeland. I have spent half my life sailing around the world, but I had never heard of this 'Wictoria Isslind' until I set foot upon it.
                return -1;
            case (34, 0):
                // $script:1014150507004116$
                // - Not at all. The people here make a big deal about how dangerous monsters are. But compared to back home, they are as cuddly as teddy bears. I am still hopeful that I will find a worthy challenge.
                return -1;
            case (40, 0):
                // $script:1026143107004286$
                // - Yalario! How may I help you? If merchandise is what you seek, please browse at your leisure.
                switch (selection) {
                    // $script:1026143107004287$
                    // - Do you know anything about Cynodia ore?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1026143107004288$
                // - Ah, I know of Cynodia ore. It is filled with mystical power and said to be able to bring balance to unstable magic.
                switch (selection) {
                    // $script:1026143107004289$
                    // - Do you know where I can find Cynodia ore?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1026143107004290$
                // - Hmm... I'm sorry, but they aren't something we carry. Come to think of it, $npcName:11001180[gender:1]$ or $npcName:11001181[gender:0]$ might know where to find some. Why don't you try speaking with them?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
