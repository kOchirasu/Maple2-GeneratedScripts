using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003456: Muphaza
/// </summary>
public class _11003456 : NpcScript {
    internal _11003456(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008667$ 
                // - I am prepared to dedicate my life to the peace of $map:02000051$. 
                return true;
            case 10:
                // $script:0706160807008668$ 
                // - I am prepared to dedicate my life to the peace of $map:02000051$. 
                return true;
            default:
                return true;
        }
    }
}
