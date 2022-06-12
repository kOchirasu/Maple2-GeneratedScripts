using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000847: Ozuma
/// </summary>
public class _11000847 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003099$
    // - What an interesting place.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003102$
                // - I believe more than one timeline exists in Ludibrium at this moment.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
