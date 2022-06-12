using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004126: Fledgling Guard
/// </summary>
public class _11004126 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720130407010495$
    // - ...N-nothing to report!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720130407010496$
                // - Y-you're talking to me?
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
