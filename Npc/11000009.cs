using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000009: Rolling Thunder
/// </summary>
public class _11000009 : NpcScript {
    internal _11000009(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000055$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:0831180407000058$ 
                // - Have you heard of $map:02000051$? The cliffs there are so treacherous that most people wouldn't dare climb it.
                // $script:0831180407000059$ 
                // - If you have the chance, you should visit $map:02000051$ and visit my dad. Tell him you're $npcName:11000009[gender:0]$'s friend and you'll be like one of the family.
                switch (selection) {
                    // $script:0831180407000060$
                    // - Who is your father?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000061$ 
                // - Oh, don't worry. You'll know him when you see him.
                return true;
            default:
                return true;
        }
    }
}
