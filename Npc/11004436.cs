using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004436: Schatten
/// </summary>
public class _11004436 : NpcScript {
    internal _11004436(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213154907011976$ 
                // - I am the shadow that evil fears.
                return true;
            case 10:
                // $script:1213154907011977$ 
                // - Hey there, $male:handsome,female:gorgeous$. After I've racked up some shore leave, what say we take a tour of Kritias's inns and test out their bed springs?
                return true;
            default:
                return true;
        }
    }
}
