using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001853: Dr. Henry
/// </summary>
public class _11001853 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1020165907007321$
    // - I'm glad you're all right.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1020165907007322$
                // - I'm glad you've made a quick recovery.  Come and see me whenever you're hurt. You can pop in for a checkup in the hospital lobby, just outside the patient rooms. 
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
