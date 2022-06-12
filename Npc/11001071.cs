using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001071: Damon
/// </summary>
public class _11001071 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003651$
    // - Are you sure you came to see me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003654$
                // - The streets here look like a jungle.
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
