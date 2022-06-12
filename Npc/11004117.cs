using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004117: Guardsman
/// </summary>
public class _11004117 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010477$
    // - Nothing to report, $male:sir,female:ma'am$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010478$
                // - To suddenly appear in a place like this...
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
