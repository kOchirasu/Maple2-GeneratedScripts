using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003215: Lennon
/// </summary>
public class _11003215 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0404083307008241$
    // - You've been following me. Why?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008242$
                // - I can tell you aren't one of $npcName:11000044$'s men.
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
