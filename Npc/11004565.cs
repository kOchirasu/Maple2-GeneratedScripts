using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004565: Ophelia
/// </summary>
public class _11004565 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220211107014536$
    // - Hm.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014537$
                // - No offense, but I'm not here on business, okay? You're gonna have to find someone else to enchant your gear.
                switch (selection) {
                    // $script:0220211107014538$
                    // - Relax. I'm just here to say hi.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0220211107014539$
                // - Huh? You mean... You're not just talking to me because I'm a genius blacksmith?
                switch (selection) {
                    // $script:0220211107014540$
                    // - There's more to you than that.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0220211107014541$
                // - L-like what?
                switch (selection) {
                    // $script:0220211107014542$
                    // - Well, for example, your... Never mind.
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0220211107014543$
                // - I know you're trying to cheer me up, but I feel oddly insulted...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
