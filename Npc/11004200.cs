using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004200: Mrs. Ibelin
/// </summary>
public class _11004200 : NpcScript {
    internal _11004200(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010648$ 
                // - What is it?
                return true;
            case 10:
                // $script:0806025707010649$ 
                // - My son is always thinking of me, and it makes me so very happy. He's such a good boy! I don't know how I'd get along without him.
                return true;
            default:
                return true;
        }
    }
}
