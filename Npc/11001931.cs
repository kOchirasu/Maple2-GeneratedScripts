using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001931: Apprentice Ladme
/// </summary>
public class _11001931 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1122150407007454$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1122214707007472$
                // - I can't afford these materials. I'll just have to get some on my own... 
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
