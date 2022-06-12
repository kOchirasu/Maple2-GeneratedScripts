using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000646: Prisoner 160919
/// </summary>
public class _11000646 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002642$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002645$
                // - It's been three days since the toilet overflowed...
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
