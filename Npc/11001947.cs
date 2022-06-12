using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001947: Violin Student
/// </summary>
public class _11001947 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1123165007007493$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1208184307007539$
                // - Are you here for the audition? You better grab your instrument and start practicing while you still can. 
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
