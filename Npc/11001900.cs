using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001900: Lennon
/// </summary>
public class _11001900 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1122193107007458$
    // - Eve was right...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1122193107007461$
                // - We've got to hold out long enough for Eve to get reinforcements.
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
