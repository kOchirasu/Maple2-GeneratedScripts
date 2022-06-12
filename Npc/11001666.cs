using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001666: Frey
/// </summary>
public class _11001666 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0617211107006381$
    // - I look forward to hearing more stories of your heroism.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0617211107006382$
                // - Please remain steadfast in your efforts to protect peace and justice.
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
