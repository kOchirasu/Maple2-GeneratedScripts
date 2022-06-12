using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001099: Oska
/// </summary>
public class _11001099 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003697$
    // - Hmm... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003698$
                // - This place is $map:52000011$. It channels the power of the Red Lapenta to maintain order among the timelines.
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
