using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004199: Nelph
/// </summary>
public class _11004199 : NpcScript {
    internal _11004199(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010646$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:0806025707010647$ 
                // - I'm delighted to be visiting $map:02000499$ with my mother. Of course, I won't be engaging in the tourney myself. Mother and I will be quite happy to cheer the contestants on from the sidelines. 
                return true;
            default:
                return true;
        }
    }
}
