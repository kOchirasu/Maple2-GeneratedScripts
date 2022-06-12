using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001932: Apprentice Tochi
/// </summary>
public class _11001932 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1122150407007455$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1122214707007475$
                // - Handicrafts are so fun that I often lose track of the time. I just wish I had someone to actually give this stuff to... 
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
