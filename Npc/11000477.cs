using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000477: Praise Goldus
/// </summary>
public class _11000477 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002078$
    // - There's a name on it: $npcName:11000477$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002079$
                // - The Goldus way! Put your back into it! Pinch a penny, make a penny!
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
