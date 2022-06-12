using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004469: Indica
/// </summary>
public class _11004469 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012119$
    // - That little cretin wants to go out and play...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012120$
                // - That little cretin wants to go out and play...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
