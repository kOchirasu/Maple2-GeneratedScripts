using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004384: Boris
/// </summary>
public class _11004384 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011815$
    // - The kids sure do love the holidays...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011816$
                // - The kids really love the holidays...
                switch (selection) {
                    // $script:1109213607011817$
                    // - Not just kids though. Adults love the holidays, too, don't they?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109213607011818$
                // - Ehh, it depends. Easier for adults to lose the spirit of the season, I think.
                switch (selection) {
                    // $script:1109213607011819$
                    // - Well, happy holidays!
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109213607011820$
                // - Agreed! Happy holidays! Remind everyone that this is a season for joy!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
