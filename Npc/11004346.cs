using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004346: Aiden
/// </summary>
public class _11004346 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011749$
    // - Why must the holidays always be so stressful...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011750$
                // - Why must the holidays always be so stressful...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
