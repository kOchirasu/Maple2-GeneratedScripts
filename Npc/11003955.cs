using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003955: Knight
/// </summary>
public class _11003955 : NpcScript {
    internal _11003955(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010001$ 
                // - Hi there.
                return true;
            case 20:
                // $script:0614143707010002$ 
                // - So you're an adventurer? You seem pretty strong. Nice to meet you.
                return true;
            default:
                return true;
        }
    }
}
