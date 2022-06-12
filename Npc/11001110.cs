using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001110: Marr
/// </summary>
public class _11001110 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003732$
    // - What's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003735$
                // - I knew $npcName:11000064[gender:0]$ didn't betray us!
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
