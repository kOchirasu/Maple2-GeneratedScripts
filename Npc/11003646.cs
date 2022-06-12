using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003646: Nikki
/// </summary>
public class _11003646 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009176$
    // - Hop hop!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009177$
                // - Hi-hi! I'm $npcName:11003646$ the Bunny!
                switch (selection) {
                    // $script:1109121007009178$
                    // - Hello there, fluffy rabbit!
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009179$
                // - Ahem. Youse the mug Schatten sent? Here's the code phrase: "The square looks at the flower twice."
                switch (selection) {
                    // $script:1109121007009180$
                    // - Uh... What?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009181$
                // - Hop hop!
                switch (selection) {
                    // $script:1109121007009182$
                    // - W-wait... What did you say?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009183$
                // - I didn't say anything, you silly goose! Run along now!
                switch (selection) {
                    // $script:1109121007009184$
                    // - Uh...
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009185$
                // - Hop hop!
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
