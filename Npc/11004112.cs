using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004112: Mysterious Bladesman
/// </summary>
public class _11004112 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010467$
    // - Focus on the task ahead.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010468$
                // - If you have something to say to me, say it now.
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
