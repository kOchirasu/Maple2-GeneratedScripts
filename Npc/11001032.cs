using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001032: Herman
/// </summary>
public class _11001032 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003529$
    // - This is bad, really bad!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003532$
                // - I'm the head of this robot development center, and even I don't know how to get these robots under control. What should I do to contain this problem?
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
