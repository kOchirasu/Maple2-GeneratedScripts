using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003957: Thief
/// </summary>
public class _11003957 : NpcScript {
    internal _11003957(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010005$ 
                // - Eh? You... 
                return true;
            case 20:
                // $script:0614143707010006$ 
                // - Are you here casing the joint? I've got dibs, alright?! 
                return true;
            default:
                return true;
        }
    }
}
