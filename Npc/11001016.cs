using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001016: Kenken
/// </summary>
public class _11001016 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003463$
    // - This place belongs to me now!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003466$
                // - Ahem, excuse me. Do you know how expensive these clothes I'm wearing are? 
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
