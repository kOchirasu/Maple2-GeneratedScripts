using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004118: Royal Watchman
/// </summary>
public class _11004118 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010479$
    // - If I see anything unusual, I'll report in right away!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010480$
                // - The blast area was pretty big...
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
