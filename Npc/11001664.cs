using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001664: Luanna
/// </summary>
public class _11001664 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0617211107006376$
    // - May the empress favor you always.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0617211107006377$
                // - Do not betray our empress's trust. 
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
