using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000224: Linda
/// </summary>
public class _11000224 : NpcScript {
    internal _11000224(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000976$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000978$ 
                // - My boyfriend and I came here for a picnic, and we ended up fighting because he kept looking at other girls. The nerve!
                return true;
            default:
                return true;
        }
    }
}
