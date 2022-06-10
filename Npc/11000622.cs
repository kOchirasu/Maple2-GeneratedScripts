using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000622: Terrence
/// </summary>
public class _11000622 : NpcScript {
    internal _11000622(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002527$ 
                // - We need more people to handle the damage. 
                return true;
            case 10:
                // $script:0831180407002528$ 
                // - Mushrooms want wooden ladders. Just wooden ones! 
                return true;
            default:
                return true;
        }
    }
}
