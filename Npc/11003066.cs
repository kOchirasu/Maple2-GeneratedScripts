using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003066: Dina
/// </summary>
public class _11003066 : NpcScript {
    internal _11003066(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102155907007650$ 
                // - $MyPCName$, I'll always remember you.
                return true;
            case 30:
                // $script:0102155907007651$ 
                // - I was told humans were selfish, foul creatures... but in the end, a human saved me.
                switch (selection) {
                    // $script:0102155907007652$
                    // - How do you feel?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0102155907007653$ 
                // - I'll live, thanks to you. We snowcubs are strong. That's all.
                return true;
            default:
                return true;
        }
    }
}
