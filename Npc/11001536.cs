using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001536: Zuma
/// </summary>
public class _11001536 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0323002607005988$
    // - A lovely day for some exercise, don't you think? One-two, one-two! 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0323002607005991$
                // - The air is so bracing out here! Care to join me? 
                switch (selection) {
                    // $script:0323002607005992$
                    // - I, um... I like your hat.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0323002607005993$
                // - Aren't you a darling? I hear this is the hottest design in $map:02010002$ nowadays! My brother, $npcName:11000167[gender:0]$, picked it up for me. 
                switch (selection) {
                    // $script:0323002607005994$
                    // - You're lucky to have such a great brother.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0323002607005995$
                // - Don't I know it! He always looks out for me, even when he's off in the field. But lately, he hasn't been himself. Not since he had to give up hunting. 
                switch (selection) {
                    // $script:0323002607005996$
                    // - Why did $npcName:11000167[gender:0]$ give up hunting?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0323002607005997$
                // - His wife hates it. She got sick of him coming home with all manner of wounds. Of course I worry about him, too, but this is his calling. A man can't be happy if he can't follow his calling.
                return 33;
            case (33, 1):
                // $script:0323002607005998$
                // - Doesn't matter what I think, of course. $npcName:11000167[gender:0]$ agreed to stop hunting and go into business in $map:02000036$. He seems awful miserable to me, but what do I know? I'm just his sister. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
