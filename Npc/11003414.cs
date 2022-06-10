using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003414: Hero's Tomb
/// </summary>
public class _11003414 : NpcScript {
    internal _11003414(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0623153207008575$ 
                // - <i>Here lies Sharp Claw, the war chief who rebuilt $map:02000051$. His kind heart and dedicated work uplifted our people during our time of need, and for that he will always be remembered.</i>
                return true;
            case 10:
                // $script:0623180607008577$ 
                // - <i>Here lies Sharp Claw, the war chief who rebuilt $map:02000051$. His kind heart and dedicated work uplifted our people during our time of need, and for that he will always be remembered.</i>
                return true;
            default:
                return true;
        }
    }
}
