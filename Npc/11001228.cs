using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001228: Puri
/// </summary>
public class _11001228 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1118145206000544$
    // - Do you have any $itemPlural:90000014$? I'll trade you some amazing fairy treasures for them!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1118145206000547$
                // - There's not much to talk about. You got $itemPlural:90000014$, I've got treasures to trade. It's pretty simple, 'cause I just LOVE those fruits!
                switch (selection) {
                    // $script:1118145206000548$
                    // - What are $itemPlural:90000014$?
                    case 0:
                        return 31;
                    // $script:1118145206000549$
                    // - Why do you need $itemPlural:90000014$?
                    case 1:
                        return 32;
                    // $script:1118145206000550$
                    // - Can you really exchange fairy treasure for $itemPlural:90000014$?
                    case 2:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:1118145206000551$
                // - They're fruits that grow in the $map:2000350$. They also call them the Fruit of Darkness, since they grow rich off the intense darkness of the Shadow World. That's what makes 'em tasty!
                return -1;
            case (32, 0):
                // $script:1118145206000552$
                // - Well, $npcName:11000031[gender:0]$ and the guard fairies have been battling back the darkness pouring out of the $map:2000350$. Some of them got poisoned from $itemPlural:90000014$, and $npc:11000031[gender:0]$ said they need the same poison to recover.
                return 32;
            case (32, 1):
                // $script:1118145206000553$
                // - I'm collecting $item:90000014$ extract to make antidotes from. It, uh, also happens to be super tasty... so I need a lot. A LOT.
                return -1;
            case (33, 0):
                // $script:1118145206000554$
                // - Sure! No treasure is worth more than a life. My friends were hurt while protecting our forest, so I'll do whatever it takes to make them better!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
