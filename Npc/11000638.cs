using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000638: Prisoner 140921
/// </summary>
public class _11000638 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407002600$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002603$
                // - I really want to get out of here. Please help me. I'm sorry for what I did. I really am. 
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
