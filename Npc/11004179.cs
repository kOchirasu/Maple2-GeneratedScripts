using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004179: Karl
/// </summary>
public class _11004179 : NpcScript {
    internal _11004179(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010620$ 
                // - What is it? 
                return true;
            case 10:
                // $script:0806025707010621$ 
                // - My greatest joy is seeing my daughter smile. I would have visited this place sooner if I had known it would make $npcName:11004180[gender:1]$ so happy. 
                return true;
            default:
                return true;
        }
    }
}
