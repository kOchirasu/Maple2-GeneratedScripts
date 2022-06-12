using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000841: Miruka
/// </summary>
public class _11000841 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003076$
    // - Sigh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003079$
                // - I think that doctor is a quack. The more he treats me, the worse I feel. Sigh... 
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
