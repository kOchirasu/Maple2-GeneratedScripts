using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003335: Barista
/// </summary>
public class _11003335 : NpcScript {
    internal _11003335(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0510143807008459$ 
                // - What do you want?!
                return true;
            case 10:
                // $script:0510145607008463$ 
                // - You'll get nothing out of me!
                return true;
            default:
                return true;
        }
    }
}
