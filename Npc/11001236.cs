using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001236: Lennon
/// </summary>
public class _11001236 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1123130907004421$
    // - Blast it...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1123130907004423$
                // - I have to stop him.
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
