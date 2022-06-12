using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004316: Mason
/// </summary>
public class _11004316 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0928133807011358$
    // - It is time my order stood with the rest of the empire.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0928133807011359$
                // - A strange power hangs over this place. A dark power... 
                return -1;
            case (20, 0):
                // $script:0116153807012736$
                // - Return to me when the time is right.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
