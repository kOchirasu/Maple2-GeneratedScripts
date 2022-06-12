using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000703: Kennis
/// </summary>
public class _11000703 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002830$
    // - Ugh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002832$
                // - Time is of the essence. We must request backup right away.
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
