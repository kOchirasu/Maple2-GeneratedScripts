using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003468: Hidden Passage
/// </summary>
public class _11003468 : NpcScript {
    internal _11003468(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008673$ 
                // - <font color="#909090">(You can feel a breeze from beyond the wall. Is there a secret passage?)</font>
                return true;
            case 10:
                // $script:0706160807008674$ 
                // - <font color="#909090">(You can feel a breeze from beyond the wall. Is there a secret passage?)</font>
                return true;
            default:
                return true;
        }
    }
}
