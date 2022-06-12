using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000293: Ellbo
/// </summary>
public class _11000293 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001167$
    // - What brings you to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001170$
                // - Want to know how I keep my fur so shiny?
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
