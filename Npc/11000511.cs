using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000511: Elliana Shuabritze
/// </summary>
public class _11000511 : NpcScript {
    internal _11000511(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000580$ 
                // - What do you want? 
                return true;
            case 10:
                // $script:0624180010002188$ functionID=1 
                // - Do you have old enchanted equipment you don't need anymore? I'll turn it into a scroll so you can transfer the enchantment to your new gear! 
                return true;
            default:
                return true;
        }
    }
}
