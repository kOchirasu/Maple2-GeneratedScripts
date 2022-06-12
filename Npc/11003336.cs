using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003336: Dark Wind Agent
/// </summary>
public class _11003336 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0510143807008460$
    // - We've been betrayed...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0510145607008464$
                // - Who told them...?
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
