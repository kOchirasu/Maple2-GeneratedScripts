using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004252: Arte
/// </summary>
public class _11004252 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0829171107010964$
    // - Looks like another day with no luck. Hm? Who are you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0829171107010965$
                // - Looks like another day with no luck. Hm? Who are you?
                switch (selection) {
                    // $script:0831123907010999$
                    // - No one important. I'm just passing through.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0831123907011000$
                // - You're either brave or real dumb, to come all the way out here. Anyway, my name's $npcName:11004252[gender:1]$. I'm here observing.
                switch (selection) {
                    // $script:0831123907011001$
                    // - Observing what?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0831123907011002$
                // - Observing the movements of $npcName:11001813[gender:0]$'s army. He's one of the Seven Commanders, you know, and I have it on good authority that he often sends his troops through $map:03000115$ and $map:03000118$.
                switch (selection) {
                    // $script:0831123907011003$
                    // - Are you sure that's wise?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0831123907011004$
                // - Pfft, I'm not scared. I have family in Maple World, and I'll do anything I can to keep them safe, including marching right up to $npcName:11001813[gender:0]$ and stopping him right here and now.
                switch (selection) {
                    // $script:0831143807011039$
                    // - Thanks.
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:0831143807011040$
                // - No need to thank me. I'm happy if my family is happy. You should keep it up, too.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
