using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003522: Little Tree Sprite
/// </summary>
public class _11003522 : NpcScript {
    internal _11003522(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009026$ 
                // - What's happening?
                return true;
            case 30:
                // $script:0816160115009027$ 
                // - Lookit me!
                return true;
            case 40:
                // $script:0816160115009028$ 
                // - What's happening?
                return true;
            default:
                return true;
        }
    }
}
