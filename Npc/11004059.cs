using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004059: Beatrice
/// </summary>
public class _11004059 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010091$
    // - The Alemani family will devote all of their resources to aid in the recovery effort.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010092$
                // - My other half... You have forged a blood oath. I expect you to aid me til the very end.
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
