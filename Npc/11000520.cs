using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000520: Poron
/// </summary>
public class _11000520 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002227$
    // - If you're not here for the job, please leave.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002229$
                // - Industrialization, urban development... I don't know who'll really benefit from all that.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
