using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001023: Lennon
/// </summary>
public class _11001023 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003476$
    // - No...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003477$
                // - To let him slip through my fingers... After everything he put me through...
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
