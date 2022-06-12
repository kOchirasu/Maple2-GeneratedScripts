using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000607: Sudas
/// </summary>
public class _11000607 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002499$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002502$
                // - Merchants like me and the palace workers are only allowed entry through the underground passageway. I wonder if I'll ever have the honor of passing through the main gates... 
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
