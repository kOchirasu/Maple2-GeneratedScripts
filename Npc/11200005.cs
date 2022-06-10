using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11200005: Shuenji
/// </summary>
public class _11200005 : NpcScript {
    internal _11200005(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0518100907008515$ 
                // - The guild could use your help. You will be compensated! 
                return true;
            case 30:
                // $script:0518100907008518$ 
                // - Complete this simple task, and you will get guild experience, funds, and some experience for yourself, too! Note that you can't start daily quests until you've been in the guild for a day, and you can't start weekly quests until you've been in the guild for a week. 
                return true;
            default:
                return true;
        }
    }
}
