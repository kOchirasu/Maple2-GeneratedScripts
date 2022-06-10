using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000002: Rina
/// </summary>
public class _11000002 : NpcScript {
    internal _11000002(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000010$ 
                // - What's the matter, dear? 
                return true;
            case 10:
                // $script:0831180407000011$ 
                // - Now that the court's been canceled, everyone has been clearing out of here. I used to pray for this day to come, but now the city feels so empty. 
                return true;
            case 20:
                // $script:0831180407000012$ 
                // - Welcome, $MyPCName$. I was just about done with this batch of cookies. Would you like to wait for them? My fresh-baked cookies are famous here in $map:02000001$, you know. 
                return true;
            default:
                return true;
        }
    }
}
