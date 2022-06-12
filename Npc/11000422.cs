using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000422: Roanna's Tombstone
/// </summary>
public class _11000422 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407001763$
    // - <font color="#909090">(The headstone is old and worn, and there is an epitaph inscribed upon it.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001764$
                // - <i>Here lies Roanna Levematri. She leaves behind her lover Alberto, whose heart will never heal.</i>
                return -1;
            case (20, 0):
                // $script:0831180407001765$
                // - <i>Here lies Roanna Levematri. She leaves behind her lover Alberto, whose heart will never heal.</i>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
