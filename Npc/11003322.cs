using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003322: Soldier
/// </summary>
public class _11003322 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0424104307008425$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0424104307008426$
                // - The enemy is up to something.
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
