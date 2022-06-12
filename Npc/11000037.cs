using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000037: Lea
/// </summary>
public class _11000037 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000200$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000203$
                // - One day, I'm going to go out and explore the world! You'll join me when I do, right $MyPCName$?
                return -1;
            case (40, 0):
                // $script:1130105307004657$
                // - I see you've brought me some $itemPlural:30000435$.
                switch (selection) {
                    // $script:1130105307004658$
                    // - Can you purify them?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1130105307004659$
                // - Well... You see, that needs some special purging magic... $npcName:11000031[gender:0]$ and the fairies think I'm too young to learn that kind of magic. They won't even let me gather $itemPlural:30000435$. 
                return 41;
            case (41, 1):
                // $script:1130105307004660$
                // - Even if I can't cast neat purifying spells, at least I can collect $itemPlural:30000435$ from adventurers like you. If I get enough flowers, maybe $npc:11000031[gender:0]$ will finally let me do the fun stuff. When he does, bring me more flowers, okay?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
