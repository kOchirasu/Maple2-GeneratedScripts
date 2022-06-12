using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000471: Vito
/// </summary>
public class _11000471 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002062$
    // - Ah, what is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002064$
                // - I know height isn't everything, but I really don't like being shorter than most people... 
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
