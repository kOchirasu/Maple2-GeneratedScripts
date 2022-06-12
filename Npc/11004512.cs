using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004512: Mannstad Pilot
/// </summary>
public class _11004512 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012465$
    // - Hey, you're that outlander!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012466$
                // - Hey, you're that outlander!
                return 10;
            case (10, 1):
                // $script:1228182607012467$
                // - This is the hub of all of our mobile forces, by land and air. But ever since the enemy pushed to our doorstep, we haven't been able to secure a supply line for the life of us.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
