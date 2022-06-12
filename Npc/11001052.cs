using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001052: Alicia
/// </summary>
public class _11001052 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003592$
    // - Wah... I messed it up!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003595$
                // - No one can imagine how exciting time travel is without trying it.
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
