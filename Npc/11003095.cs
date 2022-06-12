using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003095: Oska
/// </summary>
public class _11003095 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0207122607007942$
    // - $MyPCName$, you came.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0207122607007943$
                // - The Green Hood will always protect you.
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
