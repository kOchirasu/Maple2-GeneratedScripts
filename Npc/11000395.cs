using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000395: Yamoto
/// </summary>
public class _11000395 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001603$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001605$
                // - Everyone here works hard, including me, but we can't ever seem to get ahead. It's sad, and I've heard $map:02000100$'s mayor is responsible for keeping us all poor. 
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
