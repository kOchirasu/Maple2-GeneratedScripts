using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000604: Apollo
/// </summary>
public class _11000604 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002485$
    // - ... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002486$
                // - Keep it down out there, I'm trying to read!
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
