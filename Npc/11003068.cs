using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003068: Surnuny
/// </summary>
public class _11003068 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0102155907007655$
    // - Your Majesty...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0102155907007656$
                // - There are a great many things left to do. We should leave, for our next destination will be challenging.
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
