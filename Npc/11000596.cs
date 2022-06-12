using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000596: Ting
/// </summary>
public class _11000596 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002392$
    // - I'm busy, so busy!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002395$
                // - I have to do homework, and I have to study... 
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
