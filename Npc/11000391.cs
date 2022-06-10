using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000391: Rotiana
/// </summary>
public class _11000391 : NpcScript {
    internal _11000391(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001589$ 
                // - What? 
                return true;
            case 20:
                // $script:0831180407001591$ 
                // - Have you just arrived in $map:02000001$? I came here three days ago and I'm already sick of this city. What a waste. 
                return true;
            default:
                return true;
        }
    }
}
