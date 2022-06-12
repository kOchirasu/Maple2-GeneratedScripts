using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003467: Screaming Fist
/// </summary>
public class _11003467 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008671$
    // - You need to settle down.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008672$
                // - Don't start any trouble.
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
