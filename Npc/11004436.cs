using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004436: Schatten
/// </summary>
public class _11004436 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1213154907011976$
    // - I am the shadow that evil fears.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1213154907011977$
                // - Hey there, $male:handsome,female:gorgeous$. After I've racked up some shore leave, what say we take a tour of Kritias's inns and test out their bed springs?
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
