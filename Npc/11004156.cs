using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004156: Tutu
/// </summary>
public class _11004156 : NpcScript {
    internal _11004156(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010583$ 
                // - Wahhh...
                return true;
            case 10:
                // $script:0806025707010584$ 
                // - Yawn... Boooring. I think I liked working in $map:82000000$ better, even with the occasional beatings.
                return true;
            default:
                return true;
        }
    }
}
