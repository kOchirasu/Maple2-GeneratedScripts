using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001501: Dunba
/// </summary>
public class _11001501 : NpcScript {
    internal _11001501(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0118150907005840$ 
                // - You know I outrank you, right? Hah hah! 
                return true;
            case 30:
                // $script:0118150907005843$ 
                // - Don't just stare at your food, eat it! So rude. 
                return true;
            default:
                return true;
        }
    }
}
