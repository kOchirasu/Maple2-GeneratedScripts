using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000648: Prisoner 160921
/// </summary>
public class _11000648 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407002651$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002655$
                // - I can't wait to get out of here. How much longer? 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
