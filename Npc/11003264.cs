using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003264: Anne
/// </summary>
public class _11003264 : NpcScript {
    internal _11003264(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008208$ 
                // - I can't believe this happened to $map:02000023$. 
                return true;
            case 30:
                // $script:0403155707008209$ 
                // - We should have been ready for this. It was naive to think Ellinel was safe...
                return true;
            default:
                return true;
        }
    }
}
