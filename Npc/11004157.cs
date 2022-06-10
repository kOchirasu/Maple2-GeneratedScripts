using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004157: Mr. Buns
/// </summary>
public class _11004157 : NpcScript {
    internal _11004157(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010585$ 
                // - Meow! 
                return true;
            case 10:
                // $script:0806025707010586$ 
                // - Nom nom nom nom!
<font color="#909090">(He flops his ears joyfully.)</font> 
                return true;
            default:
                return true;
        }
    }
}
