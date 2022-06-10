using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004140: Aisha
/// </summary>
public class _11004140 : NpcScript {
    internal _11004140(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010551$ 
                // - What is it?
                return true;
            case 10:
                // $script:0806025707010552$ 
                // - Sometimes I wish I wasn't so amazing at everything...
                return true;
            default:
                return true;
        }
    }
}
