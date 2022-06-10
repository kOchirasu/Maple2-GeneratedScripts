using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001234: Ryder
/// </summary>
public class _11001234 : NpcScript {
    internal _11001234(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1125194807004482$ 
                // - Have you seen anyone out of place? 
                return true;
            case 30:
                // $script:1125194807004485$ 
                // - $npc:11001231[gender:0]$ hurt dozens of us when he escaped last night. We all knew we didn't stand a chance, but what else could we do? I'm in no shape to help bring him in, but at least I can keep a lookout. 
                return true;
            default:
                return true;
        }
    }
}
