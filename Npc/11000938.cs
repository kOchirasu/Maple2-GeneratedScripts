using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000938: 
/// </summary>
public class _11000938 : NpcScript {
    internal _11000938(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000861$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000862$ 
                // - Can I help you?
                return true;
            default:
                return true;
        }
    }
}
