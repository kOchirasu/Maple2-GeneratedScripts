using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000524: Nick
/// </summary>
public class _11000524 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002243$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002245$
                // - Don't sweat it. Crime is pretty bad around here. That's just how it is.
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
